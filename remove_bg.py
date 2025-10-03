import os
from io import BytesIO
from PIL import Image
from rembg import remove

input_path = "/Users/apple/Downloads/passport_image.jpg"
output_path = "/Users/apple/Downloads/passport_image_white_bg.jpg"

print("Starting bg removal...")
print("Open image...")
with open(input_path, "rb") as inp_file:
    input_data = inp_file.read()

print("Remove background...")
output_data = remove(input_data)

print("Convert back to Image...")
image = Image.open(BytesIO(output_data)).convert("RGBA")

print("Create white background...")
white_bg = Image.new("RGBA", image.size, (255, 255, 255, 255))
final_image = Image.alpha_composite(white_bg, image)

print("Convert to RGB (drop alpha) for JPG...")
final_image = final_image.convert("RGB")

max_size = 2 
max_size_in_bytes = 1024 * 1024

print(f"Saving under {max_size}MB...")
def save_under_a_certain_mb(img, path):
    quality = 95
    while quality > 10:
        img.save(path, "JPEG", quality=quality, optimize=True)
        if os.path.getsize(path) <= max_size_in_bytes:
            break
        quality -= 5
    print(f"Final quality used: {quality}, size: {os.path.getsize(path)/1024:.2f} KB")


print("Save with auto adjustment...")
save_under_a_certain_mb(final_image, output_path)

print(f"✅ Saved at: {output_path}")
