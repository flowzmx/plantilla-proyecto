# Cambios del método Flowz

Cada lección nueva se anota aquí (lo más nuevo arriba): qué pasó y qué regla salió. Al cambiar algo, sube `METODO-VERSION`.

- **v3.5 · 15-nov-2026 18:3x** (Arnaldo: «¿qué falta para que quede bien, la versión sencilla?»): **una hoja de una página por puesto** (`documentos/hojas/`); cada chat lee solo la suya al empezar y las reglas largas quedan de consulta. Menos lectura = menos errores y menos memoria.
- **v3.4 · 15-nov-2026 18:2x** (el servidor veía una cuenta de Codex con crédito pero sin nombre): cada cuenta en su propia carpeta con etiqueta `cuenta.txt`; sin etiqueta = «sin nombre» y se pregunta.
- **v3.3 · 15-nov-2026 18:1x** (Arnaldo: «saber quién está conectado, cuánto le queda, cómo rotamos»): cuentas de IA del equipo y su crédito en el latido; panel › Ajustes (`planeacion/ajustes.json`) con cambio de turno, aviso de crédito y «Trabaja / De respaldo»; «Mover chats» a otra cuenta antes de quedarse sin crédito.
- **v3.2 · 15-nov-2026 17:3x** (LexFree y el panel; Arnaldo: «para que no choquemos»): dos chats de claude.ai con el mismo nombre «Supervisor» se pisaban el latido y el viejo seguía con sus tareas programadas (→ nombre con número en cada turno, el nuevo marca al viejo «relevado», el viejo apaga sus tareas, aviso rojo de choque). Los chats de claude.ai no tienen medidor (→ horas y vueltas; cambio a las 6 h o 40 vueltas). Los de ChatGPT se cansaban sin relevo (→ cambio automático en el servidor; a mano con «Cambiar ›» y las palabras exactas cuando no se puede).
- **v3.1 · 15-nov-2026 16:5x**: el latido lleva `modelo` (Arnaldo: «el modelo Claude Opus más visible»); el panel lo enseña en su columna.
- **v3 · 15-nov-2026 16:4x** (Arnaldo: «lo que sea más sano… varios md… así fue el pizarrón, lo versionamos»): el método se parte en piezas chicas: `MANUAL.md` corto para todos + `documentos/reglas/` por tema. Límites: MANUAL ≤ 4,000 letras; cada pieza ≤ 3,000.
- **v2.1 · 15-nov-2026 16:4x**: cada pregunta trae **Contexto** y **Te recomiendo** (como en el chat con Claude), muy específica; el panel marca la recomendada con ★.
- **v2 · 15-nov-2026 tarde** (Flowz y el panel): reglas 12–19. Lecciones: una respuesta dada en un chat no llegó al pizarrón (→ todo por el panel); preguntas con siglas que el dueño no entendió (→ «Si dices Sí / No» y «No entiendo»); fotos que nadie subió (→ carpeta y `git add -f`); un chat de ChatGPT «trabajando» 2 h sin avisar y el panel no lo marcaba (→ latido de todos con energía); dos chats de claude.ai escribiendo a la vez (→ uno solo); un PR viejo que chocaba (→ archivos del método sin tocar la hoja de módulos del Coordinador).
- **v1 · 15-nov-2026 mañana** (LexFree): reglas 1–11.

