"""Publica una revisión del pizarrón de Flowz Proyectos (copiado de LexFree)."""
import argparse
import fcntl
import os
from pathlib import Path
import re
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]


def publicar(root, base, borrador):
    tablero = root / 'PIZARRON.md'
    versiones = root / 'pizarron/versiones'
    contenido = borrador.read_text(encoding='utf-8').strip()
    cuerpo = re.sub(r'^# .*Pizarrón v[0-9]+\s*', '', contenido).strip()
    if not cuerpo or len(cuerpo) > 3000:
        raise SystemExit('El cuerpo debe contener entre 1 y 3.000 caracteres.')
    with (versiones.parent / '.publicacion.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        actual = tablero.readlink().stem
        if actual != base:
            raise SystemExit(f'La versión vigente es {actual}. Relee y concilia los cambios.')
        numero = int(actual[1:]) + 1
        while (versiones / f'v{numero:04}.md').exists():
            numero += 1
        version = f'v{numero:04}'
        destino = versiones / f'{version}.md'
        with TemporaryDirectory(dir=versiones.parent) as temporal:
            copia = Path(temporal) / 'contenido'
            copia.write_text(f'# Flowz Proyectos · Pizarrón {version}\n\n{cuerpo}\n', encoding='utf-8')
            os.link(copia, destino)
            enlace = Path(temporal) / 'vigente'
            enlace.symlink_to(destino.relative_to(root))
            enlace.replace(tablero)
        return version


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('base', help='Versión leída antes de preparar los cambios')
    parser.add_argument('borrador', type=Path)
    args = parser.parse_args()
    print(publicar(ROOT, args.base, args.borrador))
