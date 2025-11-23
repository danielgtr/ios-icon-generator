# iOS Icon Generator - Quick Reference Card

## Essential Commands

### 1. Activate Environment
```bash
source venv/bin/activate
```

### 2. Generate Icons
```bash
# Basic
python icon_generator.py "Your app description"

# With custom output folder
python icon_generator.py "Your description" --output my_icons

# CPU mode (more stable)
python icon_generator.py "Your description" --cpu
```

### 3. Use Quick Start
```bash
./quickstart.sh "Your app description"
```

## For Your Pace Calculator App

```bash
source venv/bin/activate

python icon_generator.py "Modern running pace calculator icon with stopwatch and athletic shoe, vibrant blue to purple gradient background, minimalist clean design, no text" --output PaceCalculator_Icons

# Then copy PaceCalculator_Icons/ to Xcode as AppIcon.appiconset
```

## Files Created

✅ All 13 iOS icon sizes (20px to 1024px)
✅ Contents.json for Xcode
✅ Ready to drop into Assets.xcassets/

## Tips

**Good Prompt:**
"Stopwatch and running shoe, blue gradient, minimalist, no text"

**Avoid:**
- Text/letters in the prompt
- Too many elements
- Vague descriptions

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Black images | Add `--cpu` flag |
| Too slow | First run downloads models (~7GB) |
| Memory error | Close other apps |

## Optional: FLUX Upgrade

```bash
# 1. Login to HuggingFace
huggingface-cli login

# 2. Use FLUX generator
python icon_generator_flux.py "Your prompt"
```

---

**Performance:** 30-60 seconds per icon set (after first download)
**Output:** 13 sizes + Contents.json
**Quality:** Production-ready iOS icons
