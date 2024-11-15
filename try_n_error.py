from cryptography.fernet import Fernet

# Function to generate a key
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

# Function to load the key
def load_key():
    return open('secret.key', 'rb').read()

# Function to encrypt a message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    # Check if the key file exists, otherwise generate a new key
    try:
        load_key()
    except FileNotFoundError:
        print("No key found. Generating a new key...")
        generate_key()

    # User input for password
    password = input("Enter the password to encrypt: ")

    # Encrypt the password
    encrypted_password = encrypt_message(password)
    print(f"Encrypted password: {encrypted_password}")

    # Decrypt the password
    decrypted_password = decrypt_message(encrypted_password)
    print(f"Decrypted password: {decrypted_password}")

if __name__ == "__main__":
    main()
