#!/usr/bin/env python3
"""
iOS App Icon Generator
Generates high-quality app icons using Stable Diffusion XL Turbo
Optimized for Apple Silicon (M-series chips)
"""
import torch
from diffusers import AutoPipelineForText2Image
from PIL import Image
import os
import argparse

def load_model(use_cpu: bool = False):
    """
    Load SDXL-Turbo model once for reuse
    """
    print("🚀 Initializing SDXL-Turbo for icon generation...")
    print(f"PyTorch version: {torch.__version__}")
    print(f"MPS (Metal) available: {torch.backends.mps.is_available()}")

    # Use CPU to avoid MPS issues, or MPS if requested
    if use_cpu:
        device = "cpu"
        dtype = torch.float32
        print("Using device: CPU (more stable)")
    else:
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        dtype = torch.float16 if device == "mps" else torch.float32
        print(f"Using device: {device}")

    # Load SDXL-Turbo model (faster and more stable)
    print("\n📦 Loading SDXL-Turbo model...")
    print("First run will download ~7GB - please wait...")

    pipe = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/sdxl-turbo",
        torch_dtype=dtype,
        variant="fp16" if dtype == torch.float16 else None
    )
    pipe = pipe.to(device)

    return pipe

def generate_base_icon(pipe, prompt: str, output_path: str = "icon_base.png"):
    """
    Generate a 1024x1024 base icon using SDXL-Turbo
    """
    # Enhanced prompt for iOS icon style
    enhanced_prompt = f"""{prompt}
    iOS app icon, minimalist design, clean, centered composition,
    professional, vibrant colors, gradient background, modern,
    no text, no letters, symbolic, square format, high quality"""

    # SDXL-Turbo works best with 1-4 steps and no guidance
    image = pipe(
        prompt=enhanced_prompt,
        num_inference_steps=4,
        guidance_scale=0.0,
        height=1024,
        width=1024,
    ).images[0]

    # Save base icon
    image.save(output_path, quality=95)

    return image

def resize_for_ios(base_image: Image.Image, output_dir: str = "ios_icons", app_name: str = "App"):
    """
    Resize base icon to all required iOS sizes
    """
    # iOS icon sizes (in pixels)
    ios_sizes = [
        ("icon_1024.png", 1024, 1024, "App Store"),
        ("icon_180.png", 180, 180, "iPhone @3x"),
        ("icon_167.png", 167, 167, "iPad Pro"),
        ("icon_152.png", 152, 152, "iPad @2x"),
        ("icon_120.png", 120, 120, "iPhone @2x"),
        ("icon_87.png", 87, 87, "iPhone @3x Settings"),
        ("icon_80.png", 80, 80, "iPad @2x Settings"),
        ("icon_76.png", 76, 76, "iPad"),
        ("icon_60.png", 60, 60, "iPhone"),
        ("icon_58.png", 58, 58, "iPhone @2x Settings"),
        ("icon_40.png", 40, 40, "Spotlight"),
        ("icon_29.png", 29, 29, "Settings"),
        ("icon_20.png", 20, 20, "Notification"),
    ]

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n📐 Resizing icon to {len(ios_sizes)} iOS sizes...")

    for filename, width, height, desc in ios_sizes:
        resized = base_image.resize((width, height), Image.Resampling.LANCZOS)
        output_path = os.path.join(output_dir, filename)
        resized.save(output_path, quality=95)
        print(f"  ✓ {filename:20} ({width}x{height}) - {desc}")

    print(f"\n✅ All icons saved to: {output_dir}/")
    print(f"Total files generated: {len(ios_sizes)}")

    # Create a simple Contents.json for Xcode
    create_contents_json(output_dir)

