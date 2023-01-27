import random

def encrypt_encoded_image(base64_bytes):
    """Encrypt the base64 encoded image"""
    encrypted = decryption_key = ""
    
    string_bytes = base64_bytes.decode('utf-8')
    for i in range(len(string_bytes)):
        char = str(string_bytes)[i]
        if char.isalpha():
            char_ord = ord(char)
            no = random.randint(1, char_ord)
            
            shifted_char_no = char_ord + no
            encrypted += f'{shifted_char_no}-'
            decryption_key += f'no{no}-'
        else:
            encrypted += f'{char}-'
            decryption_key += f'{char}-'
    
    # Delete the last dash from the strings.  
    encrypted, decryption_key = encrypted[:-1], decryption_key[:-1]
    
    return {
        'encrypted': encrypted,
        'decryption_key': decryption_key
    }
    
def decrpyt_encrpyted_image(encrpyted_image, decryption_key):
    """Decrypt the encrypted image with a decryption key"""
    decrypted = ""
    # Get the splitted strings for the decryption key and the encrypted image
    splitted_decryption_key, splitted_encrypted_image = decryption_key.split('-'), encrpyted_image.split('-')
    
    # Loop through the splitted strings and decrypt the image
    for i in range(len(splitted_decryption_key)):
        char = splitted_encrypted_image[i]
        if (splitted_decryption_key[i].startswith('no')):
            no = int(splitted_decryption_key[i].replace('no', ''))
            
            shifted_char = chr(int(char) - no)
            decrypted += shifted_char
        else:
            decrypted += splitted_decryption_key[i]
    return bytes(decrypted, 'utf-8')