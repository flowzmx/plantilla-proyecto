# Latido: cómo un chat le dice al panel que está vivo

El latido es una notita por chat, cada 15 minutos, en la rama aparte `activador-estado` del repositorio del proyecto. Así no despierta a nadie. La escribe el despertador del proyecto o el propio chat. El panel solo la lee.

```json
{
  "proyecto": "lexfree",
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

## Compatibilidad con LexFree
LexFree ya publica `estado.json` con `chats[]` (`chat`, `estado`, `decision`, `espera_a_arnaldo`, `ultimo_despertar`) y `historial.jsonl`. El lector del panel acepta ese formato tal cual y lo traduce a este.

## Memoria de Codex (`/status`)
Codex guarda cada sesión en `~/.codex/sessions/**/*.jsonl` del equipo donde corre. Ahí, los eventos `type: "event_msg"` con `payload.type: "token_count"` traen `payload.info.total_token_usage` (`input_tokens`, `cached_input_tokens`, `output_tokens`, `total_tokens`). Así lo lee Mission Control (builderz-labs, MIT, `src/lib/codex-sessions.ts`).

El despertador de cada proyecto calcula el porcentaje contra la ventana de contexto que reporte la propia sesión y lo pone en `memoria_usada_pct`. Si la sesión no reporta la ventana, va `null`. El panel nunca lee esos archivos directamente, porque están en el servidor del proyecto.
