# Preguntas al dueño (Te toca)

El dueño contesta **en el panel** (Flowz Proyectos › Te toca) con **Sí / No / «No entiendo»**. Todo lo que se le pregunte en cualquier chat va también, **al momento**, a la sección `## Te toca, <Dueño>` de `MODULOS.md`.

## Formato (un renglón por pregunta)
`N. ¿Pregunta corta y específica? Contexto: qué es y por qué se pregunta (nombres y números reales). Si dices Sí: qué pasa. Si dices No: qué pasa. Te recomiendo: Sí/No/A/B, porque … (#n Módulo) (fotos: carpeta/ o carpeta/prefijo-*)`
- Para escoger entre dos: «A/B: A) … · B) …» y «Te recomiendo: A, porque …». El panel marca la recomendada con ★.
- Palabras del dueño, sin siglas ni nombres técnicos (nada de PR, DNS, repo, Caddy): se dice con lo que él ve.
- Lo ya decidido **no se pregunta**; solo «¿lo publico?».
- Una pregunta por tema. Nunca preguntar lo que ya está en sus respuestas.

## Fotos
En su carpeta y **subidas a GitHub** (`git add -f`). Sin fotos no se pide un visto bueno: el panel avisa en rojo.

## Sus respuestas
Llegan a `planeacion/respuestas-*/AAAA-MM-DD-HHMM.md` (commit «Decisión del dueño: …»). Se leen en cada vuelta y se actúa; lo contestado sale de «Te toca». **«No entiendo»** = reescribir la pregunta más sencilla, con otro título, en la siguiente vuelta.

## Buzón de Planeación (cuando no puede escribir en el proyecto)
Si el dueño contesta en un chat de **claude.ai** y Planeación no puede escribir en el repositorio del proyecto, deja la respuesta en **`flowzmx/flowz-proyectos` › `planeacion/buzon/<proyecto>/AAAA-MM-DD-HHMM-<tema>.md`** (`<proyecto>` = el `slug` de `proyectos.json`, p. ej. `proyecto-a`, `proyecto-b`…). El Coordinador lo lee **en cada vuelta** (en el servidor: `/opt/flowz-proyectos/app/planeacion/buzon/<proyecto>/`, que se actualiza solo cada 5 min; si no, `git pull` de flowz-proyectos), copia lo nuevo a sus `respuestas-*`, actúa y anota «leído» en la bitácora. Así el dueño **nunca copia y pega** recados.
