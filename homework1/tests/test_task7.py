"Caroline Duncan, 2/14/26, checking that keys are generated as bytes and that messages can be properly encrypted and decrypted"
from src.task7 import generate_key, encrypt_message, decrypt_message

def test_generate_key():
    key = generate_key()
    assert key is not None
    assert type(key) == bytes

def test_encrypt_message():
    key = generate_key()
    encrypted = encrypt_message(key, "Hello, World!")
    assert encrypted is not None
    assert type(encrypted) == bytes

def test_decrypt_message():
    key = generate_key()
    original = "Hello, World!"
    encrypted = encrypt_message(key, original)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == original
