
# Image Resizer & Format Converter

## Problem Statement

An organisation has a collection of product photographs that need to be uploaded to its website. However, the images have different dimensions and file formats.

This Python program processes images in a folder, resizes them to fit within user-defined dimensions while maintaining their original aspect ratio, converts them to a selected format, and creates a report containing the original and processed image details.

## Features

- Accepts an input folder and output folder from the user.
- Supports common image formats: JPG, JPEG, PNG, WEBP, BMP, and TIFF.
- Resizes images to user-specified dimensions.
- Maintains the original aspect ratio without stretching.
- Allows users to select JPEG or PNG output format.
- Allows users to specify JPEG quality (1–100).
- Keeps original images unchanged.
- Generates a CSV report containing original and processed image details.
- Optionally generates thumbnail versions of images.

## Technologies Used

- Python
- Pillow (PIL)
- CSV module
- OS module

## Requirements

- Python 3.8 or above
- Pillow

## Installation

Install the required library using:

```bash
pip install Pillow
```

## Project Structure

```text
image_resizer/
│
├── image_processor.py
├── input/
│   ├── product1.jpg
│   ├── product2.png
│   └── product3.webp
│
└── output/
    ├── product1.jpg
    ├── product2.jpg
    ├── product3.jpg
    ├── image_report.csv
    │
    └── thumbnails/
        ├── product1.jpg
        ├── product2.jpg
        └── product3.jpg
```

## How to Run

1. Place the images inside the input folder.
2. Open the project in VS Code.
3. Run the program:

   ```bash
   python image_processor.py
   ```

4. Enter the input folder path.
5. Enter the output folder path.
6. Enter the target width and height.
7. Select the output format (JPEG or PNG).
8. If JPEG is selected, enter the image quality (1–100).
9. Choose whether to generate thumbnails.
10. If thumbnails are enabled, enter the thumbnail width and height.

## Aspect Ratio

The program maintains the original aspect ratio of images while resizing.

For example, if an image has dimensions of 4000 × 2000 pixels and the target dimensions are 800 × 800 pixels, the resulting image will be 800 × 400 pixels.

This prevents the image from becoming stretched or distorted.

## JPEG Quality

JPEG quality determines the compression level of the saved image.

- 100 – Higher quality and generally larger file size.
- 90 – Good quality for most website images.
- 50 – More compression and generally smaller file size.

The quality setting is applicable only when the output format is JPEG.

## CSV Report

The program generates an `image_report.csv` file inside the output folder.

The report contains:

- Original filename
- Original width
- Original height
- Original file size
- Output filename
- Output width
- Output height
- Output file size
- Thumbnail path

The CSV report can be opened using Microsoft Excel or other spreadsheet applications.

## Thumbnail Generation

The program optionally creates thumbnail versions of the processed images.

Thumbnails are saved inside a separate `thumbnails` folder within the output folder.

Thumbnail images are resized to fit within the specified dimensions while maintaining the original aspect ratio.


