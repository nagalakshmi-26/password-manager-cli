import os
import json
import base64
import random
import string

DATA_FILE = "vault.json"

def generate_strong_password(length=14):
    """Generates a random, secure password with upper, lower, digits, and symbols."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
    return "".join(random.choice(chars) for _ in range(length))

def xor_cipher(text: str, key: str) -> str:
    """Simple XOR reversible encoding to store obfuscated credentials locally."""
    if not key:
        key = "default_vault_secret_key"
    extended_key = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, extended_key))

def encode_val(plain: str, key: str) -> str:
    obfuscated = xor_cipher(plain, key)
    return base64.b64encode(obfuscated.encode('utf-8')).decode('utf-8')

def decode_val(encoded: str, key: str) -> str:
    raw = base64.b64decode(encoded.encode('utf-8')).decode('utf-8')
    return xor_cipher(raw, key)

class PasswordVault:
    def __init__(self, master_password: str, filename=DATA_FILE):
        self.master_password = master_password
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def save_records(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.records, f, indent=4)

    def add_entry(self, service, username, password):
        service_key = service.strip().lower()
        enc_user = encode_val(username, self.master_password)
        enc_pass = encode_val(password, self.master_password)

        self.records[service_key] = {
            "display_name": service.strip(),
            "username": enc_user,
            "password": enc_pass
        }
        self.save_records()
        print(f"Password saved for '{service}'!")

    def get_entry(self, service):
        service_key = service.strip().lower()
        if service_key not in self.records:
            print(f"No entry found for '{service}'.")
            return None

        entry = self.records[service_key]
        try:
            user = decode_val(entry["username"], self.master_password)
            pwd = decode_val(entry["password"], self.master_password)
            return entry["display_name"], user, pwd
        except Exception:
            print("Failed to decrypt! Master password may be incorrect.")
            return None

    def list_services(self):
        if not self.records:
            print("Vault is currently empty.")
            return []

        print("\n" + "=" * 40)
        print(f"{'#':<4} | {'Saved Service/Site':<30}")
        print("=" * 40)
        services = []
        for i, (key, val) in enumerate(self.records.items(), 1):
            name = val.get("display_name", key)
            services.append(name)
            print(f"{i:<4} | {name:<30}")
        print("=" * 40)
        return services

    def delete_entry(self, service):
        service_key = service.strip().lower()
        if service_key in self.records:
            del self.records[service_key]
            self.save_records()
            print(f"Entry for '{service}' deleted.")
        else:
            print(f"No entry found for '{service}'.")
