# Turnos y chats

- **Cambio de turno** al % que eligió el dueño (`AGENTS.md`; recomendado 40–50 %; `planeacion/ajustes.json` manda si existe). Antes: nota de relevo en `planeacion/relevos/AAAA-MM-DD-HHMM-<puesto>.md` (hecho, falta, dónde quedé, siguiente pregunta al dueño).
- **Memoria:** Claude Code `/context`; Codex `/status` (usada = 100 − queda). **claude.ai no tiene medidor:** nunca se inventa un %; manda `abierto` y `vueltas` y cambia a las **6 h o 40 vueltas**.
- **Relevo automático** si el chat corre en el servidor (Coordinador o despertador: piden la nota, abren «Lee el relevo y sigue», marcan al viejo). **A mano** en claude.ai o chatgpt.com: el panel enseña «Cambiar ›» con las palabras exactas.
- **Nombres:** cada turno sube el número («Supervisor (2)», «(3)»). El nuevo marca al viejo `relevado`; el viejo **deja de latir y apaga sus tareas programadas**. Dos chats vivos con el mismo nombre o tarea = aviso rojo. **Un solo chat por puesto.**
- **Latido de todos** (Claude y ChatGPT), cada vuelta, en la rama `activador-estado` (`documentos/LATIDO.md`): IA, modelo, energía y `cuenta` (nombre de la persona). Cada chat **solo toca su renglón** (`git fetch` antes). Trabajando sin latido > 60 min = «Se paró»; claude.ai callado = «En espera». Un chat se ve en el panel hasta que se marca relevado.
- **Cuentas:** cada una en su carpeta del servidor con su etiqueta `cuenta.txt` (sin etiqueta = «sin nombre», se pregunta). El dueño las acomoda en el panel › Ajustes; una orden «mover chats» se ejecuta en la siguiente vuelta.
- **Archivar, nunca borrar:** un chat relevado se archiva solo con (1) sucesor que aceptó, (2) relevo en GitHub con commit comprobado y (3) 2 h sin problemas. Nunca el activo ni uno con relevo dudoso.
- **Despertador de afuera (v3.9):** toda vuelta programada usa una tarea que entra al chat desde afuera (Claude Code: `send_later`; cada vuelta programa la siguiente). **Prohibido el reloj interno** (`CronCreate`, `/loop`): se apaga cuando la nube duerme el chat. Red de seguridad: el vigía del plan B.
- Nadie se queda quieto; una sola revisión por entrega; si se esperan entre sí, decide el Coordinador.
