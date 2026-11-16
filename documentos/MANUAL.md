# Método Flowz · lo que lee todo chat (versión en `METODO-VERSION`)

Hace que varias IAs (Claude, ChatGPT o la que siga) y personas trabajen solas en un proyecto, y que el dueño **solo decida** desde el panel con Sí / No. El método vive **solo aquí** (`flowzmx/plantilla-proyecto`, público); cada proyecto lo lee al empezar cada chat y el Coordinador, en cada vuelta, copia lo nuevo si `METODO-VERSION` subió. Las mejoras se proponen aquí y se anotan en `documentos/reglas/CAMBIOS.md`. Se afina «hasta el 10».

## La obra
El proyecto funciona como una obra. **Dueño** (decide) → **Supervisor** externo (vigila cada hora y escribe las respuestas del dueño) → **Repositorio y pizarrón** (todo queda guardado) ↔ **Planeación** (piensa, diseña y escribe las tareas) → **Coordinador** (abre los chats, reparte y vigila) → **Trabajadores** (construyen en un taller aparte) → **Buzón con guardia** (revisa, respalda e instala) → **Página real**. Un **Despertador** levanta a cada chat solo con lo suyo, y la **Torre de control** (este proyecto) se lo muestra al dueño.

## Las piezas
| Pieza | Qué es |
|---|---|
| Repositorio | El archivero: todo queda guardado con fecha y autor |
| Pizarrón | Solo los acuerdos vigentes, en 3,000 letras como máximo, con versiones |
| Hoja de módulos | Lo que hay que construir. Cada módulo tiene 5 pasos: Imagen, Construido, Probado, Revisión final, Publicado |
| Respuestas del dueño | Un archivo por decisión, con sus palabras |
| Despertador | Despierta a cada chat con lo suyo, al jefe cada 30 min, y avisa si algo lleva 60 min quieto o espera al dueño |
| Latido | La notita de cada chat cada 15 min (ver `LATIDO.md`) |
| Buzón con guardia | La única forma de publicar, con respaldo y vuelta atrás automáticos |
| 1Password | Toda llave nueva va solo ahí, en una bóveda por proyecto |

## Las 12 reglas
1. **Nunca quedarse quieto.** Si algo espera, tomar lo siguiente.
2. **Primero la Imagen** aprobada por el dueño; lo aprobado no se cambia.
3. **Todo lo del dueño pasa por el panel**, con preguntas que se entienden solas y recomendación → `reglas/PREGUNTAS.md`.
4. **Una sola revisión por entrega** (el 15-nov, 121 de 156 cambios eran revisiones).
5. **Recibo de terminado**: sin prueba anotada no está hecho (idea de Mission Control, builderz-labs, MIT).
6. **Nada llega a la página real sin el Sí del dueño**; una publicación a la vez → `reglas/PUBLICAR.md`.
7. **Nada real** (correos, cobros, clientes, borrar) sin permiso, uno por uno. **No pedir llaves**: solo en 1Password.
8. **Nada de comandos que pidan clic** de aprobación; aviso antes de cargas pesadas.
9. **Cambio de turno** a tiempo y **latido de todos** (Claude y ChatGPT) → `reglas/TURNOS-Y-CHATS.md`.
10. **Un solo supervisor/planeación** a la vez.
11. **Tutorial siempre** en cada pantalla nueva.
12. **Español sencillo** para el dueño: corto, con analogías, palabras de su negocio.

## Tu hoja (empieza aquí)
Cada chat lee **solo la hoja de su puesto** al empezar: `hojas/PLANEACION.md`, `hojas/COORDINADOR.md` o `hojas/TRABAJADOR.md` (una página cada una). Lo de abajo es de consulta, solo si hace falta.

## Piezas (lee solo las de tu puesto)
| Pieza | Para quién |
|---|---|
| `reglas/PREGUNTAS.md` | Planeación y Coordinador |
| `reglas/PUBLICAR.md` | Coordinador y Trabajadores |
| `reglas/TURNOS-Y-CHATS.md` | Todos |
| `reglas/MODELOS.md` (modelo e intensidad por puesto) | Todos, al abrir un chat |
| `ENTRAR-AL-EQUIPO.md` (una página) | Persona nueva con su propia cuenta |
| `reglas/ALARMAS.md` | Supervisor y Coordinador |
| `reglas/ARRANCAR.md`, `ARMAR-EQUIPO.md`, `CONECTAR-UN-PROYECTO.md` | Planeación, al empezar un proyecto |
| `LATIDO.md` | Coordinador (y el despertador) |
| `reglas/CAMBIOS.md` | Quien mejora el método |
| `skills/<puesto>/SKILL.md` | Cada puesto |

**Tamaños (como el pizarrón):** este archivo ≤ 4,000 letras; cada pieza ≤ 3,000. Si algo no cabe, se aprieta o se manda a su pieza.
