from image_operations import *
from algorithms import *
from file_operations import *
import base64
import cryptography.fernet as fernet
import openai
openai.api_key = "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"

def analyze_text(text):
    """Uses OpenAI's API to analyze text for potential security vulnerabilities"""
    prompt = f"Analyze the following text for security vulnerabilities: {text}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()


def encrpyt_image(image_path):
    """Encrypt an image"""
    try:
        # Combine the functions from the other files
        image_bytes = get_image_bytes(image_path)
        encoded = encode_image_bytes(image_bytes)
        results = encrypt_encoded_image(encoded)
        save_credentials_to_files(results)

        analysis = analyze_text(str(results))
        print("Security analysis results: ", analysis)
        
        print("The image has been encrypted and saved to the files encryption.txt and decryption_key.txt")
    except Exception as e:
        print("An error occured while encrypting the image: " + str(e))

def decrppt_image():
    try:
        encrypted, decryption_key = read_credentials_from_files()
        decrypted = decrpyt_encrpyted_image(encrypted, decryption_key)
        save_image(decrypted, 'out.png')

        # Analyze the decrypted data for potential vulnerabilities
        analysis = analyze_text(str(decrypted))
        print("Security analysis results: ", analysis)

        print("The image has been decrypted and saved to the file out.png")
    except Exception as e:
        print("An error occured while decrypting the image: " + str(e))

def encrypt_message(message, key):
    # Generate a fernet key from the given key
    fernet_key = fernet.Fernet(key)

    # Encode the message
    encoded_message = message.encode()

    # Encrypt the encoded message
    encrypted_message = fernet_key.encrypt(encoded_message)

    # Return the encrypted message
    return encrypted_message

def decrypt_message(encrypted_message, key):
    # Generate a fernet key from the given key
    fernet_key = fernet.Fernet(key)

    # Decrypt the encrypted message
    decrypted_message = fernet_key.decrypt(encrypted_message)

    # Decode the decrypted message
    # enter_key = int(input("Enter key: "))
    decoded_message = decrypted_message.decode()

    # Return the decoded message
    return decoded_message

# Example usage
key = fernet.Fernet.generate_key()

def main():
    print("Welcome to the image encryptor!\n\n1. Encrypt an image\n2. Decrypt an image\n")
    option = input("Please Choose an option(0 for sending private message or 1 or 2): ")
    if option =="0":
        # print("Press 0 for writting a encrypted message")
        message = input("Enter message:")
        encrypted_message = encrypt_message(message, key)
        print("Encrypted message:", encrypted_message)

        enter_key = input("Enter key: ")
        decrypted_message = decrypt_message(encrypted_message, key)
        if enter_key == "show":
            print("Decrypted message:", decrypted_message)
        else:
            print("couldn't load the message because of wrong password")

    if option == "1":
        path = input("Please enter the path to the image you want to encrypt: ")
        encrpyt_image(path)
        
    elif option == "2":
        you_sure = input("Do you have the encrypted and decryption_key files in the same directory? (y/n): ")
        
        if (you_sure != "y"):
            print("Please make sure you have the files in the same directory as this script and try again!")
            return
        decrppt_image()
        
    # else:
    #     print("Invalid option!")

if __name__ == '__main__':
    main()
