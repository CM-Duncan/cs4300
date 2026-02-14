from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message)
    return decrypted.decode()
