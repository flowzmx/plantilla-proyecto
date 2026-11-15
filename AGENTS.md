# {{nombre}} · instrucciones para los chats

## Primero
1. Lee [`IDEA.md`](IDEA.md): es lo que pidió {{dueno}}, con sus palabras.
2. Lee [`PIZARRON.md`](PIZARRON.md), que es el vigente, y [`planeacion/MODULOS.md`](planeacion/MODULOS.md).
3. Lee las decisiones del dueño en `planeacion/respuestas-dueno/`, de la más nueva a la más vieja. **Valen como palabra de {{dueno}}.**
4. Toma tu ficha en `planeacion/chats/` y tu encargo en `planeacion/encargos/`.
5. Trabaja en la rama `main`, con commits chicos y un título que diga qué hiciste. Nunca uses `--force`.

## Cómo trabajamos (de [`documentos/MANUAL.md`](documentos/MANUAL.md))
- **Nunca te quedes quieto.** Si algo te espera, toma lo siguiente.
- **Una sola revisión por entrega,** la que asigne el jefe. No acuses recibo ni concilies lo que no es tuyo.
- **Primero la Imagen.** Algo nuevo se le presenta al dueño como A/B, con una recomendada.
- **Una sola pregunta al dueño,** corta, y sigues con otra cosa.
- **Recibo de terminado:** un paso cuenta como hecho solo con la prueba anotada (qué se probó y el resultado).
- **Cambio de turno** al 35–40 % de memoria: dejas una nota de relevo en `planeacion/relevos/`.

## Los NO de verdad
- No crear ni pedir llaves. Las que hagan falta van en el gestor de contraseñas del dueño, y las crea él con una guía.
- Nada de datos personales, textos de conversación ni llaves en el repositorio.
- Nada real (correos, cobros, clientes, borrar) sin permiso del dueño, uno por uno.
- No usar comandos que pidan aprobación (rm, sudo, cambiar permisos).

## Herramientas
- Pizarrón: `python3 tools/publicar_pizarron.py vNNNN borrador.md`, con un máximo de 3,000 caracteres.
- Avance: `python3 tools/avance_modulos.py` genera `planeacion/avance-modulos.json` a partir de `MODULOS.md`.
- Panel: este proyecto se ve en Flowz Proyectos (proyectos.flowz.mx).
