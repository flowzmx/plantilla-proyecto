# Turnos y chats

- **Cambio de turno** al % de memoria que eligió el dueño (en `AGENTS.md`; recomendado 40–50 %). Antes: nota de relevo en `planeacion/relevos/AAAA-MM-DD-HHMM-<puesto>.md` (qué hice, qué falta, dónde quedé, siguiente pregunta al dueño).
- Memoria: Claude Code `/context`; Codex `/status` (dice lo que **queda**).
- **Latido de todos, siempre (Claude y ChatGPT):** cada vuelta del Coordinador escribe en la rama `activador-estado` el estado de todos sus chats con su energía (`documentos/LATIDO.md`). Trabajando sin latido > 60 min = «Se paró».
- **Un solo chat de supervisor/planeación a la vez.** Antes de abrir otro, cerrar el viejo y sus tareas programadas: dos chats se pisan y avisan doble.
- Nadie se queda quieto; una sola revisión por entrega; si se esperan entre sí, el Coordinador decide quién sigue.
