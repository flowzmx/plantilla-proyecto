# Plantilla de proyecto · Flowz Proyectos

Repositorio plantilla. **No se trabaja aquí:** se crea un proyecto nuevo desde ella («Use this template») y la IA del dueño llena las marcas.

## Para la IA que arma el proyecto
1. Crea un repositorio privado nuevo desde esta plantilla, con el nombre que diga el dueño (en minúsculas, con guiones).
2. Reemplaza en todos los archivos estas marcas, menos en `tools/` y `documentos/`:
   - `{{nombre}}`: el nombre del proyecto · `{{dueno}}`: el nombre del dueño · `{{fecha}}`: hoy, como 15-nov-2026
   - `{{idea}}`: la idea del dueño, **con sus palabras, sin resumir**
   - `{{ia_planeacion}}`, `{{ia_coordinador}}`, `{{ia_trabajadores}}`: Claude, ChatGPT o Cualquiera · `{{equipo}}`: 2, 3 o 5 trabajadores
   - `{{relevo}}`: % de memoria para el cambio de turno (recomendado 50; el dueño puede escoger otro)
   - `{{disponibles}}`: «- (ninguna todavía)» (las skills de oficio del dueño no van en la plantilla pública)
3. Crea una ficha por trabajador en `planeacion/chats/1N-trabajador.md` («área por definir»; skill base `skills/trabajador-flowz`).
4. Borra este archivo (`PLANTILLA.md`) del proyecto nuevo, haz un solo commit en `main` y súbelo.
5. Lee `AGENTS.md`: eres **Planeación**. Haz `planeacion/encargos/00-propuesta-inicial.md`. **No construyas nada más** hasta que el dueño apruebe.
