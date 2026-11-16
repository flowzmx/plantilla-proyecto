# Conectar un proyecto que ya existe a Flowz Proyectos

Para la IA de un proyecto que ya está en marcha (el que sea). El dueño quiere manejar **todos sus proyectos** desde Flowz Proyectos (proyectos.flowz.mx). El panel **solo lee GitHub**: si estos archivos existen con esta forma, el proyecto se ve completo. **No se toca el código del proyecto.**

## Reglas
- **Propuesta de cambio**: trabaja en una rama nueva y abre un pull request; el dueño lo aprueba. Nada directo a la rama principal.
- **No muevas ni renombres lo que ya existe** si otros chats lo usan. Si el proyecto ya tiene su hoja de módulos o su pizarrón con otro nombre, déjalos donde están y **anota la ruta** al final (el panel se configura con esas rutas).
- Nada de llaves, datos reales ni textos de conversación.

## Lo que el panel lee (y su forma)
1. **Hoja de módulos** (ej. `planeacion/MODULOS.md`):
   - Secciones `## Ahora`, `## Después` y `## Te toca, <Dueño>` (lista numerada; cada punto con el `#` del módulo que toca).
   - Fases `## 1. Nombre`, `## 2. …`, cada una con esta tabla exacta:
     `| # | Módulo | Imagen | Construido | Probado | Revisión final | Publicado | Qué falta | Siguiente paso |`
   - Marcas: ✅ hecho · 🔶 a medias · ⬜ falta · — no aplica. Solo ✅ con prueba o decisión anotada.
2. **Pizarrón** (ej. `PIZARRON.md`): lo vigente, máximo 3,000 letras.
3. **Respuestas del dueño**: una por archivo en `planeacion/respuestas-<dueño>/AAAA-MM-DD-HHMM.md` (sus palabras, la decisión, qué cambia).
4. **Equipo** (tres puestos: Planeación, Coordinador, Trabajadores):
   - `planeacion/equipo/chats.json`: `[{"puesto": "planeacion"}, {"puesto": "coordinador"}, {"puesto": "trabajador-1"}, …]` (puede llevar `"ia"` y `"skill"`).
   - Fichas: `planeacion/chats/00-planeacion.md`, `01-coordinador.md`, `11-trabajador.md`, `12-trabajador.md`…
   - Relevos: `planeacion/relevos/AAAA-MM-DD-HHMM-<puesto>.md` (ej. `2026-11-15-1325-trabajador-2.md`).
5. **Skills**: `skills/planeacion-flowz/`, `skills/coordinador-flowz/`, `skills/trabajador-flowz/` (cópialas de https://github.com/flowzmx/plantilla-proyecto/tree/main/skills) y las del proyecto en `skills/<nombre>/SKILL.md`, anotadas en `skills/README.md`.
6. **Latidos** (opcional, para «quién trabaja» y la barra de memoria): rama aparte `activador-estado` con `estado.json` (`chats[]` con `chat`, `estado`, `ia`, `memoria_usada_pct`, `espera_al_dueno`). Si no hay despertador, el panel muestra «sin dato».
7. **Reglas para los chats**: `AGENTS.md` corto (qué leer primero, los tres puestos, una sola revisión por entrega, relevo al % que eligió el dueño, los «No» de verdad). Toma como base el de https://github.com/flowzmx/plantilla-proyecto.

## Al terminar, dile al dueño (en una línea cada uno)
- Rama principal del proyecto y rutas de: hoja de módulos, pizarrón, respuestas del dueño.
- Si hay rama de latidos (`activador-estado`) o no.
- El número del pull request para aprobar.

Con eso, el dueño (o su supervisor) agrega el proyecto a la lista del panel.
