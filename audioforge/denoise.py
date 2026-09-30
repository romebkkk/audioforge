"""Reducción de ruido.

Por defecto usa `noisereduce` (spectral gating, funciona en CPU). Para máxima
calidad en voz puedes cambiar a DeepFilterNet (opcional, más pesado).
"""
from __future__ import annotations


def reducir_ruido(data, sr, cantidad=0.85):
    """Reduce el ruido de fondo estacionario. `cantidad` en [0, 1]."""
    import noisereduce as nr
    return nr.reduce_noise(y=data, sr=sr, prop_decrease=float(cantidad), stationary=True)
