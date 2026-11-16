# Latido: cómo un chat le dice al panel que está vivo

El latido es una notita por chat, cada 15 minutos, en la rama aparte `activador-estado` del repositorio del proyecto. Así no despierta a nadie. La escribe el despertador del proyecto, el propio chat **o el Coordinador en cada vuelta para todos sus chats** (lo más simple: él ya mide la memoria de cada uno). El panel solo la lee. **Regla v2: siempre, en Claude y en ChatGPT**; un chat «trabajando» sin latido por más de 60 min sale como «Se paró».

```json
{
  "proyecto": "mi-proyecto",
  "chat": "F1 · Biblioteca y diseño",
  "rol": "cuadrilla",
  "quien": "chat",
  "cuenta_github": null,
  "ia": "codex",
  "hora": "2026-11-15T15:30:00Z",
  "estado": "trabajando",
  "tarea": "Portada #2, opción A",
  "memoria_usada_pct": 32,
  "espera_a": null,
  "espera_al_dueno": false,
  "ultima_entrega": "2026-11-15T15:12:00Z",
  "error": null
}
```

- `quien`: `chat` o `persona`. Si es una persona, `cuenta_github` lleva su usuario de GitHub (para los colaboradores con su propio Codex).
- `estado`: `trabajando` | `en espera` | `apagado` | `solo ver`.
- `memoria_usada_pct`: si no hay dato, va `null`. **Nunca se inventa.**
- Nada de texto de conversación, llaves, rutas privadas ni correos.

## Compatibilidad con proyectos que ya tenían su propio estado
Un proyecto que ya publica su propio `estado.json` con `chats[]` (`chat`, `estado`, `decision`, `espera_a_<dueño>`, `ultimo_despertar`) y `historial.jsonl`. El lector del panel acepta ese formato tal cual y lo traduce a este.

## Memoria de Codex (`/status`)
Codex guarda cada sesión en `~/.codex/sessions/**/*.jsonl` del equipo donde corre. Ahí, los eventos `type: "event_msg"` con `payload.type: "token_count"` traen `payload.info.total_token_usage` (`input_tokens`, `cached_input_tokens`, `output_tokens`, `total_tokens`). Así lo lee Mission Control (builderz-labs, MIT, `src/lib/codex-sessions.ts`).

El despertador de cada proyecto calcula el porcentaje contra la ventana de contexto que reporte la propia sesión y lo pone en `memoria_usada_pct`. Si la sesión no reporta la ventana, va `null`. El panel nunca lee esos archivos directamente, porque están en el servidor del proyecto.

## Chats sin medidor (claude.ai) · el dueño, 15-nov
Un chat de claude.ai no sabe cuánta memoria lleva: manda `memoria_usada_pct: null`, `ia: "claude-ai"` y además:
- `abierto`: cuándo se abrió el chat (ISO UTC, p. ej. `2026-11-15T23:00Z`).
- `vueltas`: cuántas revisiones o respuestas lleva (número entero).
El panel lo enseña como **«Sin medidor» · abierto hace X · N vueltas**, y a las **6 horas o 40 vueltas** sale «Ya toca cambio de turno». Nunca se inventa un %.
- `frase_relevo` (opcional): lo que el dueño pega en el chat nuevo cuando el cambio de turno es a mano (si falta: «Lee el relevo y sigue.»).
- `lugar` (opcional): dónde se abre el chat nuevo, p. ej. «el Proyecto «Mi proyecto» de claude.ai».
Con «Ya toca cambio de turno» sale **«Cambiar de turno ›»**: ventanita con 3 pasos y las palabras listas para copiar (t01, el dueño «a»).

## Siempre visibles hasta archivarse · sin choques (el dueño, 15-nov)
- Un chat sale en Ayudantes **siempre**, aunque esté callado, hasta que su renglón diga `estado: "relevado"` (o `"archivado"`); entonces pasa a «Relevados · N» (cerrado, abajo).
- Un chat de claude.ai callado más de 1 h sale **«En espera · espera que le escribas»**, nunca «Se paró».
- **Al tomar el turno, el chat nuevo marca al viejo** como `estado: "relevado"` en `estado.json` (y pone su propio renglón con nombre nuevo, p. ej. «Planeación (2)»).
- Si dos chats vivos tienen **el mismo nombre o la misma tarea**, sale arriba en rojo: «Ojo: A y B están en lo mismo».

## Cuentas y crédito (el dueño, 15-nov, «constrúyelo»)
- Cada chat dice con la cuenta de quién trabaja: `cuenta: "Ana"` (solo el nombre de la persona; nunca correo ni contraseña).
- Quien escribe los latidos (despertador o Coordinador) agrega en `estado.json` un pedacito por cuenta conectada en el servidor:
  `"cuentas": [{"nombre": "Dueño", "ia": "claude", "queda": 10, "renueva": "21:00", "hora": "2026-11-16T00:10Z"}]`
  - `queda`: % que le queda a la cuenta de su límite actual (Codex lo guarda en sus sesiones como `rate_limits` del último `token_count`: queda = 100 − `used_percent`; Claude Code: lo que diga su propio aviso de uso). Si no se puede leer, **no se manda** (sale «sin dato»). Nunca se inventa.
  - **Etiqueta de cada cuenta:** en el servidor cada cuenta de IA vive en **su propia carpeta** (Codex: `CODEX_HOME`; Claude Code: `CLAUDE_CONFIG_DIR`; la de siempre es la del dueño). Dentro va un archivo `cuenta.txt` con el nombre de la persona (p. ej. `Ana`). Quien escribe los latidos lee esa etiqueta para poner `nombre` y la `cuenta` de cada chat. **Nunca dos personas en la misma carpeta.** Cuenta sin etiqueta: se manda como «sin nombre» y se pregunta al dueño; no se adivina.
- `renueva`: a qué hora se renueva, en hora de Monterrey, corto («21:00», «mañana 08:00»).
- El dueño acomoda las cuentas en el panel › **Ajustes** (`planeacion/ajustes.json`: % de cambio de turno, horas y vueltas de claude.ai, aviso de crédito, cuentas con «Trabaja» o «De respaldo»). Coordinador y despertador **leen ese archivo**: el % de cambio de turno manda sobre el de `AGENTS.md`.
- Si a una cuenta que trabaja le queda menos del aviso, el panel le ofrece al dueño **«Mover ›»**. Su orden queda en `planeacion/respuestas-*/AAAA-MM-DD-HHMM-mover-chats.md`; el Coordinador o el despertador la ejecutan en su siguiente vuelta (relevo, chat nuevo en la otra cuenta con número siguiente, viejo `relevado`; si no se puede abrir solo, las palabras exactas al dueño).
