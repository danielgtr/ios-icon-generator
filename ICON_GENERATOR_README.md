# iOS App Icon Generator

Generate high-quality iOS app icons using AI image generation, optimized for Apple Silicon (M4 Pro).

## What's Installed

This setup uses **Stable Diffusion XL Turbo** for fast, high-quality icon generation on your M4 Pro Mac.

### System Requirements
- macOS with Apple Silicon (M1/M2/M3/M4)
- Python 3.9+
- ~10GB free disk space for models
- Internet connection for initial model download

## Quick Start

### 1. Activate the Environment

```bash
source venv/bin/activate
```

### 2. Generate Icons

```bash
# Basic usage - generates all iOS icon sizes
python icon_generator.py "Your app description here"

# Example for the Pace Calculator app
python icon_generator.py "A modern running pace calculator app icon. Stopwatch timer with running shoe symbol. Blue and purple gradient background. Clean minimalist design."

# Specify custom output directory
python icon_generator.py "Music player app with headphones" --output music_icons

# Use CPU mode (more stable, slightly slower)
python icon_generator.py "Calculator app" --cpu
```

### 3. Use in Xcode

The generator creates all required iOS icon sizes automatically:

```
app_icons/
├── icon_1024.png  (App Store)
├── icon_180.png   (iPhone @3x)
├── icon_167.png   (iPad Pro)
├── icon_152.png   (iPad @2x)
├── icon_120.png   (iPhone @2x)
├── icon_87.png    (iPhone @3x Settings)
├── icon_80.png    (iPad @2x Settings)
├── icon_76.png    (iPad)
├── icon_60.png    (iPhone)
├── icon_58.png    (iPhone @2x Settings)
├── icon_40.png    (Spotlight)
├── icon_29.png    (Settings)
├── icon_20.png    (Notification)
└── Contents.json  (Xcode configuration)
```

**To use in Xcode:**
1. Rename the `app_icons/` folder to `AppIcon.appiconset`
2. Copy it into your project's `Assets.xcassets/` directory
3. The `Contents.json` is already configured - no manual setup needed!

## Command Line Options

```bash
python icon_generator.py --help

Arguments:
  prompt              Description of the icon to generate (required)

Options:
  -o, --output DIR   Output directory for icons (default: app_icons)
  -n, --name NAME    App name for file naming (default: app)
  --cpu              Force CPU usage instead of MPS (more stable)
```

## Examples

### Running/Fitness App
```bash
python icon_generator.py "Running shoe with stopwatch, blue gradient background, minimalist"
```

### Finance App
```bash
python icon_generator.py "Dollar sign with upward arrow, green gradient, professional"
```

### Weather App
```bash
python icon_generator.py "Sun and clouds, blue sky background, clean design"
```

### Task Manager
```bash
python icon_generator.py "Checkmark on paper, orange gradient, modern minimalist"
```

## Tips for Better Icons

1. **Be Specific**: Describe the main elements clearly
2. **Keep It Simple**: iOS icons work best with 1-2 main elements
3. **Mention Style**: Include words like "minimalist", "modern", "clean"
4. **Include Colors**: Specify gradient colors or color scheme
5. **Avoid Text**: Don't include letters/words in the prompt (iOS icons are symbolic)

### Good Prompts:
- "Stopwatch with running shoe, blue gradient, minimalist"
- "Camera lens with aperture, purple background, modern"
- "Heart rate monitor, red and pink gradient, clean design"

### Bad Prompts:
- "Running" (too vague)
- "App icon that says 'RUN' with text" (avoid text)
- "A very detailed realistic photograph of running shoes" (too complex)

## Upgrading to FLUX.1-schnell (Optional)

For even higher quality icons, you can use FLUX.1-schnell. This requires a free HuggingFace account.

### Setup FLUX

1. Create a free account at https://huggingface.co
2. Accept the FLUX.1-schnell license at https://huggingface.co/black-forest-labs/FLUX.1-schnell
3. Create an access token at https://huggingface.co/settings/tokens
4. Login from terminal:

```bash
source venv/bin/activate
huggingface-cli login
# Paste your token when prompted
```

5. Use the FLUX generator (coming soon):

```bash
python icon_generator_flux.py "Your prompt here"
```

## Models Used

### SDXL-Turbo (Default)
- **Size**: ~7GB
- **Speed**: Very fast (4 inference steps)
- **Quality**: Excellent for icons
- **Optimized**: Works great on M4 Pro
- **License**: Open source (Stability AI)

### FLUX.1-schnell (Optional)
- **Size**: ~24GB
- **Speed**: Fast (4 inference steps)
- **Quality**: Exceptional
- **Requires**: HuggingFace account + license agreement
- **License**: Apache 2.0 (requires acceptance)

## Troubleshooting

### Black/Corrupted Images
If you get all-black images, use CPU mode:
```bash
python icon_generator.py "your prompt" --cpu
```

### Out of Memory
The M4 Pro should handle these models fine, but if you encounter memory issues:
1. Close other applications
2. Use CPU mode with `--cpu` flag
3. Restart your terminal session

### Slow Generation
- First run is slower (downloading models)
- Subsequent runs are much faster (models cached)
- CPU mode is slower than MPS but more stable

### Model Download Issues
If download fails or is interrupted:
```bash
# Clear cache and retry
rm -rf ~/.cache/huggingface
python icon_generator.py "your prompt"
```

## Technical Details

- **Framework**: PyTorch with MPS backend (Metal Performance Shaders)
- **Image Generation**: Diffusers library by HuggingFace
- **Base Resolution**: 1024x1024 (then resized for all iOS sizes)
- **Resizing**: High-quality LANCZOS resampling
- **Format**: PNG with 95% quality

## File Structure

```
image-generation/
├── venv/                          # Python virtual environment
├── icon_generator.py              # Main CLI tool (SDXL-Turbo)
├── ICON_GENERATOR_README.md       # This file
├── app_icons/                     # Generated icons (output)
├── app_icon_base.png             # Base 1024x1024 image
└── ~/.cache/huggingface/         # Downloaded models (cached)
```

## Performance on M4 Pro

- **First Run**: 5-7 minutes (model download)
- **Subsequent Runs**: 30-60 seconds per icon set
- **Memory Usage**: ~8-10GB
- **Recommended**: Use MPS mode for best performance

## License

This tool is MIT licensed. However, generated images follow the license of the underlying models:
- SDXL-Turbo: Stability AI Community License
- FLUX.1-schnell: Apache 2.0 with usage restrictions

Always review the model licenses for commercial use.

## Credits

- Built with [Diffusers](https://github.com/huggingface/diffusers) by HuggingFace
- SDXL-Turbo by [Stability AI](https://stability.ai/)
- FLUX.1-schnell by [Black Forest Labs](https://blackforestlabs.ai/)
- Optimized for Apple Silicon M4 Pro
