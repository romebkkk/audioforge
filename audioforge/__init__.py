"""
AudioForge — limpia y masteriza audio (voz, podcast, música) automáticamente.
by DataFlow Elegance · MIT

Flujo: reducir ruido -> normalizar a un objetivo de sonoridad (LUFS) -> limitar
picos -> exportar. Pensado para creadores: "sube tu audio cutre y sale pro".
"""
from .analyze import medir_lufs
from .denoise import reducir_ruido
from .master import masterizar
from .pipeline import procesar

__version__ = "0.1.0"
__all__ = ["medir_lufs", "reducir_ruido", "masterizar", "procesar", "__version__"]
