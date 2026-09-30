#!/usr/bin/env python3
"""AudioForge CLI — limpia y masteriza audio.

Ejemplo:
  python cli.py --in bruto.wav --out pro.wav --target podcast
"""
import argparse
import json
import sys

from audioforge import procesar, __version__
from audioforge.analyze import OBJETIVOS


def main():
    ap = argparse.ArgumentParser(description=f"AudioForge v{__version__} — DataFlow Elegance")
    ap.add_argument("--in", dest="entrada", required=True, help="Audio de entrada (wav/flac/...)")
    ap.add_argument("--out", dest="salida", required=True, help="Audio de salida")
    ap.add_argument("--target", default="podcast", help="Objetivo LUFS: " + ", ".join(OBJETIVOS) + " o un número")
    ap.add_argument("--no-denoise", action="store_true", help="No reducir ruido")
    ap.add_argument("--noise", type=float, default=0.85, help="Cantidad de reducción de ruido [0-1]")
    args = ap.parse_args()

    try:
        report = procesar(args.entrada, args.salida, objetivo=args.target,
                          denoise=not args.no_denoise, cantidad_ruido=args.noise)
    except Exception as e:  # noqa: BLE001
        print(f"[error] {e}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
