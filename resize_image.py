from PIL import Image

# Open the uploaded image
input_path = "/Users/apple/Downloads/Signature_1.JPG"
output_path = "/Users/apple/Downloads/Signature_1_100x100.jpg"

# Resize the image to 100x100 pixels
with Image.open(input_path) as img:
    resized_img = img.resize((100, 100))
    resized_img.save(output_path)

print(output_path)
