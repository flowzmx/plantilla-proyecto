#!/usr/bin/env python3
"""Avance por módulo: una sola fuente (planeacion/MODULOS.md) → planeacion/avance-modulos.json. Copiado de LexFree.

Lee planeacion/MODULOS.md y escribe el JSON que lee la pantalla /avance
(misma idea que «Nuestros módulos» de Flowz, ejecucion/avance/desde_modulos.py).

- pasos  = Imagen → Construido → Probado → Revisión final → Publicado.
- fases  = secciones «## 1. …», «## 2. …» que tienen la tabla de 5 pasos.
- ✅ hecho · 🔶 a medias · ⬜ falta · — no aplica (cuenta como hecho).
- falta  = «Siguiente paso» (con «Qué falta» como línea) + lo de «Te toca, Arnaldo» que nombra el #.
- hecho  = se conserva la historia del JSON anterior (MODULOS no la lleva).
- resumen.ahora / resumen.despues = secciones «## Ahora» y «## Después» de MODULOS
  (o --ahora / --despues); resumen.te_toca = lista «## Te toca, Arnaldo».
- Si MODULOS dice «Borrador:» arriba, la pantalla lo avisa.

Uso, en cada revisión de Planeación, después de poner al día MODULOS.md:
    python3 tools/avance_modulos.py            # escribe el JSON
    python3 tools/avance_modulos.py --revisar  # solo comprueba
Rutas: LEXFREE_MODULOS (entrada) y LEXFREE_AVANCE_FILE (salida).
"""
import argparse
import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MODULOS = Path(os.environ.get('LEXFREE_MODULOS', RAIZ / 'planeacion' / 'MODULOS.md'))
SALIDA = Path(os.environ.get('LEXFREE_AVANCE_FILE', RAIZ / 'planeacion' / 'avance-modulos.json'))

PASOS = ['Imagen', 'Construido', 'Probado', 'Revisión final', 'Publicado']
COLUMNAS = ['#', 'Módulo', *PASOS, 'Qué falta', 'Siguiente paso']
ESTADOS = (('✅', 'hecho'), ('🔶', 'a medias'), ('⬜', 'falta'))


def slug(texto):
    t = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-') or 'modulo'


def celdas(linea):
    return [c.strip() for c in linea.strip().strip('|').split('|')]


def sin_formato(texto):
    return re.sub(r'\*\*|`', '', texto).strip()


def paso(celda):
    c = celda.strip()
    nota = re.sub(r'^(✅|🔶|⬜|—)\s*', '', c).strip()
    nota = re.sub(r'^\((.*)\)$', r'\1', nota).strip()
    if c.startswith('—'):
        return {'estado': 'hecho', 'nota': ('No aplica: ' + nota) if nota else 'No aplica.'}
    for marca, estado in ESTADOS:
        if c.startswith(marca):
            return {'estado': estado, 'nota': nota} if nota else {'estado': estado}
    raise ValueError(f'paso sin marca (✅ 🔶 ⬜ —): «{celda}»')


def _texto_seccion(lineas, i):
    """Texto corrido debajo de «## X» hasta el siguiente «## »."""
    partes = []
    for t in lineas[i + 1:]:
        if t.startswith('## '):
            break
        if t.strip():
            partes.append(sin_formato(t.strip().lstrip('-* ').strip()))
    return ' '.join(partes)


def leer(md):
    fases, modulos, te_toca, extra = [], [], [], {}
    seccion = None
    lineas = md.split('\n')
    extra['borrador'] = bool(re.search(r'^\*{0,2}Borrador:', md, re.M))
    for i, l in enumerate(lineas):
        m = re.match(r'^## (\d+)\. (.+)$', l)
        if m:
            seccion = {'id': int(m.group(1)), 'nombre': m.group(2).split('(')[0].strip()}
            continue
        if l.startswith('## '):
            seccion = None
            if l.startswith('## Te toca,'):  # «Te toca, Arnaldo» o el nombre del dueño (proyectos de clientes)
                for t in lineas[i + 1:]:
                    if t.startswith('## '):
                        break
                    mt = re.match(r'^\d+\.\s+(.*)$', t)
                    if mt:
                        te_toca.append(sin_formato(mt.group(1)))
            elif re.match(r'^## Ahora\b', l):
                extra['ahora'] = _texto_seccion(lineas, i)
            elif re.match(r'^## Despu[eé]s\b', l):
                extra['despues'] = _texto_seccion(lineas, i)
            continue
        if seccion and l.startswith('|'):
            c = celdas(l)
            if c[0] == '#':
                if c != COLUMNAS and 'Imagen' not in c:
                    seccion = None  # otra tabla (p. ej. «Al final» de Flowz): no son módulos de 5 pasos
                    continue
                if c != COLUMNAS:
                    raise ValueError(f'columnas distintas en «{seccion["nombre"]}»: {c}')
                if seccion not in fases:
                    fases.append(seccion)
                continue
            if set(c[0]) <= set('-:') or len(c) != len(COLUMNAS):
                continue
            num, nombre = c[0], sin_formato(c[1])
            modulos.append({
                'num': num, 'id': slug(nombre), 'nombre': nombre, 'fase': seccion['id'],
                'pasos': [paso(x) for x in c[2:7]],
                'que_falta': sin_formato(c[7]), 'siguiente': sin_formato(c[8]),
            })
    if not modulos:
        raise ValueError('no encontré tablas de módulos en MODULOS.md')
    vistos = set()
    for m in modulos:
        if m['num'] in vistos:
            raise ValueError(f'número repetido en MODULOS.md: #{m["num"]}')
        vistos.add(m['num'])
    return fases, modulos, te_toca, extra


