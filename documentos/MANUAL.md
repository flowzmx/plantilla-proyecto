# Cómo trabajamos con IAs · Manual de Arnaldo

**Método Flowz v2 (15-nov-2026, tarde).** Versión en el repositorio del documento https://claude.ai/artifact/FCSd5JvozCBjj93g5Acss2. Nació en LexFree y se afinó el mismo día con Flowz y el panel. **Se sigue afinando «hasta el 10»** (Arnaldo): cada lección nueva se anota en «Cambios del método» (abajo) y se copia a cada proyecto.

## Para qué sirve
Hace que varias IAs trabajen solas y sin pararse en un proyecto. El dueño solo toma las decisiones de dueño. Funciona con cualquier IA (ChatGPT/Codex, Claude o la que siga).

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

## Reglas
1. Nunca quedarse quieto.
2. Una sola revisión por entrega. El 15-nov, 121 de 156 cambios eran revisiones entre chats.
3. Primero la Imagen, aprobada por el dueño.
4. Una sola pregunta al dueño: a/b, con una recomendada.
5. No pedir llaves nuevas.
6. Nada real (correos, cobros, clientes, borrar) sin permiso, uno por uno.
7. Aviso antes de cargas pesadas.
8. Nada de comandos que pidan clic de aprobación.
9. Una sola publicación a la vez.
10. Cambio de turno al % de memoria que elija el dueño (recomendado 50 %; puede escoger otro).
11. Recibo de terminado: sin prueba anotada no está hecho. La idea viene de Mission Control, de builderz-labs, con licencia MIT.
12. **Todo lo del dueño pasa por el panel.** Lo que se le pregunte en cualquier chat va también, al momento, a «Te toca»; ahí contesta Sí / No / «No entiendo».
13. **Preguntas que se entienden solas:** `N. ¿Pregunta corta? Si dices Sí: qué pasa. Si dices No: qué pasa. (#n Módulo) (fotos: carpeta/)`. Sin siglas ni nombres técnicos; para escoger, «A/B: A) … · B) …». Lo ya decidido no se pregunta: se pregunta solo «¿lo publico?».
14. **«No entiendo»** = reescribir la pregunta más sencilla, con otro título, en la siguiente vuelta.
15. **Fotos con su carpeta y subidas a GitHub** (`git add -f`). Sin fotos no se pide un visto bueno.
16. **Latido de todos, siempre (Claude y ChatGPT):** cada vuelta del Coordinador escribe el estado de todos sus chats con su energía (ver `LATIDO.md`). «Sin dato» solo si de verdad no se puede medir.
17. **Tutorial siempre:** toda pantalla nueva trae su paso a paso (como el de Flowz).
18. **Un solo chat de supervisor/planeación a la vez.** Antes de abrir otro, cerrar el viejo y sus tareas programadas: dos chats se pisan y avisan doble.
19. **Lo que se publica solo** (una rama que se sube sola) se trabaja en otra rama y pasa con el Sí del dueño.

## Arrancar un proyecto nuevo
1. El dueño dice qué quiere. 2. Se crea el repositorio. 3. Se escriben instrucciones cortas (`AGENTS.md`). 4. Se arma la hoja de módulos. 5. Planeación recomienda el equipo con `documentos/ARMAR-EQUIPO.md` (el dueño dice qué tiene y elige A/B) y el Coordinador abre a los trabajadores. 6. Bóveda en 1Password (la crea el dueño). 7. Despertador y buzón en el servidor (con la Mac del dueño, una sola vez). 8. Se conecta a Flowz Proyectos. 9. El supervisor revisa cada hora.

## Cómo decide el dueño
El dueño habla con el supervisor, o elige en el panel. Cada respuesta queda en `planeacion/respuestas-arnaldo/AAAA-MM-DD-HHMM.md` con sus palabras. Le toca decidir los diseños, el orden y autorizar lo real. No le tocan los detalles técnicos ni las llaves.

## Señales de alarma → arreglo
| Señal | Arreglo |
|---|---|
| Más de 60 min sin cambios | Ver el último cambio y si alguien espera un clic; despertar al jefe |
| Esperan al dueño | Juntar la pregunta y llevársela en una línea |
| Más revisiones que trabajo nuevo | Una revisión por entrega; mover a módulos en 0 % |
| Se esperan entre sí | El jefe decide quién sigue |
| Repiten lo mismo | Revisar la instrucción que los manda |
| Memoria ≥35 % | Relevo y chat nuevo |
| Pizarrón lleno | Partirlo en piezas |
| Trabajo en algo prohibido | Dejarlo a un solo chat hasta que el dueño lo autorice |

## Cambios del método (lo más nuevo arriba)
- **v2 · 15-nov-2026 tarde** (Flowz y el panel): reglas 12–19. Lecciones: una respuesta dada en un chat no llegó al pizarrón (→ todo por el panel); preguntas con siglas que el dueño no entendió (→ «Si dices Sí / No» y «No entiendo»); fotos que nadie subió (→ carpeta y `git add -f`); un chat de ChatGPT «trabajando» 2 h sin avisar y el panel no lo marcaba (→ latido de todos con energía); dos chats de claude.ai escribiendo a la vez (→ uno solo); un PR viejo que chocaba (→ archivos del método sin tocar la hoja de módulos del Coordinador).
- **v1 · 15-nov-2026 mañana** (LexFree): reglas 1–11.
