# Abrir un chat de {{nombre}}

Todos escriben en el pizarrón. Cada chat arranca con **un solo mensaje** y ya sabe qué hacer. (También sale en Flowz Proyectos → Chats → «Abrir un chat», con botón Copiar.)

## En Claude (claude.ai o Claude Code): cada chat va aparte
Abre un chat nuevo con el repositorio conectado y pega (cambia el puesto):
> Eres Planeación de {{nombre}} (método Flowz). Repositorio [usuario/repo], rama main. Lee AGENTS.md, tu ficha (planeacion/chats/00-planeacion.md), el pizarrón y tu último relevo, y sigue. Todo lo que hagas o decidas, escríbelo en el pizarrón.

Otros puestos: «Eres el Coordinador…» (ficha `01-coordinador.md`) · «Eres el Trabajador 1…» (ficha `11-trabajador.md`), Trabajador 2 → `12-trabajador.md`, etc.

## En Codex (ChatGPT): conviven todos en la misma carpeta
El mismo mensaje, y al final:
> Compartes carpeta con otros chats: antes de escribir trae lo último (git pull); toca solo tus archivos; si el pizarrón cambió mientras trabajabas, reléelo y junta los cambios antes de subir.

## Memoria (contexto)
Cada chat hace relevo al **{{relevo}} %**. Lo ves con `/context` (Claude Code) o `/status` (Codex, dice lo que **queda**). En claude.ai (web) no hay número: haz relevo cuando el chat esté largo o empiece a olvidar.
