
import os
import csv
from PIL import Image

# Supported image formats
SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff")


def get_file_size(file_path):
    """Return file size in KB."""
    return round(os.path.getsize(file_path) / 1024, 2)


def resize_image(image, target_width, target_height):
    """Resize image while maintaining aspect ratio."""

    image_copy = image.copy()

    image_copy.thumbnail(
        (target_width, target_height),
        Image.Resampling.LANCZOS
    )

    return image_copy


def convert_image_mode(image, output_format):
    """Prepare image color mode for the selected format."""

    if output_format == "JPEG":
        # JPEG does not support transparency
        if image.mode in ("RGBA", "LA") or "transparency" in image.info:
            image = image.convert("RGBA")

            background = Image.new("RGB", image.size, "white")
            background.paste(image, mask=image.getchannel("A"))

            return background

        return image.convert("RGB")

    # PNG supports transparency
    if output_format == "PNG":
        return image.convert("RGBA") if image.mode in ("RGBA", "LA") else image.convert("RGB")


def process_images():
    input_folder = input("Enter input folder path: ").strip().strip('"')
    output_folder = input("Enter output folder path: ").strip().strip('"')

    width = int(input("Enter target width: "))
    height = int(input("Enter target height: "))

    print("\nSelect output format:")
    print("1. JPEG")
    print("2. PNG")

    format_choice = input("Enter choice (1 or 2): ").strip()

    if format_choice == "1":
        output_format = "JPEG"
        extension = ".jpg"
    elif format_choice == "2":
        output_format = "PNG"
        extension = ".png"
    else:
        print("Invalid format choice.")
        return

    # JPEG quality
    quality = 90

    if output_format == "JPEG":
        quality = int(input("Enter JPEG quality (1-100): "))

        if not 1 <= quality <= 100:
            print("Quality must be between 1 and 100.")
            return

    # Thumbnail option
    thumbnail_choice = input(
        "Generate thumbnails too? (yes/no): "
    ).strip().lower()

    generate_thumbnails = thumbnail_choice in ("yes", "y")

    thumbnail_width = 150
    thumbnail_height = 150

    if generate_thumbnails:
        thumbnail_width = int(input("Enter thumbnail width: "))
        thumbnail_height = int(input("Enter thumbnail height: "))

    # Check folders
    if not os.path.isdir(input_folder):
        print("Input folder does not exist.")
        return

    os.makedirs(output_folder, exist_ok=True)

    thumbnail_folder = os.path.join(output_folder, "thumbnails")

    if generate_thumbnails:
        os.makedirs(thumbnail_folder, exist_ok=True)

    report_data = []

    # Scan all files in input folder
    for filename in os.listdir(input_folder):

        input_path = os.path.join(input_folder, filename)

        # Skip folders and unsupported files
        if not os.path.isfile(input_path):
            continue

        if not filename.lower().endswith(SUPPORTED_EXTENSIONS):
            continue

        try:
            with Image.open(input_path) as image:

                # Original details
                original_width, original_height = image.size
                original_size = get_file_size(input_path)

                # Resize main image
                resized_image = resize_image(
                    image, width, height
                )

                resized_image = convert_image_mode(
                    resized_image, output_format
                )

                output_filename = os.path.splitext(filename)[0] + extension
                output_path = os.path.join(output_folder, output_filename)

                # Save processed image
                save_options = {}

                if output_format == "JPEG":
                    save_options["quality"] = quality
                    save_options["optimize"] = True

                resized_image.save(
                    output_path,
                    format=output_format,
                    **save_options
                )

                # Result details
                new_width, new_height = resized_image.size
                new_size = get_file_size(output_path)

                print(f"Processed: {filename}")

                # Generate thumbnail
                thumbnail_path = ""

                if generate_thumbnails:

                    thumbnail = resize_image(
                        image, thumbnail_width, thumbnail_height
                    )

                    thumbnail = convert_image_mode(
                        thumbnail, output_format
                    )

                    thumbnail_filename = (
                        os.path.splitext(filename)[0] + extension
                    )

                    thumbnail_path = os.path.join(
                        thumbnail_folder, thumbnail_filename
                    )

                    thumbnail.save(
                        thumbnail_path,
                        format=output_format,
                        **save_options
                    )

                # Store report details
                report_data.append([
                    filename,
                    original_width,
                    original_height,
                    original_size,
                    output_filename,
                    new_width,
                    new_height,
                    new_size,
                    thumbnail_path
                ])

        except Exception as error:
            print(f"Failed to process {filename}: {error}")

    # Generate CSV report
    report_path = os.path.join(output_folder, "image_report.csv")

    with open(report_path, "w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "Original File",
            "Original Width",
            "Original Height",
            "Original Size (KB)",
            "Output File",
            "Output Width",
            "Output Height",
            "Output Size (KB)",
            "Thumbnail Path"
        ])

        writer.writerows(report_data)

    print("\nImage processing completed!")
    print(f"Processed images saved in: {output_folder}")
    print(f"Report saved in: {report_path}")


# Run the program
if __name__ == "__main__":
    process_images()
