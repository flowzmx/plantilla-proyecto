# Método Flowz

Cómo trabajamos con inteligencia artificial para construir software sin ser programadores. Escrito en palabras de todos los días, y con su historia: cómo era antes y por qué fue cambiando.

## Por qué nació

El Método Flowz nació de **gente con conocimiento casi nulo de programación** que quiso construir su propio sistema con varios chats de IA trabajando al mismo tiempo. La idea era buena, pero en la práctica **no funcionaba bien, era muy estresante y se perdía mucho tiempo**.

Los chats se pisaban el trabajo en la misma carpeta. Se les llenaba la memoria y olvidaban lo que iban haciendo. Cada mensaje de un chat a otro le pedía permiso al dueño, así que se pasaba el día picando «sí» y llevando recados de un chat a otro. Le volvían a preguntar cosas que ya había contestado. Un chat podía quedarse parado horas y nadie se daba cuenta.

Era como tener una oficina llena de gente muy capaz, pero sin jefe, sin pizarrón y sin turnos: todos trabajando, nadie coordinado, y el dueño apagando fuegos todo el día.

El Método Flowz es el orden que fuimos poniendo, regla por regla, cada vez que algo fallaba. Nada se inventó en el escritorio: **cada regla nació de un problema real**.

**Al principio el objetivo era solo coordinar.** Todos los chats usaban el modelo de IA más potente (y más caro), y la verdad funcionaba muy bien. Pero la cuenta llegaba a su límite antes de terminar la semana y el trabajo se paraba. Así que el método sumó un segundo objetivo que no estaba en el plan: **gastar menos sin trabajar peor**, usando para cada trabajo el modelo justo, como en una obra donde no pones al arquitecto a cargar ladrillos.

## Para qué sirve

- Para que **una persona que no programa** pueda construir y mantener su propio sistema con varios chats de IA a la vez, sin volverse loca.
- Para que **varias personas**, cada una con su propia cuenta de IA, trabajen en el mismo proyecto sin pisarse.
- Para que el dueño **solo decida** (Sí / No) y no lleve recados.
- Para que el trabajo **no se pare**: si un chat se cansa, se cae o se le acaba el crédito, otro sigue donde se quedó.
- Para **gastar lo menos posible**: el modelo caro piensa y revisa; los baratos construyen.

## Cómo funciona hoy

- **El dueño decide.** No programa ni lleva recados: contesta Sí o No en su panel (proyectos.flowz.mx), con fotos, contexto y una recomendación.
- **Planeación piensa.** Un chat que diseña: hace las imágenes de cómo se va a ver cada pantalla (opción A o B), escribe los encargos y le pregunta al dueño lo que solo él sabe.
- **El Coordinador reparte.** Como un jefe de obra: abre a los trabajadores, le da a cada uno su pieza, vigila que nadie se pare y publica lo terminado.
- **Los Trabajadores construyen.** Cada uno un módulo, solo en su carpeta. Entregan con prueba: qué probaron y qué salió.
- **El pizarrón es GitHub.** Todo queda escrito ahí: decisiones, encargos, avances. El panel lo lee y se lo enseña al dueño. Si no está escrito, no pasó.

## Un día normal

1. El dueño abre su panel y ve en una frase si todo va bien.
2. En «Te toca» contesta lo que espera su respuesta. Su respuesta se guarda y despierta a quien la esperaba.
3. Planeación convierte lo aprobado en encargos; el Coordinador se los reparte a los trabajadores.
4. Cada trabajador construye su pieza, la prueba y deja su recibo.
5. El Coordinador revisa una sola vez, publica y avisa.
6. Cuando un chat se cansa, deja su nota de relevo y entra uno nuevo que sigue donde se quedó.

## Cómo ha cambiado

### v3.11 · 16-nov-2026 · Más general, sin nombres
- **Antes:** la historia del método nombraba personas y proyectos.
- **Qué pasó:** este método es público y sirve para cualquier proyecto; los nombres no ayudaban a entenderlo y podían comprometer a quien lo usa.
- **Ahora:** se habla de para qué sirve y cómo se usa, sin nombres. Y la historia cuenta que, además de coordinar, el método se volvió una forma de **gastar menos**.

### v3.10 · 16-nov-2026 · Un solo buzón y lista para gente nueva
- **Antes:** cuando el dueño contestaba en claude.ai, la respuesta quedaba donde el Coordinador no la alcanzaba a leer, y el dueño tenía que copiar y pegar recados. Las reglas se habían ido alargando.
- **Qué pasó:** el 16-nov el Coordinador de un proyecto no encontró dos respuestas del dueño y hubo que pegárselas a mano. Y el dueño quiere la prueba más importante: que otra persona se conecte con su propia cuenta y trabaje coordinada.
- **Ahora:** las respuestas que no se pueden escribir en el proyecto van a un **buzón** que el Coordinador lee en cada vuelta: el dueño nunca copia recados. Hay una **guía de una página para entrar al equipo**. Y las reglas de turnos quedaron más cortas, sin perder ninguna.

### v3.9 · 16-nov-2026 · Despertador de afuera
- **Antes:** el Coordinador ponía su revisión cada 30 minutos con un reloj que vive dentro de su propio chat.
- **Qué pasó:** de madrugada la nube «durmió» el chat del Coordinador de un proyecto, su reloj se apagó con él y nadie revisó nada por más de 4 horas. Planeación, que usaba una alarma de afuera, sí siguió despierta toda la noche.
- **Ahora:** todos los chats usan una alarma de afuera, como pedirle a alguien que te llame a una hora: aunque el chat se duerma, la llamada llega. Y el vigía del plan B, en el servidor, avisa si aun así alguien se queda callado.

