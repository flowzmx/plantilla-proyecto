# Varios proyectos en un servidor, sin choques

El servidor es un **edificio de departamentos**: todos comparten la entrada y cada proyecto tiene su departamento con llave propia. Léelo antes de instalar algo.

## Cómo se habla con cada proyecto
- El dueño habla con **un chat por proyecto**. Ese chat es el **jefe del proyecto** (Planeación): piensa, diseña y le explica al dueño.
- Adentro, el **Coordinador** (siempre Claude Code, en el servidor) reparte el trabajo entre **muchos trabajadores**, que pueden ser Claude o ChatGPT/Codex. Los lanza el lanzador cada 5 min: cada uno hace una pieza, deja su recibo y se va.
- Más trabajadores no le dan más trabajo al dueño: él solo contesta Sí o No en el panel.

## El conserje
- Hay **un solo conserje** por servidor: un chat Claude Code con su hoja de **Servidor**. Es el único que toca lo compartido: la recepción (proxy), Docker, tareas programadas, respaldos y la lista de vecinos.
- Los Coordinadores **le piden** lo compartido con un pedido en su pizarrón. Nunca lo hacen ellos.
- Lo que cambie la recepción o reinicie algo compartido lleva **permiso escrito del dueño** en el chat del conserje.

## Las 7 reglas del edificio
1. **Un departamento por proyecto:** su carpeta (`/opt/<proyecto>`) y su usuario del servidor, que solo entra a la suya.
2. **Un bloque de puertos por proyecto**, por ejemplo de 100 en 100 (8000–8099, 8100–8199…). Antes de usar un puerto, se busca en la lista de vecinos. Nadie usa un puerto fuera de su bloque.
3. **Una caja aislada por proyecto** (contenedor o servicio propio), con **su propia base de datos** y su red. Nunca se comparte una base entre proyectos.
4. **Una sola recepción:** cada dominio apunta a su proyecto desde el proxy. Solo el conserje la edita.
5. **Sus propias llaves:** una bóveda por proyecto en el gestor de contraseñas. Ningún proyecto lee las llaves de otro.
6. **Su tope de consumo:** límite de memoria y procesador por proyecto, para que uno no tumbe a los demás.
7. **Su propio pizarrón y su latido:** un repositorio, un Coordinador y una rama de latidos por proyecto. El panel los junta en una sola vista.

## La lista de vecinos
`/opt/vecinos.md`, solo la escribe el conserje. Un renglón por proyecto: nombre, carpeta, usuario, bloque de puertos, dominios, base de datos, bóveda de llaves y tope de consumo.

## Cuándo crecer
Un servidor mediano aguanta de 5 a 15 proyectos según su peso, no miles. Cuando la memoria o el procesador pasan del 70 % por varios días, se abre **otro edificio** (otro servidor) con las mismas reglas y su propio conserje. Los proyectos de clientes van siempre con su propia base, aunque haya que crecer en servidores.

## Proyecto nuevo, en orden
1. Planeación pide al conserje un departamento.
2. El conserje lo anota en la lista de vecinos, crea la carpeta y el usuario, y le asigna puertos y tope.
3. El dueño crea la bóveda de llaves.
4. El Coordinador del proyecto arranca dentro de su departamento.
