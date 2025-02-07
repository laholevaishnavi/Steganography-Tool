from PIL import Image

def encode(image_path, message, output_path):
    """Encodes a message into an image using LSB steganography."""
    img = Image.open(image_path).convert('RGB') # Ensure the image is RGB
    binary_message = ''.join(format(ord(char), '08b') for char in message) # Convert message to binary

    data_index = 0
    img_data = list(img.getdata()) # Get pixel data as a list of tuples

    for i in range(len(img_data)):
        pixels = list(img_data[i])
        for j in range(3):  # Iterate through R, G, B
            if data_index < len(binary_message):
                pixels[j] = int(bin(pixels[j])[:-1] + binary_message[data_index], 2)
                data_index += 1
        img_data[i] = tuple(pixels)

    img.putdata(img_data)

    # Save the encoded image
    img.save(output_path, "PNG") # Save as PNG to avoid quality loss
