#!/usr/bin/env python3
"""
Test FLUX.1-schnell image generation on M4 Pro Mac
"""
import torch
from diffusers import FluxPipeline
from PIL import Image

def test_flux():
    print("🚀 Testing FLUX.1-schnell on M4 Pro...")
    print(f"PyTorch version: {torch.__version__}")
    print(f"MPS (Metal) available: {torch.backends.mps.is_available()}")

    # Use MPS (Metal Performance Shaders) for M-series Macs
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Using device: {device}")

    # Load FLUX.1-schnell model (optimized for speed)
    print("\n📦 Loading FLUX.1-schnell model...")
    print("This will download ~24GB on first run - please be patient...")

    pipe = FluxPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-schnell",
        torch_dtype=torch.bfloat16
    )
    pipe = pipe.to(device)

    # Test prompt for a running app icon
    prompt = """A minimalist iOS app icon for a running pace calculator app.
    Modern, clean design with a stopwatch and running shoe symbol.
    Vibrant gradient background from blue to purple.
    Professional, high quality, centered composition, no text."""

    print(f"\n🎨 Generating test image...")
    print(f"Prompt: {prompt}")

    # Generate image
    image = pipe(
        prompt,
        num_inference_steps=4,  # schnell works well with just 4 steps
        guidance_scale=0.0,     # schnell doesn't use guidance
        height=1024,
        width=1024,
    ).images[0]

    # Save test image
    output_path = "test_icon.png"
    image.save(output_path)
    print(f"\n✅ Image saved to: {output_path}")
    print(f"Image size: {image.size}")

if __name__ == "__main__":
    test_flux()
