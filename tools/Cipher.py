from cryptography.fernet import Fernet
import random
import string
import time
import os


class Cipher:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt_data(self, data: bytes) -> bytes:
        return self.fernet.encrypt(data)

    def decrypt_data(self, encrypted_data: bytes) -> bytes:
        return self.fernet.decrypt(encrypted_data)

    def encrypt_file(self, file_path: str, output_path: str):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        with open(file_path, 'rb') as f:
            file_data = f.read()

        encrypted_data = self.encrypt_data(file_data)
        file_name = os.path.basename(file_path) + ".enc"
        output_file_path = os.path.join(output_path, file_name)

        with open(output_file_path, 'wb') as f:
            f.write(encrypted_data)

        print(f"File encrypted and saved to {output_file_path}")

    def decrypt_file(self, file_path: str, output_path: str):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = self.decrypt_data(encrypted_data)
        file_name = os.path.basename(file_path).replace('.enc', '')
        output_file_path = os.path.join(output_path, file_name)

        with open(output_file_path, 'wb') as f:
            f.write(decrypted_data)

        print(f"File decrypted and saved to {output_file_path}")
