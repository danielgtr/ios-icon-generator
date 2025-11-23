# Pace Calculator - iOS App

A native iOS running pace calculator app built with SwiftUI.

## Features

### 1. Pace Converter
- Convert pace between km and miles
- Calculate speed in km/h and mph
- Perfect for treadmill settings

### 2. Run Calculator
- Calculate total run time based on distance and pace
- Preset race distances (5K, 10K, Half Marathon, Marathon, 50K, 100K)
- Support for both metric (km) and imperial (miles) units
- Shows treadmill speed settings

### 3. Race Splits Calculator (New!)
- Calculate split times for races
- Customizable split intervals (1km, 1mi, 5km, etc.)
- Shows cumulative time for each split
- Perfect for race planning and pacing strategy

## Requirements

- iOS 16.0 or later
- Xcode 15.0 or later
- Swift 5.9 or later

## Installation

1. Open `PaceCalculator.xcodeproj` in Xcode
2. Select your development team in the Signing & Capabilities tab
3. Build and run on your device or simulator

## Deployment to Physical Device

### Step 1: Configure Signing
1. Open the project in Xcode
2. Select the PaceCalculator target
3. Go to "Signing & Capabilities"
4. Select your Apple Developer Team
5. Xcode will automatically generate a provisioning profile

### Step 2: Build for Device
1. Connect your iPhone via USB
2. Select your iPhone from the device dropdown in Xcode
3. Click the Run button (▶️)
4. On first run, you may need to trust the developer certificate on your iPhone:
   - Settings → General → VPN & Device Management
   - Tap your developer certificate
   - Tap "Trust"

### Step 3: Using CodeSign (if needed)
If you need to manually sign the app:
```bash
# Build the app first
xcodebuild -project PaceCalculator.xcodeproj -scheme PaceCalculator -configuration Release

# The built app will be in the build folder
# Sign it with your certificate
codesign --force --sign "iPhone Developer: Your Name" PaceCalculator.app
```

## Project Structure

```
PaceCalculator/
├── PaceCalculator.xcodeproj/
│   └── project.pbxproj           # Xcode project file
└── PaceCalculator/
    ├── PaceCalculatorApp.swift   # App entry point
    ├── ContentView.swift          # Main tab view
    ├── Info.plist                 # App configuration
    ├── Models/
    │   └── PaceCalculator.swift  # Core calculation logic
    └── Views/
        ├── PaceConverterView.swift
        ├── RunCalculatorView.swift
        └── RaceSplitsView.swift
```

## Usage Tips

- All calculations update in real-time
- Use the preset race distance buttons for quick setup
- The app supports both portrait and landscape orientations
- Dark mode is automatically supported
- All data is calculated locally - no internet connection required

## Customization

### Changing Bundle Identifier
Edit `project.pbxproj` and search for `PRODUCT_BUNDLE_IDENTIFIER`. Change `com.yourcompany.PaceCalculator` to your own identifier.

### Adding App Icons
1. Create an `Assets.xcassets` folder in the PaceCalculator directory
2. Add an `AppIcon.appiconset` folder inside
3. Add icon images in the required sizes
4. Update the `Contents.json` file

## Common Race Distances Included

- 5K (5.0 km / 3.1 mi)
- 10K (10.0 km / 6.2 mi)
- Half Marathon (21.1 km / 13.1 mi)
- Marathon (42.2 km / 26.2 mi)
- 50K (50.0 km / 31.1 mi)
- 100K (100.0 km / 62.1 mi)

## Testing Checklist

- [ ] Pace conversion works correctly
- [ ] Run time calculation is accurate
- [ ] Race splits calculator generates correct splits
- [ ] Preset distances populate correctly
- [ ] App works in both portrait and landscape
- [ ] Dark mode displays correctly
- [ ] Tab navigation works smoothly
- [ ] All pickers scroll smoothly
- [ ] Calculations are accurate for edge cases

## License

This project is provided as-is for personal use.
