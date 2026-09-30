"""Masterización básica: normaliza a un objetivo LUFS y limita el pico real."""
from __future__ import annotations

import numpy as np

from .analyze import OBJETIVOS


def _true_peak_limit(data, techo_db=-1.0):
    """Limita el pico para no pasar de `techo_db` dBTP (aprox., por muestra)."""
    techo = 10.0 ** (techo_db / 20.0)
    pico = float(np.max(np.abs(data))) if data.size else 0.0
    if pico > techo and pico > 0:
        data = data * (techo / pico)
    return data


def masterizar(data, sr, objetivo="podcast", techo_db=-1.0):
    """Normaliza la sonoridad al objetivo (nombre de OBJETIVOS o LUFS numérico)
    y aplica un limitador de pico. Devuelve el audio masterizado."""
    import pyloudnorm as pyln

    target = OBJETIVOS.get(objetivo, objetivo)
    target = float(target)

    meter = pyln.Meter(sr)
    loudness = meter.integrated_loudness(data)
    normalizado = pyln.normalize.loudness(data, loudness, target)
    return _true_peak_limit(normalizado, techo_db=techo_db)
