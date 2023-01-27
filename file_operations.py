import base64
import io
import imghdr
from PIL import Image

def save_credentials_to_files(results):
    """Save the encrypted image and decryption key to a file"""
    with open("encryption.txt", 'w') as file:
        file.write(results['encrypted'])
    
    with open("decryption_key.txt", 'w') as file:
        file.write(results['decryption_key'])

def read_credentials_from_files():
    encryption_file = open("encryption.txt", 'r')
    decryption_key_file = open("decryption_key.txt", 'r') 

    return encryption_file.read(), decryption_key_file.read()

def save_image(base64_bytes, image_name):
    """Save the image to the file"""
    # Decode the base64 string
    image_bytes = base64.b64decode(base64_bytes + b'==')
    # Create a BytesIO object from the image bytes
    image_data = io.BytesIO(image_bytes)
    # detect the image file format
    file_format = imghdr.what(image_data)
    # Open the image file
    image = Image.open(image_data)
    # Save the image to file
    image.save(image_name, format = file_format)