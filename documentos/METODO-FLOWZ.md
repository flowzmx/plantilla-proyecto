# Método Flowz

Cómo trabajamos con inteligencia artificial para construir software sin ser programadores. Escrito en palabras de todos los días, y con su historia: cómo era antes y por qué fue cambiando.

## Por qué nació

El Método Flowz nació de **gente con conocimiento casi nulo de programación** que quiso construir su propio sistema con varios chats de IA trabajando al mismo tiempo. La idea era buena, pero en la práctica **no funcionaba bien, era muy estresante y se perdía mucho tiempo**.

Los chats se pisaban el trabajo en la misma carpeta. Se les llenaba la memoria y olvidaban lo que iban haciendo. Cada mensaje de un chat a otro le pedía permiso al dueño, así que se pasaba el día picando «sí» y llevando recados de un chat a otro. Le volvían a preguntar cosas que ya había contestado. Un chat podía quedarse parado horas y nadie se daba cuenta.

Era como tener una oficina llena de gente muy capaz, pero sin jefe, sin pizarrón y sin turnos: todos trabajando, nadie coordinado, y el dueño apagando fuegos todo el día.

El Método Flowz es el orden que fuimos poniendo, regla por regla, cada vez que algo fallaba. Nada se inventó en el escritorio: **cada regla nació de un problema real**.

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
- **Qué pasó:** dos «Supervisores» de LexFree se pisaban, y el viejo seguía haciendo tareas.
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
- **Qué pasó:** lo que se aprendía en Flowz no le servía a LexFree, y al revés.
- **Ahora:** el método vive en un solo lugar (la plantilla) y todos los proyectos lo usan: Planeación, Coordinador y Trabajadores, con el panel para el dueño.

### Antes del método · 7 al 13-nov-2026 · Las primeras reglas
- **Antes:** varios chats en la misma carpeta, sin turnos ni pizarrón.
- **Qué pasó:** se pisaban el trabajo, olvidaban al llenarse de memoria, cada mensaje entre chats le pedía permiso al dueño y un pizarrón enorme hacía que todos chocaran.
- **Ahora:** cada chat en su carpeta (7-nov); cambio de turno antes de llenarse (8-nov); avisos por el pizarrón y no por mensajes (8-nov); un Coordinador que aprueba lo chico (10-nov); el pizarrón en piezas chicas (12-nov); y «que corra solo», sin pedir «sí» más que para gastar o borrar (13-nov).
