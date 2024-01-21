from PIL import Image
import os

def watermark_with_logo(image_path, logo_path, output_path, scale=0.1, opacity=128):
    try:
        image = Image.open(image_path)
        logo = Image.open(logo_path).convert("RGBA")
        
        # Calculate the new size of the logo based on the scale
        logo_size = (int(image.size[0] * scale), int(image.size[1] * scale))
        logo.thumbnail(logo_size, Image.ANTIALIAS)
        
        # Adjust logo opacity
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        alpha = logo.split()[3]
        alpha = Image.eval(alpha, lambda a: a//2 if a > opacity else a)
        logo.putalpha(alpha)

        # Set the position for the logo
        x = image.size[0] - logo.size[0] - int(image.size[0] * 0.05)
        y = image.size[1] - logo.size[1] - int(image.size[1] * 0.05)
        position = (x, y)

        # Paste the logo onto the image
        image.paste(logo, position, logo)

        # Save the watermarked image
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        image.save(output_path)
        print(f"Watermarked image saved as: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Placeholder paths for user input
input_directory = "path/to/your/originals"
output_directory = "path/to/your/watermarked/images"
logo_path = "path/to/your/logo.png"

# Loop over all images in the input directory and watermark them
for filename in os.listdir(input_directory):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, f"watermarked_{filename}")
        watermark_with_logo(image_path, logo_path, output_path)
