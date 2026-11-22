# Comparativo de métodos: Flowz vs LexFree (documento vivo)
Arnaldo (22-nov-2026): «lexfree trabaja diferente a nosotros… la idea es ver cuál método es más eficiente». Aquí se anota **cómo trabaja Flowz** con hechos y números; el lado de LexFree lo llena su Coordinador (mismo formato). Lo actualiza el Coordinador en cada vuelta cuando hay un dato nuevo. El método base público vive en `flowzmx/plantilla-proyecto` (no se sube nada ahí sin ok de Arnaldo).

## 1. Cómo trabaja Flowz hoy (22-nov)
| Pieza | Flowz |
|---|---|
| Planeación | claude.ai (Proyecto): dibuja imágenes, Arnaldo las aprueba; solo eso. |
| Coordinador | Claude Code (Opus/Sonnet) en el servidor, dentro de `/opt/flowz`. Reparte, aprueba planes chicos, publica y lleva el pizarrón. Vuelta cada 30 min con `send_later`. Relevo a ~30–35 % de contexto. |
| Trabajadores | **Desde dec. 489 (22-nov 17:05): Codex (ChatGPT), uno por módulo**, abiertos por el Coordinador con `local_runtime/codex/abrir-trabajador.sh` (`codex exec`, sin caja `danger-full-access` por orden de Arnaldo, root en `/opt/flowz`). Antes (hasta esa hora): Claude Sonnet vía `create_session`. |
| Comunicación | Todo por el **pizarrón en GitHub** (rama `flowz-1.0`): pedidos (`pizarron/pedidos/`), bitácora, ESTADO, relevos. Claude→Claude también con `send_message`; **Codex no tiene `send_message`** (el Coordinador cierra el pedido con «Resultado:» y el Trabajador lo lee en `pedidos/cerrados/`). |
| Carpeta | **Una sola carpeta compartida** (`/opt/flowz`) para todos; cada uno solo su módulo; prohibido stash/reset/add -A. |
| Publicar | Coordinador: capa por módulo sobre la versión anterior, tsc/build, reinicios uno por uno, revisión «solo mirar». Desde dec. 487: lo aprobado y probado se publica sin pedir otro sí. |
| Reglas de Arnaldo | Una pantalla + pop-ups; solo imágenes aprobadas; modo pruebas; nada de borrar/cobrar/enviar real sin su ok. |

## 2. Datos medidos (22-nov)
- **Costo de Trabajadores Claude (Sonnet)** por chat, según `get_session` (`usage.cost_usd`): Clientes (7) US$2.21 · (8) 1.30 · (9) 4.37 · (10) 5.93 → ~US$14 por la ficha completa de Clientes en 4 chats y ~2.5 h. Coordinador (50) Opus: US$9.94 en ~10 h.
- **Rendimiento Sonnet:** la ficha de Clientes (k03, k04b/c, k05, k08, k09, k11b, k20, Bolsa) salió en 4 chats entre 14:53 y 17:11 UTC y se publicó (2.0.110, 50/50 en revisión) a las 17:10.
- **Relevos de más:** los Sonnet (7) y (8) pararon a ~18–24 % real creyendo estar al 35 % → 2 relevos evitables. Lección: el Coordinador mide con `get_session`, no confía en el % que dicen.
- **Límite del plan:** el límite semanal de Claude estuvo en aviso (renueva jue 26-nov 03:00 UTC); fue la razón de pasar Trabajadores a Codex.
- **Incidentes:** (a) un Opus publicador escribió `rm -f /dev/null` y rompió `/dev/null` ~1 min (reparado con `mknod`); (b) un Sonnet armó otro `rm -f /dev/null` el 21-nov. Causa común: `rm` dentro de comandos largos → regla «nada de borrar» + `mv` a papelera.
- **Codex:** instalación 22-nov 17:09 (`npm i -g @openai/codex`, v0.171.0), login por código (`codex login --device-auth`) hecho por Arnaldo en ~2 min. **La caja de Codex (bubblewrap) no funciona dentro de este contenedor** (`bwrap: Can't mkdir …`): sin quitarla, no puede ejecutar comandos. Con `danger-full-access` sí corre. 5 Trabajadores en paralelo a las 17:22; la carga del servidor se mantuvo ~1.
- **Colisiones de git:** al compartir carpeta, un `pull` del Coordinador puede chocar con archivos sin commit de un Trabajador (visto 17:23); se resuelve esperando su commit, nunca con reset.

## 3. Qué medir para decidir cuál método es más eficiente (se llena con el tiempo)
| Métrica | Flowz (Claude Trabajadores) | Flowz (Codex Trabajadores) | LexFree |
|---|---|---|---|
| Piezas entregadas «LISTO» por hora de trabajo | ficha Clientes: ~8 piezas/2.3 h (4 chats) | _por medir (desde 17:20)_ | _llenar_ |
| Costo por pieza (US$ / plan consumido) | ~US$14 / 8 piezas | _plan ChatGPT: por medir_ | _llenar_ |
| Re-trabajo (pedidos devueltos / piezas) | _por medir_ | _por medir_ | _llenar_ |
| Fallas en producción tras publicar | 0 en 2.0.110 | — | _llenar_ |
| Intervenciones de Arnaldo por pieza | bajas (solo imágenes + permisos) | _por medir_ | _llenar_ |
| Incidentes de seguridad/orden | 2 (`/dev/null`) | _por medir_ | _llenar_ |
| Relevos por pieza | 2 evitables de 4 | _por medir_ | _llenar_ |

## 4. Diferencias a documentar de LexFree (pendiente de su Coordinador)
Cómo abre trabajadores, si usa una carpeta por trabajador (worktrees) o compartida, cómo se comunican Codex↔Coordinador, cómo evita choques de git, cómo prueba/publica, cuánto gasta de plan, y qué le falla. Llenar en `planeacion/metodo/LEXFREE-como-trabaja.md` (su Coordinador) y volver aquí.

## 5. Registro de cambios del método (más nuevo arriba)
- 22-nov 17:5x · Documento creado. Trabajadores 5 en Codex en paralelo; respuestas del Coordinador por `pedidos/cerrados/`.
- 22-nov 17:05 · Dec. 489: Trabajadores a Codex. 17:2x · Dec. «A»: Codex sin caja. 
- 22-nov 16:55 · Dec. 487: publicar seguido lo aprobado y probado. 
- 22-nov 15:0x · Dec. 486: cuenta `flowz-prueba` admin permanente de los chats.
