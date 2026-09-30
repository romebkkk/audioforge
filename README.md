# 🎙️ AudioForge

> "Upload your rough audio → get a professional-sounding file." AudioForge **removes background noise**, **normalizes loudness to a target (LUFS)** and **limits peaks** — automatically. For podcasters, musicians and video creators. Python pipeline, self-hostable.

<sub>Part of the **DataFlow Audio** suite · [🇪🇸 Español abajo](#-español)</sub>

---

## What it does
- 🧹 **Denoise** background hum/hiss (`noisereduce`; optional DeepFilterNet for voice).
- 📏 **Loudness normalization** to broadcast targets (EBU R128 / ITU-R BS.1770) — Podcast −16, Spotify/YouTube −14, Broadcast −23 LUFS.
- 🔒 **True-peak limiting** (default −1 dBTP) so it never clips.
- Reports loudness **before/after**.

## Install & use
Python 3.10+.
```bash
pip install -r requirements.txt
python cli.py --in bruto.wav --out pro.wav --target podcast
```
Targets: `podcast`, `spotify`, `youtube`, `broadcast`, `apple_music`, or a number (e.g. `-14`).

## Status
Reference implementation using the documented APIs of `pyloudnorm`, `noisereduce` and `soundfile`. Runs on CPU (no GPU needed). Verify on your machine with the deps installed.

## License
[MIT](LICENSE) © 2026 DataFlow Elegance

---

## 🇪🇸 Español
**AudioForge**: "sube tu audio cutre y sale profesional". **Quita el ruido de fondo**, **iguala el volumen a un objetivo (LUFS)** y **limita los picos**, automáticamente. Para podcasters, músicos y creadores de vídeo.

- 🧹 **Reducción de ruido** (`noisereduce`; DeepFilterNet opcional para voz).
- 📏 **Normalización de sonoridad** (EBU R128) — Podcast −16, Spotify/YouTube −14, Broadcast −23 LUFS.
- 🔒 **Limitador de pico** (−1 dBTP) para que no sature.
- Informe de sonoridad **antes/después**.

```bash
pip install -r requirements.txt
python cli.py --in bruto.wav --out pro.wav --target podcast
```
Funciona en CPU (sin GPU). Implementación de referencia sobre `pyloudnorm`/`noisereduce`/`soundfile`; verifícalo en tu máquina con las dependencias instaladas.

---

<div align="center">
Hecho con ❤️ por <a href="https://github.com/romebkkk">DataFlow Elegance</a> · <a href="https://dataflowelegance.es">dataflowelegance.es</a>
</div>