def create_contents_json(output_dir: str):
    """
    Create Contents.json for Xcode AppIcon.appiconset
    """
    contents = {
        "images": [
            {"filename": "icon_20.png", "idiom": "iphone", "scale": "1x", "size": "20x20"},
            {"filename": "icon_40.png", "idiom": "iphone", "scale": "2x", "size": "20x20"},
            {"filename": "icon_60.png", "idiom": "iphone", "scale": "3x", "size": "20x20"},
            {"filename": "icon_29.png", "idiom": "iphone", "scale": "1x", "size": "29x29"},
            {"filename": "icon_58.png", "idiom": "iphone", "scale": "2x", "size": "29x29"},
            {"filename": "icon_87.png", "idiom": "iphone", "scale": "3x", "size": "29x29"},
            {"filename": "icon_40.png", "idiom": "iphone", "scale": "1x", "size": "40x40"},
            {"filename": "icon_80.png", "idiom": "iphone", "scale": "2x", "size": "40x40"},
            {"filename": "icon_120.png", "idiom": "iphone", "scale": "3x", "size": "40x40"},
            {"filename": "icon_120.png", "idiom": "iphone", "scale": "2x", "size": "60x60"},
            {"filename": "icon_180.png", "idiom": "iphone", "scale": "3x", "size": "60x60"},
            {"filename": "icon_1024.png", "idiom": "ios-marketing", "scale": "1x", "size": "1024x1024"},
        ],
        "info": {
            "author": "icon_generator.py",
            "version": 1
        }
    }

    import json
    json_path = os.path.join(output_dir, "Contents.json")
    with open(json_path, 'w') as f:
        json.dump(contents, f, indent=2)
    print(f"  ✓ Contents.json created for Xcode")

def main():
    parser = argparse.ArgumentParser(
        description="Generate iOS app icons from a text prompt",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python icon_generator.py "A running shoe with a stopwatch"
  python icon_generator.py "Calculator app with numbers" --output calculator_icons
  python icon_generator.py "Music player app" --cpu
  python icon_generator.py "Running shoe with timer" --count 50
        """
    )
    parser.add_argument(
        "prompt",
        type=str,
        help="Description of the icon you want to generate"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="app_icons",
        help="Base output directory for icons (default: app_icons)"
    )
    parser.add_argument(
        "-n", "--name",
        type=str,
        default="app",
        help="App name for file naming (default: app)"
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=50,
        help="Number of variations to generate (default: 50)"
    )
    parser.add_argument(
        "--cpu",
        action="store_true",
        help="Force CPU usage instead of MPS (more stable but slower)"
    )

    args = parser.parse_args()

    # Load model once for all generations
    print(f"\n{'='*60}")
    print(f"Generating {args.count} icon variations")
    print(f"Prompt: {args.prompt}")
    print(f"{'='*60}\n")

    pipe = load_model(use_cpu=args.cpu)

    # Create high-res previews directory
    preview_dir = os.path.join(args.output, "high_res_previews")
    os.makedirs(preview_dir, exist_ok=True)

    # Generate multiple variations
    for i in range(1, args.count + 1):
        print(f"\n{'='*60}")
        print(f"🎨 Generating variation {i}/{args.count}")
        print(f"{'='*60}")

        # Create folder for this variation
        variation_dir = os.path.join(args.output, f"option_{i:02d}")
        os.makedirs(variation_dir, exist_ok=True)

        # Generate base icon
        base_filename = os.path.join(variation_dir, "icon_base.png")
        base_icon = generate_base_icon(pipe, args.prompt, base_filename)

        print(f"✅ Base icon saved to: {base_filename}")

        # Create all iOS sizes in the variation folder
        resize_for_ios(base_icon, variation_dir, args.name)

        # Copy high-res version to preview folder
        preview_filename = os.path.join(preview_dir, f"preview_{i:02d}.png")
        base_icon.save(preview_filename, quality=95)
        print(f"📋 High-res preview saved to: {preview_filename}")

    print(f"\n{'='*60}")
    print(f"🎉 Done! Generated {args.count} variations")
    print(f"{'='*60}")
    print(f"\n📁 Output structure:")
    print(f"   {args.output}/")
    print(f"   ├── high_res_previews/    (All 1024x1024 versions for comparison)")
    print(f"   ├── option_01/            (Full icon set)")
    print(f"   ├── option_02/            (Full icon set)")
    print(f"   └── ...")
    print(f"\n💡 To use in Xcode:")
    print(f"   1. Browse 'high_res_previews/' to pick your favorite")
    print(f"   2. Copy the corresponding 'option_XX/' folder to your Xcode project")
    print(f"   3. Rename it to 'AppIcon.appiconset'")
    print(f"   4. Place it inside Assets.xcassets/")

if __name__ == "__main__":
    main()
