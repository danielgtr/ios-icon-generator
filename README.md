# iOS App Icon Generator 🎨

Generate production-ready iOS app icons using AI-powered image generation, optimized for Apple Silicon (M-series Macs).

![iOS Icon Sizes](https://img.shields.io/badge/iOS-13%20Sizes-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-Optimized-orange)

## Features

- 🚀 **Fast Generation**: 30-60 seconds per complete icon set
- 🎯 **All iOS Sizes**: Automatically generates all 13 required icon sizes
- 🍎 **Apple Silicon Optimized**: Built for M1/M2/M3/M4 Macs
- 📱 **Xcode Ready**: Includes Contents.json configuration
- 🎨 **High Quality**: Uses SDXL-Turbo or FLUX.1-schnell models
- 💻 **100% Local**: No cloud APIs, all processing on-device

## Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install mlx mlx-lm huggingface-hub Pillow transformers accelerate safetensors diffusers invisible_watermark torch
```

### 2. Generate Icons

```bash
# Basic usage
python icon_generator.py "Your app description here"

# Example
python icon_generator.py "Running app with stopwatch, blue gradient, minimalist"

# With custom output
python icon_generator.py "Calculator app" --output calculator_icons
```

### 3. Use in Xcode

1. Rename the output folder to `AppIcon.appiconset`
2. Copy to your project's `Assets.xcassets/` directory
3. Build and run!

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/ios-icon-generator.git
cd ios-icon-generator

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install mlx mlx-lm huggingface-hub Pillow transformers accelerate safetensors diffusers invisible_watermark torch
```

## Usage

### Basic Command

```bash
python icon_generator.py "Your icon description"
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `prompt` | Icon description (required) | - |
| `-o, --output` | Output directory | `app_icons` |
| `-n, --name` | App name for file naming | `app` |
| `--cpu` | Use CPU instead of MPS | `False` |

### Examples

```bash
# Weather app
python icon_generator.py "Sun and clouds, blue sky, modern design"

# Finance app
python icon_generator.py "Dollar sign with growth arrow, green gradient"

# Fitness tracker
python icon_generator.py "Heart rate monitor, red gradient, minimalist"

# Task manager
python icon_generator.py "Checkmark on list, orange gradient, clean"
```

## Generated Icon Sizes

All 13 iOS icon sizes are automatically created:

- 1024×1024 (App Store)
- 180×180 (iPhone @3x)
- 167×167 (iPad Pro)
- 152×152 (iPad @2x)
- 120×120 (iPhone @2x)
- 87×87 (iPhone @3x Settings)
- 80×80 (iPad @2x Settings)
- 76×76 (iPad)
- 60×60 (iPhone)
- 58×58 (iPhone @2x Settings)
- 40×40 (Spotlight)
- 29×29 (Settings)
- 20×20 (Notification)

## Tips for Best Results

### Good Prompts ✅

- "Stopwatch with running shoe, blue gradient, minimalist, no text"
- "Camera lens with aperture, purple background, modern"
- "Heart rate monitor, red and pink gradient, clean design"

### Avoid ❌

- Vague descriptions ("running app")
- Text or letters in the prompt
- Too many elements (cluttered)
- Overly complex scenes

## Advanced: FLUX.1-schnell (Optional)

For highest quality icons, use the FLUX generator:

### Setup

1. Create free HuggingFace account: https://huggingface.co
2. Accept FLUX license: https://huggingface.co/black-forest-labs/FLUX.1-schnell
3. Login:
   ```bash
   huggingface-cli login
   ```

### Usage

```bash
python icon_generator_flux.py "Your icon description"
```

## System Requirements

- **OS**: macOS with Apple Silicon (M1/M2/M3/M4)
- **Python**: 3.9 or later
- **RAM**: 16GB+ recommended
- **Storage**: ~10GB for models
- **Internet**: Required for initial model download

## Performance

| Stage | Time | Notes |
|-------|------|-------|
| First run | 8-10 min | One-time model download (~7GB) |
| Subsequent runs | 30-60 sec | Models cached locally |
| Memory usage | 8-10GB | During generation |

## Models Used

### SDXL-Turbo (Default)
- **Size**: ~7GB
- **Speed**: 4 inference steps
- **Quality**: Excellent for icons
- **License**: Stability AI Community License

### FLUX.1-schnell (Optional)
- **Size**: ~24GB
- **Speed**: 4 inference steps
- **Quality**: Exceptional
- **License**: Apache 2.0 (requires acceptance)

## Project Structure

```
ios-icon-generator/
├── icon_generator.py              # Main tool (SDXL-Turbo)
├── icon_generator_flux.py         # FLUX version (optional)
├── quickstart.sh                  # Easy launcher
├── ICON_GENERATOR_README.md       # Full documentation
├── QUICK_REFERENCE.md             # Command cheat sheet
├── requirements.txt               # Python dependencies
└── .gitignore                     # Git ignore rules
```

## Troubleshooting

### Black/Corrupted Images

Use CPU mode for more stability:
```bash
python icon_generator.py "your prompt" --cpu
```

### Memory Issues

- Close other applications
- Use CPU mode: `--cpu`
- Restart terminal session

### Slow Generation

- First run always slower (downloads models)
- Subsequent runs use cached models
- CPU mode slower but more stable than MPS

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

Model licenses:
- SDXL-Turbo: Stability AI Community License
- FLUX.1-schnell: Apache 2.0 (requires acceptance)

## Credits

- Built with [Diffusers](https://github.com/huggingface/diffusers) by HuggingFace
- SDXL-Turbo by [Stability AI](https://stability.ai/)
- FLUX.1-schnell by [Black Forest Labs](https://blackforestlabs.ai/)
- Optimized for Apple Silicon

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

Made with ❤️ for iOS developers
