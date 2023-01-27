import base64

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