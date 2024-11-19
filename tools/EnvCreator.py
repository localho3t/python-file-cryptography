import os
from cryptography.fernet import Fernet

class EnvCreator:
    def __init__(self, env_file='.env', key_name='ENCRYPTION_KEY'):
        self.env_file = env_file
        self.key_name = key_name
        self.key = None
        self._ensure_env_file()

    def _ensure_env_file(self):
        if not os.path.exists(self.env_file):
            print(f"{self.env_file} not found. Creating one...")
            self.key = Fernet.generate_key().decode()
            with open(self.env_file, 'w') as f:
                f.write(f"{self.key_name}={self.key}\n")
        else:
            self._load_key()

    def _load_key(self):
        with open(self.env_file, 'r') as f:
            for line in f:
                if line.startswith(f"{self.key_name}="):
                    self.key = line.split('=', 1)[1].strip()
                    break
        if not self.key:
            raise ValueError(f"{self.key_name} not found in {self.env_file}")

