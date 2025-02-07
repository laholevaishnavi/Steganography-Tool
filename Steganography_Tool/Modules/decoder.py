from PIL import Image

def decode(image_path):
    """Decodes a hidden message from an image using LSB steganography."""
    img = Image.open(image_path).convert('RGB')
    binary_data = ""
    img_data = list(img.getdata())

    for i in range(len(img_data)):
        pixels = list(img_data[i])
        for j in range(3):
            binary_data += bin(pixels[j])[-1]

    # Convert binary data to characters
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_message = ""
    for byte in all_bytes:
        try:
            decoded_message += chr(int(byte, 2))
        except ValueError:
            break  # Stop when encountering non-ASCII characters or incomplete byte

    return decoded_message
