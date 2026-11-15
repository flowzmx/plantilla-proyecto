# Cómo trabajamos con IAs · Manual de Arnaldo

Versión en el repositorio del documento https://claude.ai/artifact/FCSd5JvozCBjj93g5Acss2, escrito por Claude el 15-nov-2026 con el método que se probó ese día en LexFree.

## Para qué sirve
Hace que varias IAs trabajen solas y sin pararse en un proyecto. El dueño solo toma las decisiones de dueño. Funciona con cualquier IA (ChatGPT/Codex, Claude o la que siga).

## La obra
El proyecto funciona como una obra. **Dueño** (decide) → **Supervisor** externo (vigila cada hora y escribe las respuestas del dueño) → **Repositorio y pizarrón** (todo queda guardado) ↔ **Jefe** (Planeación, reparte) → **Cuadrillas** (construyen en un taller aparte) → **Buzón con guardia** (revisa, respalda e instala) → **Página real**. Un **Despertador** levanta a cada chat solo con lo suyo, y la **Torre de control** (este proyecto) se lo muestra al dueño.

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
10. Cambio de turno al 35–40 % de memoria.
11. Recibo de terminado: sin prueba anotada no está hecho. La idea viene de Mission Control, de builderz-labs, con licencia MIT.

## Arrancar un proyecto nuevo
1. El dueño dice qué quiere. 2. Se crea el repositorio. 3. Se escriben instrucciones cortas (`AGENTS.md`). 4. Se arma la hoja de módulos. 5. El jefe recomienda el equipo con `documentos/ARMAR-EQUIPO.md` (el dueño dice qué tiene y elige A/B) y se abren las cuadrillas. 6. Bóveda en 1Password (la crea el dueño). 7. Despertador y buzón en el servidor (con la Mac del dueño, una sola vez). 8. Se conecta a Flowz Proyectos. 9. El supervisor revisa cada hora.

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
