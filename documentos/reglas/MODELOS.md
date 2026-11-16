# Qué modelo usa cada puesto (y con qué intensidad)

Desde v3.8 (16-nov-2026). Medido en el proyecto de prueba (`flowzmx/prueba-del-metodo`, `documentos/MODELOS.md` y `documentos/COSTOS.md`). Muestra chica: se ajusta con cada medición nueva.

| Puesto | Modelo | Intensidad | Por qué |
|---|---|---|---|
| Planeación | Opus | Alta | Piensa, diseña y habla con el dueño |
| Revisor (escribe la prueba antes y revisa lado a lado) | Opus | **Alta** en lo delicado (dinero, permisos, facturas, datos de personas); **Media** en pantallas y cosas chicas | La revisión es lo más caro del camino; en lo no delicado basta media |
| Coordinador | Opus | Media | Reparte y vigila. Su vuelta corta va en un guion sin IA cuando exista (plan B) |
| Trabajador de módulo delicado | Sonnet | Alta | Lógica, dinero y permisos |
| Trabajador de pantalla normal | Sonnet | Media | Medido: 8.5/10 en una pantalla mediana |
| Trabajador de cosas chicas (guías, tutoriales, textos, arreglos de color o lugar) | Haiku | Media | Medido: 8/10 en un tutorial |
| Ayudantes (buscar, rondas, avisos) | Haiku | Baja | Trabajo mecánico |

## Qué IA en cada puesto (v3.14)
- **Coordinador: siempre Claude Code.** Es el único que se despierta solo (tarea programada desde afuera), ve la memoria de cada chat y abre a sus trabajadores.
- **Trabajadores: «trabajamos con todo».** Claude (Sonnet/Haiku, tabla de arriba) **o ChatGPT/Codex**, según qué cuenta tenga crédito. Los de Codex los lanza el Coordinador desde el servidor (`codex exec` por encargo, su propia rama, recibo con resumen de 5 líneas), sin que el dueño abra chats; a mano en chatgpt.com solo si algo no se puede.
- **Revisor:** Claude (Opus) que no construyó, aunque la pieza la haya hecho Codex.
- Lo que no se ve de Codex desde afuera (memoria, crédito) se anota «no se pudo»; el Coordinador lo vigila por sus entregas y su latido.
- En prueba con el primer proyecto que trabaja así; se ajusta con lo que se mida.

## Cuentas chicas
Una persona con cuenta de **US$20 (Pro)** trabaja **solo con Haiku** (decisión del dueño, 16-nov-2026): le tocan piezas de «cosas chicas». Si su pieza resulta más grande, sube a una cuenta mayor; no cambia de modelo en su cuenta. Su revisión la hace un Opus de otra cuenta.

## Reglas de oro
1. **Quien construye nunca se califica.** Siempre revisa un Opus que no construyó esa pieza.
2. **Revisión lado a lado en una sola imagen** (lo aprobado junto a lo construido), no de memoria.
3. **La prueba se escribe antes** de construir, y el que construye no la cambia.
4. Si un modelo barato falla 2 veces seguidas igual, la pieza sube un escalón (Haiku → Sonnet → Opus).
5. Si una intensidad o modelo no se puede elegir o leer en una plataforma, se anota «no se pudo»; nunca se inventa.

## Lo que se sabe (y lo que no)
- Ahorro medido de Haiku o Sonnet + revisión Opus contra solo Opus: **unas 2–3 veces** (n = 2), no 40. Revisar cuesta más que construir.
- El gasto más grande es el Coordinador dando vueltas: bajarlo con el plan B.
- Haiku puede «cumplir la foto, no la regla» (fijó una fecha para pasar la prueba): por eso la regla 1 y 3.
- Falta medir: Trabajador delicado con Sonnet, ayudantes con Haiku, y revisión Opus media (2 revisiones más).
