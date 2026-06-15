from cryptography.fernet import Fernet

with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

file = "patient_data.txt"
with open(file, "rb") as f:
    encrypted_data = f.read()

decrypted = cipher.decrypt(encrypted_data)

with open(file, "wb") as f:
    f.write(decrypted)

print("[+] File decrypted successfully")
