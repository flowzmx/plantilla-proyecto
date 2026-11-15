# Encargo 00 · Propuesta inicial de {{nombre}}

Para Planeación (el jefe). Es lo primero que se hace en este proyecto.

## Qué hacer
1. Lee `IDEA.md` completo.
2. Propón el **equipo** siguiendo `documentos/ARMAR-EQUIPO.md` (con quién cuenta, reglas y formato A/B): 1 jefe + de 3 a 5 cuadrillas, cada una con su área. {{dueno}} prefiere **{{equipo}}**; si recomiendas otro tamaño, di por qué en una línea.
3. Propón las **skills** que le servirían a cada cuadrilla (las que ya existan en la IA de cada puesto: jefe **{{ia_jefe}}**, cuadrillas **{{ia_cuadrillas}}**), sin instalar nada.
4. Propón los **primeros módulos**: la tabla de `planeacion/MODULOS.md` con 5 a 12 módulos agrupados en fases, todos en ⬜.
5. Escribe las fichas de cada cuadrilla en `planeacion/chats/` (una por cuadrilla, corta: su área, qué hace primero y sus «No»).
6. Pon la propuesta en «Te toca» de `MODULOS.md` como **opciones A/B, con una recomendada**, para que el dueño elija con un clic en el panel.

## Qué NO hacer
- No construir nada todavía: primero que el dueño apruebe.
- No pedir llaves ni conectar nada real.
- No inventar lo que la idea no dice: si falta algo importante, hazlo **una sola pregunta** en «Te toca».

## Recibo de terminado
Commit con la propuesta, `python3 tools/avance_modulos.py` corrido sin errores y la nota en el pizarrón.
