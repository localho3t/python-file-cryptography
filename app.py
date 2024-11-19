from tools.EnvCreator import EnvCreator
import argparse
from tools.Cipher import Cipher

import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt Files")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("input", help="Input file path")
    parser.add_argument("output", help="Output folder path")
    args = parser.parse_args()

    # Load or generate encryption key
    env_creator = EnvCreator()
    cipher = Cipher(env_creator.key.encode())

    # Perform action
    if args.action == "encrypt":
        cipher.encrypt_file(args.input, args.output)
    elif args.action == "decrypt":
        cipher.decrypt_file(args.input, args.output)