"""Orquestador: cargar -> (opcional) reducir ruido -> masterizar -> exportar."""
from __future__ import annotations

from .analyze import medir_lufs
from .denoise import reducir_ruido
from .master import masterizar


def procesar(entrada, salida, objetivo="podcast", denoise=True, cantidad_ruido=0.85):
    """Procesa un archivo de audio y escribe el resultado en `salida`.

    Devuelve un informe con la sonoridad antes/después.
    """
    import soundfile as sf

    data, sr = sf.read(entrada)
    lufs_antes = medir_lufs(data, sr)

    if denoise:
        data = reducir_ruido(data, sr, cantidad=cantidad_ruido)

    data = masterizar(data, sr, objetivo=objetivo)
    lufs_despues = medir_lufs(data, sr)

    sf.write(salida, data, sr)
    return {
        "entrada": entrada,
        "salida": salida,
        "sr": sr,
        "objetivo": objetivo,
        "lufs_antes": round(lufs_antes, 2),
        "lufs_despues": round(lufs_despues, 2),
        "denoise": denoise,
    }
