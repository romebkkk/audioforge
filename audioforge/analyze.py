"""Medición de sonoridad (LUFS) según la norma EBU R128 / ITU-R BS.1770."""
from __future__ import annotations


def medir_lufs(data, sr):
    """Devuelve la sonoridad integrada en LUFS de una señal (numpy array)."""
    import pyloudnorm as pyln
    meter = pyln.Meter(sr)  # bloque BS.1770
    return float(meter.integrated_loudness(data))


# Objetivos de sonoridad habituales por plataforma (LUFS integrados).
OBJETIVOS = {
    "podcast": -16.0,
    "spotify": -14.0,
    "youtube": -14.0,
    "broadcast": -23.0,  # EBU R128
    "apple_music": -16.0,
}
