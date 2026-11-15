# Turnos y chats

- **Cambio de turno** al % de memoria que eligió el dueño (en `AGENTS.md`; recomendado 40–50 %). Antes: nota de relevo en `planeacion/relevos/AAAA-MM-DD-HHMM-<puesto>.md` (qué hice, qué falta, dónde quedé, siguiente pregunta al dueño).
- Memoria: Claude Code `/context`; Codex `/status` (dice lo que **queda**: usada = 100 − queda).
- **Chats sin medidor (claude.ai):** no saben cuánta memoria llevan; nunca se inventa un %. Mandan `abierto` (hora en que se abrió) y `vueltas` (súmale 1 en cada revisión). **Cambio de turno a las 6 horas o 40 vueltas**, lo que pase primero.
- **Automático cuando se puede:** si el chat corre en el servidor (Claude Code o Codex), el Coordinador o el despertador hacen el cambio solo: piden la nota de relevo, abren el chat nuevo con «Lee el relevo y sigue» y marcan al viejo. **A mano cuando no se puede** (claude.ai, chatgpt.com): el panel enseña «Cambiar ›» con las palabras exactas para copiar; el latido puede traer `lugar` y `frase_relevo`.
- **Latido de todos, siempre (Claude y ChatGPT):** cada vuelta escribe en la rama `activador-estado` el estado de cada chat con su **IA, modelo** y energía (`documentos/LATIDO.md`). En `estado.json` cada chat **solo actualiza su renglón** (`git fetch` antes; nunca borra los de otros). Trabajando sin latido > 60 min = «Se paró» (claude.ai callado = «En espera», no se paró).
- **Nombres sin choques:** cada cambio de turno **sube el número** del nombre: «Supervisor» → «Supervisor (2)» → «(3)». El chat nuevo **marca al viejo** con `estado: "relevado"` (pasa a «Relevados» en el panel). Dos chats vivos con el mismo nombre o la misma tarea = aviso rojo.
- **Un solo chat por puesto.** Al relevarse, el viejo **deja de latir y apaga sus tareas programadas** (revisiones, resúmenes); si no, pisa al nuevo y avisa doble. Luego el dueño lo renombra «✅ Relevado · …».
- Un chat se ve en el panel **siempre**, aunque esté callado, hasta que se marca relevado.
- Nadie se queda quieto; una sola revisión por entrega; si se esperan entre sí, el Coordinador decide quién sigue.
