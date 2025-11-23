#!/usr/bin/env python3
"""
Generate iOS app icons using Stable Diffusion XL on M4 Pro Mac
Optimized for Apple Silicon using MPS backend
"""
import torch
from diffusers import DiffusionPipeline
from PIL import Image
import os

def generate_base_icon(prompt: str, output_path: str = "icon_base.png"):
    """
    Generate a 1024x1024 base icon using SDXL
    """
    print("🚀 Initializing SDXL for icon generation...")
    print(f"PyTorch version: {torch.__version__}")
    print(f"MPS (Metal) available: {torch.backends.mps.is_available()}")

    # Use MPS for M-series Macs
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Using device: {device}")

    # Load SDXL model
    print("\n📦 Loading Stable Diffusion XL model...")
    print("First run will download ~7GB - please wait...")

    pipe = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16"
    )
    pipe = pipe.to(device)

    # Optimize for M-series
    pipe.enable_attention_slicing()

    # Enhanced prompt for iOS icon style
    enhanced_prompt = f"""{prompt}
    iOS app icon style, minimalist, clean design, centered composition,
    professional quality, vibrant colors, gradient background,
    modern aesthetic, no text, no letters, symbolic, rounded square format"""

    negative_prompt = """text, letters, words, watermark, signature, blurry,
    low quality, distorted, ugly, bad anatomy, extra elements"""

    print(f"\n🎨 Generating icon...")
    print(f"Prompt: {prompt}")

    # Generate 1024x1024 image (standard iOS icon size)
    image = pipe(
        prompt=enhanced_prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=30,
        guidance_scale=7.5,
        height=1024,
        width=1024,
    ).images[0]

    # Save base icon
    image.save(output_path)
    print(f"\n✅ Base icon saved to: {output_path}")
    print(f"Size: {image.size}")

    return image

def resize_for_ios(base_image: Image.Image, output_dir: str = "ios_icons"):
    """
    Resize base icon to all required iOS sizes
    """
    # iOS icon sizes (in pixels)
    # Format: (size_name, width, height, description)
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

if __name__ == "__main__":
    # Example prompt for pace calculator app
    prompt = """A modern running pace calculator app icon.
    Stopwatch timer with running shoe symbol.
    Blue and purple gradient background.
    Clean minimalist design."""

    # Generate base 1024x1024 icon
    base_icon = generate_base_icon(prompt, "pace_calculator_icon_base.png")

    # Create all iOS sizes
    resize_for_ios(base_icon, "PaceCalculator_Icons")

    print("\n🎉 Done! Your iOS icons are ready!")
    print("To use in Xcode:")
    print("1. Create Assets.xcassets/AppIcon.appiconset/ in your project")
    print("2. Copy the generated icons")
    print("3. Update Contents.json with the icon references")
