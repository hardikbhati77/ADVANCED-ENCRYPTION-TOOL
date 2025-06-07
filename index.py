from cryptography.fernet import Fernet
import os

# ---------- KEY GENERATION ----------
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔑 Key generated and saved as secret.key")

def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("❌ secret.key not found. Please generate key first.")
        return None

# ---------- ENCRYPTION ----------
def encrypt_file(file_path):
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)
    
    try:
        with open(file_path, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(file_path + ".enc", 'wb') as enc_file:
            enc_file.write(encrypted)
        print(f"✅ File encrypted successfully: {file_path}.enc")
    except FileNotFoundError:
        print("❌ File not found.")

# ---------- DECRYPTION ----------
def decrypt_file(encrypted_path):
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)

    try:
        with open(encrypted_path, 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        original_path = encrypted_path.replace(".enc", ".dec")
        with open(original_path, 'wb') as dec_file:
            dec_file.write(decrypted)
        print(f"✅ File decrypted successfully: {original_path}")
    except FileNotFoundError:
        print("❌ Encrypted file not found.")
    except Exception as e:
        print(f"❌ Decryption failed: {e}")

# ---------- CLI MENU ----------
def main():
    while True:
        print("\n🔐 Advanced File Encryption Tool")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            path = input("Enter path to file to encrypt: ")
            encrypt_file(path)
        elif choice == "3":
            path = input("Enter path to encrypted (.enc) file: ")
            decrypt_file(path)
        elif choice == "0":
            print("👋 Exiting encryption tool.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
