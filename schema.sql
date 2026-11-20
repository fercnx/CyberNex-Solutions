-- =====================================================================
-- CYBERNEX 10.0V — Esquema de base de datos para Supabase (PostgreSQL)
-- ESTADO: PREPARADO, NO CONECTADO. Nada en el sitio actual usa este
-- esquema todavía. Ejecútalo en el editor SQL de tu proyecto de Supabase.
-- La autenticación (registro, inicio de sesión, contraseñas con hash) la
-- gestiona Supabase Auth: este esquema NO guarda contraseñas.
-- =====================================================================

create extension if not exists "pgcrypto";

-- Perfiles: uno por usuario de Supabase Auth
create table if not exists public.profiles (
  id          uuid primary key references auth.users(id) on delete cascade,
  full_name   text not null check (char_length(full_name) between 2 and 120),
  company     text check (char_length(company) <= 120),
  role        text not null default 'client' check (role in ('client','admin')),
  created_at  timestamptz not null default now()
);

-- Solicitudes de servicio / cotización
create table if not exists public.service_requests (
  id          uuid primary key default gen_random_uuid(),
  client_id   uuid not null references public.profiles(id) on delete cascade,
  division    text not null check (division in ('development','security','academy','labs','other')),
  title       text not null check (char_length(title) between 3 and 140),
  description text not null check (char_length(description) between 10 and 4000),
  status      text not null default 'recibida' check (status in ('recibida','en_revision','cotizada','aprobada','en_progreso','entregada','cancelada')),
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);

-- Seguimiento de proyectos (derivados de una solicitud aprobada)
create table if not exists public.projects (
  id          uuid primary key default gen_random_uuid(),
  request_id  uuid references public.service_requests(id) on delete set null,
  client_id   uuid not null references public.profiles(id) on delete cascade,
  name        text not null,
  stage       text not null default 'planeacion' check (stage in ('planeacion','desarrollo','pruebas','entregado')),
  progress    int  not null default 0 check (progress between 0 and 100),
  created_at  timestamptz not null default now()
);

-- Mensajes entre cliente y empresa
create table if not exists public.messages (
  id          uuid primary key default gen_random_uuid(),
  request_id  uuid not null references public.service_requests(id) on delete cascade,
  sender_id   uuid not null references public.profiles(id) on delete cascade,
  body        text not null check (char_length(body) between 1 and 4000),
  created_at  timestamptz not null default now()
);

-- Archivos compartidos (metadatos; los archivos van en Supabase Storage)
create table if not exists public.shared_files (
  id           uuid primary key default gen_random_uuid(),
  request_id   uuid not null references public.service_requests(id) on delete cascade,
  uploaded_by  uuid not null references public.profiles(id) on delete cascade,
  storage_path text not null,
  file_name    text not null,
  created_at   timestamptz not null default now()
);

-- Mensajes del formulario de contacto (sin cuenta)
create table if not exists public.contact_messages (
  id          uuid primary key default gen_random_uuid(),
  name        text not null check (char_length(name) between 2 and 120),
  email       text not null check (email ~* '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  message     text not null check (char_length(message) between 10 and 4000),
  created_at  timestamptz not null default now()
);

-- Función auxiliar: ¿el usuario actual es administrador?
create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'admin');
$$;

-- ---------------------------------------------------------------------
-- Seguridad a nivel de fila (RLS): cada cliente solo ve lo suyo.
-- ---------------------------------------------------------------------
alter table public.profiles         enable row level security;
alter table public.service_requests enable row level security;
alter table public.projects         enable row level security;
alter table public.messages         enable row level security;
alter table public.shared_files     enable row level security;
alter table public.contact_messages enable row level security;

create policy "perfil: ver el propio o admin" on public.profiles for select using (id = auth.uid() or public.is_admin());
create policy "perfil: crear el propio (rol cliente)" on public.profiles for insert with check (id = auth.uid() and role = 'client');
create policy "perfil: editar el propio sin cambiar rol" on public.profiles for update using (id = auth.uid()) with check (id = auth.uid() and role = (select role from public.profiles where id = auth.uid()));

create policy "solicitudes: ver propias o admin" on public.service_requests for select using (client_id = auth.uid() or public.is_admin());
create policy "solicitudes: crear propias" on public.service_requests for insert with check (client_id = auth.uid());
create policy "solicitudes: admin actualiza" on public.service_requests for update using (public.is_admin());

create policy "proyectos: ver propios o admin" on public.projects for select using (client_id = auth.uid() or public.is_admin());
create policy "proyectos: solo admin escribe" on public.projects for all using (public.is_admin()) with check (public.is_admin());

create policy "mensajes: ver los de mis solicitudes o admin" on public.messages for select
  using (public.is_admin() or exists (select 1 from public.service_requests r where r.id = request_id and r.client_id = auth.uid()));
create policy "mensajes: escribir en mis solicitudes o admin" on public.messages for insert
  with check (sender_id = auth.uid() and (public.is_admin() or exists (select 1 from public.service_requests r where r.id = request_id and r.client_id = auth.uid())));

create policy "archivos: ver los de mis solicitudes o admin" on public.shared_files for select
  using (public.is_admin() or exists (select 1 from public.service_requests r where r.id = request_id and r.client_id = auth.uid()));
create policy "archivos: subir a mis solicitudes o admin" on public.shared_files for insert
  with check (uploaded_by = auth.uid() and (public.is_admin() or exists (select 1 from public.service_requests r where r.id = request_id and r.client_id = auth.uid())));

-- Contacto: cualquiera puede enviar (idealmente a través de la API con CAPTCHA); solo admin lee
create policy "contacto: enviar" on public.contact_messages for insert with check (true);
create policy "contacto: solo admin lee" on public.contact_messages for select using (public.is_admin());
