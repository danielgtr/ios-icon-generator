#!/bin/bash
# Quick Start Script for iOS Icon Generator

echo "🚀 iOS Icon Generator - Quick Start"
echo "===================================="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run setup first."
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Check if we have arguments
if [ $# -eq 0 ]; then
    echo ""
    echo "Please provide a description of your icon:"
    echo ""
    echo "Examples:"
    echo "  ./quickstart.sh \"Running app with stopwatch and shoe\""
    echo "  ./quickstart.sh \"Calculator app with numbers\""
    echo "  ./quickstart.sh \"Music player with headphones\""
    echo ""
    exit 1
fi

# Get the prompt
PROMPT="$1"
OUTPUT_DIR="${2:-app_icons}"

echo ""
echo "🎨 Generating icons for: $PROMPT"
echo "📁 Output directory: $OUTPUT_DIR"
echo ""

# Run the icon generator
python icon_generator.py "$PROMPT" --output "$OUTPUT_DIR" --cpu

# Check if successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Success! Icons are ready in: $OUTPUT_DIR/"
    echo ""
    echo "Next steps:"
    echo "1. Rename $OUTPUT_DIR/ to AppIcon.appiconset"
    echo "2. Copy to your Xcode project's Assets.xcassets/"
    echo "3. Build and run!"
else
    echo ""
    echo "❌ Generation failed. Please check the error messages above."
fi