def total(modulos):
    """Hecho = 1, a medias = ½, entre los pasos, ×100 redondeado; promedio redondeado (igual que la pantalla)."""
    vals = []
    for m in modulos:
        p = m.get('pasos') or []
        if p:
            vals.append(round(100 * sum(1 if x.get('estado') == 'hecho' else 0.5 if x.get('estado') == 'a medias' else 0 for x in p) / len(p)))
    return round(sum(vals) / len(vals)) if vals else 0


def historial(anterior, modulos, hoy):
    """Un renglón por día (UTC, el último valor del día), máximo 90 días."""
    h = [x for x in (anterior.get('historial') or []) if x.get('fecha') != hoy]
    h.append({'fecha': hoy, 'total': total(modulos), 'modulos': len(modulos)})
    return sorted(h, key=lambda x: x['fecha'])[-90:]


def armar(md, anterior, ahora=None, despues=None, ahora_utc=None):
    ahora_utc = ahora_utc or datetime.now(timezone.utc)
    fases, modulos, te_toca, extra = leer(md)
    viejo = {m.get('id'): m for m in anterior.get('modulos', [])}
    salida = []
    for m in modulos:
        falta = []
        if m['siguiente'] and m['siguiente'] != '—':
            quien = 'Arnaldo' if re.match(r'^Arnaldo\b', m['siguiente']) else 'Equipo'
            falta.append({'que': m['siguiente'], 'quien': quien, 'linea': m['que_falta']})
        for t in te_toca:
            if re.search(rf'#{re.escape(m["num"])}(?![0-9a-z])', t):
                falta.append({'que': t, 'quien': 'Arnaldo', 'linea': 'Te toca, Arnaldo (planeacion/MODULOS.md)'})
        salida.append({'id': m['id'], 'nombre': m['nombre'], 'fase': m['fase'], 'pasos': m['pasos'],
                       'hecho': viejo.get(m['id'], {}).get('hecho', []), 'falta': falta})
    resumen = dict(anterior.get('resumen') or {})
    for clave, valor in (('ahora', ahora or extra.get('ahora')), ('despues', despues or extra.get('despues'))):
        if valor:
            resumen[clave] = valor
    resumen['te_toca'] = ' · '.join(f'{i}. {t}' for i, t in enumerate(te_toca, 1))
    return {
        'como_actualizar': 'Sale de planeacion/MODULOS.md (una sola fuente). En cada revisión: poner al día '
                           'MODULOS.md y correr python3 tools/avance_modulos.py.',
        'actualizado': ahora_utc.strftime('%Y-%m-%dT%H:%MZ'),
        'fuente': 'planeacion/MODULOS.md',
        'borrador': extra['borrador'],
        'pasos': PASOS,
        'fases': fases,
        'resumen': resumen,
        'modulos': salida,
        'historial': historial(anterior, salida, ahora_utc.strftime('%Y-%m-%d')),
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--ahora', help='línea «Ahora» (si no, sale de «## Ahora» de MODULOS)')
    ap.add_argument('--despues', help='línea «Después» (si no, sale de «## Después» de MODULOS)')
    ap.add_argument('--revisar', action='store_true', help='solo comprueba, no escribe')
    a = ap.parse_args(argv)
    try:
        anterior = json.loads(SALIDA.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        anterior = {}
    try:
        datos = armar(MODULOS.read_text(encoding='utf-8'), anterior, a.ahora, a.despues)
    except (OSError, ValueError) as e:
        print(f'MODULOS.md no se pudo leer; el JSON no se tocó: {e}', file=sys.stderr)
        return 1
    texto = json.dumps(datos, ensure_ascii=False, indent=2) + '\n'
    if not a.revisar:
        SALIDA.parent.mkdir(parents=True, exist_ok=True)
        tmp = SALIDA.with_suffix(f'.json.{os.getpid()}.tmp')
        tmp.write_text(texto, encoding='utf-8')
        tmp.replace(SALIDA)
    print(f'ok: {len(datos["modulos"])} módulos, {len(datos["fases"])} fases, total {total(datos["modulos"])} %, '
          f'{sum(len(m["falta"]) for m in datos["modulos"])} pendientes'
          + (' (solo revisado)' if a.revisar else f' → {SALIDA}'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
