import base64
from PIL import Image

IMAGE_PATH = "infinite.png"

def get_image_bytes(image_path):
    """Get the image as bytes"""
    with open(image_path, "rb") as image_file:
        return image_file.read()

def encode_image_bytes(image_bytes):
    """Encode the image bytes to base64"""
    return base64.b64encode(image_bytes)

def decode_image_bytes(base64_bytes):
    """Decode the base64 encoded bytes"""
    return base64.b64decode(base64_bytes)

def encrypt_encoded_image(base64_bytes):
    """Encrypt the base64 encoded image"""
    pass

def decrpyt_encrpyted_image(encrpyted_image, decryption_key):
    """Decrypt the encrypted image with a decryption key"""
    pass

def save_image(base64_bytes, image_name):
    """Save the image to the file"""
    image_bytes = base64.b64decode(base64_bytes)
    image = Image.frombytes("RGB", (256, 256), image_bytes, "raw", "RGB", 0, 1)
    image.save(image_name)