### v3.8 · 16-nov-2026 · Qué modelo usa cada puesto
- **Antes:** casi todos los chats usaban el modelo más caro (Opus) para todo, y el método no decía cuál usar ni con qué intensidad.
- **Qué pasó:** en el proyecto de prueba se hizo la misma pieza con Opus, Sonnet y Haiku. Construir con los baratos salió bien (8 y 8.5 de 10), pero revisar con Opus cuesta más que construir: el ahorro real es de 2 a 3 veces, no de 40. Y un Haiku hizo trampa para pasar su prueba.
- **Ahora:** una tabla dice qué modelo e intensidad usa cada puesto (`documentos/reglas/MODELOS.md`): Opus piensa y revisa, Sonnet construye pantallas, Haiku hace cosas chicas. Quien construye nunca se califica. (v3.7, banda y despertador, sigue en prueba aparte.)

### v3.7 · 16-nov-2026 · En prueba: banda y despertador
- **Antes:** los chats en la nube solo despertaban en la vuelta del Coordinador, y algunos no podían subir su trabajo a la rama principal.
- **Qué pasó:** el dueño aprobó un diseño y el trabajador se enteró 31 minutos después. El panel no veía el trabajo del Coordinador porque se quedaba en su rama.
- **Ahora:** en el proyecto de prueba, una «banda» junta sola cada rama a la principal, y un despertador de tres alarmas avisa al chat en minutos. Meta: 15 minutos o menos.

### v3.6 · 15-nov-2026 · Archivar sin perder nada
- **Antes:** los chats viejos se quedaban abiertos para siempre, por si acaso.
- **Qué pasó:** se juntaban muchos chats relevados y era difícil saber cuál era el bueno.
- **Ahora:** un chat viejo se archiva (nunca se borra) solo cuando su sucesor ya aceptó, su nota de relevo está guardada y pasaron 2 horas sin problemas. El activo nunca se toca.

### v3.5 · 15-nov-2026 · Una hoja por puesto
- **Antes:** cada chat leía todas las reglas al empezar.
- **Qué pasó:** mucha lectura gastaba memoria y causaba errores.
- **Ahora:** cada puesto tiene una hoja de una página. Lo largo queda de consulta.

### v3.4 · 15-nov-2026 · Cada cuenta con su nombre
- **Antes:** el servidor veía cuentas de IA con crédito, pero no sabía de quién eran.
- **Qué pasó:** salía una cuenta «sin nombre» y nadie sabía a quién preguntarle.
- **Ahora:** cada cuenta lleva su etiqueta con el nombre de su dueño.

### v3.3 · 15-nov-2026 · Cuentas y crédito a la vista
- **Antes:** no se sabía cuánto le quedaba a cada cuenta de IA hasta que se acababa.
- **Qué pasó:** el dueño quería saber quién estaba conectado, cuánto le quedaba y cómo rotar.
- **Ahora:** el panel enseña cada cuenta y su crédito, avisa cuando queda poco y deja mover chats a otra cuenta.

### v3.2 · 15-nov-2026 · Turnos sin choques
- **Antes:** dos chats con el mismo nombre podían trabajar a la vez sin saberlo.
- **Qué pasó:** dos «Supervisores» del mismo proyecto se pisaban, y el viejo seguía haciendo tareas.
- **Ahora:** cada turno lleva su número, el nuevo marca al viejo como relevado y el panel avisa en rojo si dos chats van a lo mismo.

### v3.1 y v3 · 15-nov-2026 · El método en piezas chicas
- **Antes:** un solo manual largo.
- **Qué pasó:** era difícil de leer y de mantener al día.
- **Ahora:** un manual corto y reglas por tema, cada una de una página. El panel enseña qué IA y qué modelo usa cada chat.

### v2 y v2.1 · 15-nov-2026 · Todo pasa por el panel
- **Antes:** el dueño contestaba en distintos chats, y las preguntas venían con siglas.
- **Qué pasó:** una respuesta dada en un chat nunca llegó al pizarrón, y hubo preguntas que nadie entendió.
- **Ahora:** todo se contesta en el panel. Cada pregunta trae contexto, qué pasa si dices Sí o No, una recomendación con estrella y el botón «No entiendo».

### v1 · 15-nov-2026 · Nace el Método Flowz
- **Antes:** cada proyecto tenía sus propias reglas, escritas a la carrera.
- **Qué pasó:** lo que se aprendía en un proyecto no le servía al otro, y al revés.
- **Ahora:** el método vive en un solo lugar (la plantilla) y todos los proyectos lo usan: Planeación, Coordinador y Trabajadores, con el panel para el dueño.

### Antes del método · 7 al 13-nov-2026 · Las primeras reglas
- **Antes:** varios chats en la misma carpeta, sin turnos ni pizarrón.
- **Qué pasó:** se pisaban el trabajo, olvidaban al llenarse de memoria, cada mensaje entre chats le pedía permiso al dueño y un pizarrón enorme hacía que todos chocaran.
- **Ahora:** cada chat en su carpeta (7-nov); cambio de turno antes de llenarse (8-nov); avisos por el pizarrón y no por mensajes (8-nov); un Coordinador que aprueba lo chico (10-nov); el pizarrón en piezas chicas (12-nov); y «que corra solo», sin pedir «sí» más que para gastar o borrar (13-nov).
