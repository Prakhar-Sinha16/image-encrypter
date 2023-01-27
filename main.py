from image_operations import *
from algorithms import *
from file_operations import *

def encrpyt_image(image_path):
    """Encrypt an image"""
    try:
        # Combine the functions from the other files
        image_bytes = get_image_bytes(image_path)
        encoded = encode_image_bytes(image_bytes)
        results = encrypt_encoded_image(encoded)
        save_credentials_to_files(results)
        
        print("The image has been encrypted and saved to the files encryption.txt and decryption_key.txt")
    except Exception as e:
        print("An error occured while encrypting the image: " + str(e))

def decrppt_image():
    try:
        encrypted, decryption_key = read_credentials_from_files()
        decrypted = decrpyt_encrpyted_image(encrypted, decryption_key)
        save_image(decrypted, 'out.png')
        print("The image has been decrypted and saved to the file out.png")
    except Exception as e:
        print("An error occured while decrypting the image: " + str(e))
    
def main():
    print("Welcome to the image encryptor!\n\n1. Encrypt an image\n2. Decrypt an image\n")
    option = input("Please Choose an option(1 or 2): ")
    
    if option == "1":
        path = input("Please enter the path to the image you want to encrypt: ")
        encrpyt_image(path)
        
    elif option == "2":
        you_sure = input("Do you have the encrypted and decryption_key files in the same directory? (y/n): ")
        
        if (you_sure != "y"):
            print("Please make sure you have the files in the same directory as this script and try again!")
            return
        decrppt_image()
        
    else:
        print("Invalid option!")

if __name__ == '__main__':
    main()
