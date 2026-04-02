#!/usr/bin/env python3
"""
Script to crop Safari browser chrome from Mia VMS app screenshots.
Detects where Safari UI ends and actual app content begins by analyzing color transitions.
"""

from PIL import Image
import os
from pathlib import Path

def find_chrome_end(image_path):
    """
    Find where Safari browser chrome ends by analyzing pixel rows from top.

    Safari chrome typically includes:
    - Tabs bar (~25-30px) - usually gray/light
    - URL bar (~35-40px) - usually white
    - Total chrome height: ~60-75px

    The app content (Mia VMS) typically has:
    - Dark sidebar on left
    - Light content area

    Returns the y-coordinate where app content begins.
    """
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Sample the middle of the image width to avoid edges
    sample_x = width // 2

    # Look for a significant color change that indicates end of chrome
    # Chrome is typically lighter (tabs/URL bar), app content has darker sidebar
    prev_brightness = None
    max_brightness_drop = 0
    chrome_end = 0

    for y in range(min(150, height)):  # Only check first 150 pixels max
        # Get pixel at this y coordinate
        r, g, b = pixels[sample_x, y][:3]  # Get RGB (ignore alpha if present)
        brightness = (r + g + b) / 3

        # Look for significant brightness drop
        if prev_brightness is not None:
            brightness_drop = prev_brightness - brightness
            if brightness_drop > max_brightness_drop:
                max_brightness_drop = brightness_drop
                chrome_end = y

        prev_brightness = brightness

    # Add some margin and round up to nearest pixel
    # Typically the chrome ends around 60-75px
    if chrome_end < 40:  # Minimum threshold
        chrome_end = 70  # Fallback to estimate
    else:
        chrome_end = min(chrome_end + 5, 85)  # Add small margin, cap at 85px

    return chrome_end


def crop_image(image_path, crop_top):
    """Crop image from the top by removing specified number of pixels."""
    try:
        img = Image.open(image_path)
        width, height = img.size

        # Crop: (left, top, right, bottom)
        cropped = img.crop((0, crop_top, width, height))

        # Save back to same file
        cropped.save(image_path, quality=95)

        original_height = height
        new_height = cropped.size[1]
        removed_pixels = original_height - new_height

        return {
            'file': os.path.basename(image_path),
            'original_size': (width, original_height),
            'new_size': cropped.size,
            'removed_pixels': removed_pixels,
            'status': 'success'
        }
    except Exception as e:
        return {
            'file': os.path.basename(image_path),
            'status': 'error',
            'error': str(e)
        }


def main():
    img_dir = '/Users/jishnunarasimhamoorthy/Desktop/vet-clinic-landing/img'

    # List of image files to process
    images = [
        'dashboard.png',
        'patient.png',
        'owner.png',
        'calendar.png',
        'queue.png',
        'services.png',
        'operations.png'
    ]

    print("Safari Chrome Cropping Tool")
    print("=" * 60)

    # First, analyze one image to determine chrome height
    first_image_path = os.path.join(img_dir, images[0])
    chrome_end = find_chrome_end(first_image_path)

    print(f"\nAnalyzing first image ({images[0]})...")
    print(f"Detected Safari chrome ends at pixel: {chrome_end}")
    print(f"Will remove top {chrome_end} pixels from all images\n")

    # Process all images
    results = []
    for image_name in images:
        image_path = os.path.join(img_dir, image_name)

        if not os.path.exists(image_path):
            print(f"❌ {image_name} - File not found")
            continue

        result = crop_image(image_path, chrome_end)
        results.append(result)

        if result['status'] == 'success':
            print(f"✓ {image_name}")
            print(f"  Original: {result['original_size']}")
            print(f"  New:      {result['new_size']}")
            print(f"  Removed:  {result['removed_pixels']}px from top")
        else:
            print(f"✗ {image_name} - Error: {result['error']}")

    # Summary
    print("\n" + "=" * 60)
    successful = sum(1 for r in results if r['status'] == 'success')
    print(f"Processed: {successful}/{len(results)} images successfully")

    if successful == len(results):
        print("All images cropped successfully!")
    else:
        print("Some images encountered errors.")


if __name__ == '__main__':
    main()
