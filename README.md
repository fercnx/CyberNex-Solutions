# Backend de CYBERNEX 10.0V (preparado, no conectado)

Esta carpeta contiene la **base** para el portal NEX Connect y el panel administrativo.
**Nada del sitio actual depende de ella**: el sitio funciona completo en GitHub Pages sin backend.

| Archivo | Para qué sirve |
|---|---|
| `schema.sql` | Tablas, validaciones y políticas de seguridad (RLS) para Supabase/PostgreSQL |
| `.env.example` | Variables de entorno necesarias (sin valores reales) |

## Qué falta para activarlo (no existe todavía)
1. Crear un proyecto en [Supabase](https://supabase.com) y ejecutar `schema.sql` en su editor SQL.
2. Copiar `.env.example` a `.env` y completar las claves. **La clave `SERVICE_ROLE` nunca debe estar en el frontend ni en GitHub.**
3. Implementar las pantallas de registro, inicio de sesión y panel (siguiente etapa). Supabase Auth guarda las contraseñas con hash; este proyecto nunca las guarda en texto plano.
4. Para el formulario de contacto con protección anti-spam, añadir un CAPTCHA y una función de servidor que valide el token con `CAPTCHA_SECRET`.
5. Alojar la API (si se usa Node.js) en un servicio compatible y definir `ALLOWED_ORIGIN` con el dominio de GitHub Pages.

## Estado honesto
- El esquema **no ha sido ejecutado** contra una base de datos real en esta entrega; revisarlo y probarlo es parte de la siguiente etapa.
- No hay inicio de sesión, portal ni panel funcionando todavía. El sitio no los simula.
