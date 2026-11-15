# Armar el equipo · instrucciones para cualquier IA

Para la IA que hace de jefe (Claude, ChatGPT/Codex o la que sea). El dueño te dice **lo que tiene** y tú le recomiendas **cómo organizarse**. Él solo aprueba.

## Cómo te lo va a pedir
> Lee documentos/ARMAR-EQUIPO.md. Tengo: 10 programadores (3 con experiencia), 4 cuentas de Codex y una de Claude. Proyectos: LexFree y Flowz. ¿Cómo le hacemos?

## 1. Junta los datos (sin preguntar lo que ya está escrito)
- **Personas:** cuántas, quiénes tienen experiencia y cuántas horas al día tiene cada una.
- **IAs:** cuántas cuentas hay de cada una. Varios chats en una cuenta comparten sus créditos.
- **Trabajo:** lee `planeacion/MODULOS.md` de cada proyecto. Cuenta los módulos que nadie tiene y los que esperan al dueño.
- **Cómo va hoy:** en el historial de commits, cuenta el trabajo nuevo y las revisiones de la última semana.
- Si falta algo que cambia la recomendación, hazle **una sola pregunta**, corta. Si no, asume lo razonable y dilo.

## 2. Decide con estas reglas
1. **Un módulo por persona.** Si hay menos módulos listos que personas, no metas a más gente: primero se preparan módulos.
2. **Un encargado por cada 4 o 5.** Con más de 6 personas: un jefe general y encargados por proyecto o por área.
3. **Cada persona con su IA** (persona + IA = una pareja). Si las cuentas no alcanzan, di cuántas parejas caben sin quedarse sin créditos.
4. **«Libre»** solo para quien el dueño ya conoce. Los nuevos, **«Con revisión»**, que hace su encargado **una sola vez**.
5. **Arranque por etapas:** empieza con la mitad o menos. Crece cuando las revisiones sean menos que el trabajo nuevo.
6. **El jefe puede ser cualquier IA.** Recomienda la que más créditos tenga ese día.
7. **El dueño no es el cuello de botella:** sus preguntas van juntas y en A/B.

## 3. Entrega la recomendación
Escríbela en `planeacion/equipo/PROPUESTA-AAAA-MM-DD.md`:
- **Opción A (recomendada) y opción B**, cada una en 3 líneas: cómo queda y por qué.
- **Tabla** con persona o pareja, IA, puesto (jefe, encargado o cuadrilla), proyecto o área, primer módulo y si va «Libre» o «Con revisión».
- **Etapas:** quién entra la semana 1, quién la 2 y qué se mide para decidir.
- **Lo que no alcanza:** cuentas, módulos sin preparar o permisos que faltan.

Luego pon en «Te toca» de `MODULOS.md` una línea: «Elegir A o B del equipo (planeacion/equipo/PROPUESTA-…)».

## Lo que NO haces
- No invitas a nadie ni cambias permisos: eso lo hace el dueño desde el panel (pestaña Equipo) cuando apruebe.
- No pides llaves ni datos personales. A las personas se les nombra por su usuario de GitHub o como «Programador 1, 2…».
