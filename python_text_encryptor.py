from cryptography.fernet import Fernet

def generate_key() -> bytes:
    """Generate a new Fernet key."""
    return Fernet.generate_key()

def encrypt_message(key: bytes, message: str) -> bytes:
    """Encrypt a message using the provided key."""
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt_message(key: bytes, encrypted_message: bytes) -> str:
    """Decrypt an encrypted message using the provided key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

def main() -> None:
    print("Text Encryptor")

    while True:
        print("\nSelect an option:")
        print("1. Generate a new key")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = generate_key()
            print(f"Generated key: {key.decode()}")
        elif choice == '2':
            key = input("Enter the key: ").encode()
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(key, message)
            print(f"Encrypted message: {encrypted_message.decode()}")
        elif choice == '3':
            key = input("Enter the key: ").encode()
            encrypted_message = input("Enter the encrypted message: ").encode()
            try:
                decrypted_message = decrypt_message(key, encrypted_message)
                print(f"Decrypted message: {decrypted_message}")
            except Exception as e:
                print(f"Decryption error: {e}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()