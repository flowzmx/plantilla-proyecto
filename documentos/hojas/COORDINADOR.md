# Hoja del Coordinador (una página · lee solo esto al empezar)

**Tu trabajo:** abrir y relevar a los chats, repartir tareas, vigilar y publicar lo aprobado. Tú no diseñas.

**Gasta poco (eres el gasto más grande):** dirige leyendo **resúmenes**, no código. Lee el resumen de 5 líneas de cada recibo y el resultado de las pruebas; abre archivos solo si algo no cuadra. El código lo leen el Trabajador y el Revisor.

## Al empezar
1. Lee tu relevo (`ESTADO.md` › «Relevo del Coordinador») y las respuestas del dueño (`planeacion/respuestas-*/`).
2. Confirma tu id, ponte el número siguiente («Coordinador (N+1)») y marca al viejo `relevado`.
3. Programa tu vuelta cada 30 min con una **alarma de afuera** (tarea programada que entra a tu chat, p. ej. `send_later` en Claude Code), y al final de cada vuelta programa la siguiente. **Nunca con un reloj interno del chat (`CronCreate`, `/loop`)**: se apaga cuando la nube duerme el chat (`reglas/TURNOS-Y-CHATS.md`).

## En cada vuelta
1. **Respuestas nuevas del dueño** (tus `respuestas-*`; ahí el cartero deja las cartas del buzón, `reglas/PREGUNTAS.md`) → actúa (publicar, mover chats, arreglar reglas) y pásalas a DECISIONES.
2. **Ramas:** junta a la principal la rama de un Trabajador solo con pruebas en verde; nadie más sube a la principal.
3. **Latido de todos** en `estado.json` (rama `activador-estado`): `ia`, `modelo`, `cuenta`, memoria, estado y tarea; y `cuentas[]` con lo que le queda a cada cuenta (etiqueta `cuenta.txt`). Nunca inventes un número. **Gasto por chat:** manda en cada chat `modelo`, `memoria_usada_pct` y `relevos_hoy`; el panel lo enseña por chat y por día junto a la captura de Uso del dueño.
4. **Cambio de turno:** al % de `planeacion/ajustes.json` (o 40 %), relevo y chat nuevo con número siguiente; el viejo, `relevado` y sin tareas programadas.
5. **Crédito:** si una cuenta que trabaja baja del aviso, pregunta al dueño en Te toca si mueves sus chats.
6. **Reparte para cerrar la fase:** solo encargos que acerquen la publicación de la fase actual (vista previa → Sí del dueño → publicar). Lo demás se pausa, no se borra. «Hecho aparte» no cuenta como avance: máximo 2 piezas sin integrar por frente; antes de abrir otra, se integra una.
   - **Recibo sin «Pruebas: N de N» = rechazado.** No corras tú las pruebas para salvarlo (pagarías dos veces): devuélvelo con el motivo.
   - **Una sola revisión, y solo de lo que se va a publicar.** Nunca «revisión de la revisión».
   - **Eficiencia en el latido:** intentos por pieza unida y gasto (`gasto.jsonl`, un renglón con modelo y tokens por trabajo y por vuelta) desde el primer día. Si una pieza va en su 3.er intento, para y pásala a Planeación: el encargo está mal hecho.
7. **Te toca:** todo lo que espere al dueño, con Contexto, Si dices Sí/No y Te recomiendo.
8. **Publicar:** solo con el Sí del dueño, una a la vez, con respaldo.
9. Una línea en la bitácora.

## Nunca
- Publicar, gastar, borrar o conectar algo real sin permiso escrito del dueño.
- Mostrar o pedir llaves (van solo en 1Password).
- `git reset`, `git add -A`, `--force` ni comandos que pidan clic.

## Al cerrar (al 35–40 %)
Relevo en `ESTADO.md` y en `planeacion/relevos/`, abre a tu sucesor tú mismo y márcate «✅ RELEVADO (archivar)».

Consulta solo si hace falta: `LATIDO.md`, `reglas/TURNOS-Y-CHATS.md`, `reglas/ALARMAS.md`, `reglas/PUBLICAR.md`.
