#!/usr/bin/env python3
"""
iOS App Icon Generator - FLUX Edition
Generates highest-quality app icons using FLUX.1-schnell
Requires HuggingFace account and FLUX license acceptance
"""
import torch
from diffusers import FluxPipeline
from PIL import Image
import os
import argparse

def generate_base_icon(prompt: str, output_path: str = "icon_base.png", use_cpu: bool = False):
    """
    Generate a 1024x1024 base icon using FLUX.1-schnell
    """
    print("🚀 Initializing FLUX.1-schnell for icon generation...")
    print(f"PyTorch version: {torch.__version__}")
    print(f"MPS (Metal) available: {torch.backends.mps.is_available()}")

    # Use MPS or CPU
    if use_cpu:
        device = "cpu"
        dtype = torch.float32
        print("Using device: CPU")
    else:
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        dtype = torch.bfloat16 if device == "mps" else torch.float32
        print(f"Using device: {device}")

    # Load FLUX.1-schnell model
    print("\n📦 Loading FLUX.1-schnell model...")
    print("First run will download ~24GB - please be patient...")
    print("\nNOTE: If you get an authentication error:")
    print("1. Create account at https://huggingface.co")
    print("2. Accept license at https://huggingface.co/black-forest-labs/FLUX.1-schnell")
    print("3. Run: huggingface-cli login")
    print()

    try:
        pipe = FluxPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-schnell",
            torch_dtype=dtype
        )
        pipe = pipe.to(device)
    except Exception as e:
        print(f"\n❌ Error loading FLUX model: {e}")
        print("\nPlease ensure you:")
        print("1. Have a HuggingFace account")
        print("2. Accepted the FLUX.1-schnell license")
        print("3. Logged in with: huggingface-cli login")
        return None

    # Enhanced prompt for iOS icon style
    enhanced_prompt = f"""{prompt}
    iOS app icon style, minimalist, clean design, centered composition,
    professional quality, vibrant colors, gradient background,
    modern aesthetic, no text, no letters, symbolic, rounded square format,
    high detail, crisp edges"""

    print(f"\n🎨 Generating icon with FLUX...")
    print(f"Prompt: {prompt}")

    # FLUX.1-schnell works best with 4 steps and no guidance
    image = pipe(
        prompt=enhanced_prompt,
        num_inference_steps=4,
        guidance_scale=0.0,  # schnell doesn't use guidance
        height=1024,
        width=1024,
    ).images[0]

    # Save base icon
    image.save(output_path, quality=95)
    print(f"\n✅ Base icon saved to: {output_path}")
    print(f"Size: {image.size}")

    return image

def resize_for_ios(base_image: Image.Image, output_dir: str = "ios_icons"):
    """
    Resize base icon to all required iOS sizes
    """
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

    os.makedirs(output_dir, exist_ok=True)
    print(f"\n📐 Resizing icon to {len(ios_sizes)} iOS sizes...")

    for filename, width, height, desc in ios_sizes:
        resized = base_image.resize((width, height), Image.Resampling.LANCZOS)
        output_path = os.path.join(output_dir, filename)
        resized.save(output_path, quality=95)
        print(f"  ✓ {filename:20} ({width}x{height}) - {desc}")

    print(f"\n✅ All icons saved to: {output_dir}/")

    # Create Contents.json
    import json
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
        "info": {"author": "icon_generator_flux.py", "version": 1}
    }
    json_path = os.path.join(output_dir, "Contents.json")
    with open(json_path, 'w') as f:
        json.dump(contents, f, indent=2)
    print(f"  ✓ Contents.json created")

def main():
    parser = argparse.ArgumentParser(
        description="Generate iOS icons using FLUX.1-schnell (highest quality)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python icon_generator_flux.py "A running shoe with stopwatch"
  python icon_generator_flux.py "Calculator app" --output calc_icons
  python icon_generator_flux.py "Music player" --cpu

Requirements:
  1. HuggingFace account (free)
  2. Accept FLUX.1-schnell license
  3. Login with: huggingface-cli login
        """
    )
    parser.add_argument("prompt", type=str, help="Icon description")
    parser.add_argument("-o", "--output", default="flux_icons", help="Output directory")
    parser.add_argument("-n", "--name", default="app", help="App name")
    parser.add_argument("--cpu", action="store_true", help="Use CPU instead of MPS")

    args = parser.parse_args()

    # Generate base icon
    base_filename = f"{args.name}_icon_flux_base.png"
    base_icon = generate_base_icon(args.prompt, base_filename, use_cpu=args.cpu)

    if base_icon is None:
        print("\n❌ Failed to generate icon. Please check the requirements above.")
        return

    # Create all iOS sizes
    resize_for_ios(base_icon, args.output)

    print(f"\n🎉 FLUX icons ready in '{args.output}/'")
    print("\nTo use in Xcode:")
    print(f"1. Rename '{args.output}/' to 'AppIcon.appiconset'")
    print("2. Copy to Assets.xcassets/")
    print("3. Contents.json already configured!")

if __name__ == "__main__":
    main()
