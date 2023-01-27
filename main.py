import base64
from PIL import Image
import random
import json

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
    encrypted = ""
    decryption_key = ""
    
    string_bytes = str(base64_bytes)
    for i in range(len(string_bytes)):
        char = str(string_bytes)[i]
        if char.isalpha():
            no_1 = random.randrange(80, 99)
            no_2 = random.randrange(20, 29)
            no_3 = random.randrange(1, 9)
            
            shifted_char = chr((ord(char) + no_3 - no_1) % no_2 + no_1)
            encrypted += shifted_char
            decryption_key += f"{no_1}.{no_2}.{no_3}-"
        else:
            encrypted += char
            decryption_key += f'{char}-'
    
    decryption_key = decryption_key[:-1]
    return {
        'encrypted': encrypted,
        'decryption_key': decryption_key
    }
    
def decrpyt_encrpyted_image(encrpyted_image, decryption_key):
    """Decrypt the encrypted image with a decryption key"""
    pass

def save_image(base64_bytes, image_name):
    """Save the image to the file"""
    image_bytes = decode_image_bytes(base64_bytes)
    image = Image.frombytes("RGB", (256, 256), image_bytes, "raw", "RGB", 0, 1)
    image.save(image_name)
    
def main():
    image_bytes = get_image_bytes(IMAGE_PATH)
    encoded = encode_image_bytes(image_bytes)
    results = encrypt_encoded_image(encoded)
    
    with open("results.json", 'w') as file:
        json_dumps_str = json.dumps(results, indent=4)
        file.write(json_dumps_str)

main()