import sys
from vault import PasswordVault, generate_strong_password

def print_menu():
    print("\n--- PASSWORD VAULT MENU ---")
    print("1. Add / Store Password")
    print("2. Retrieve a Password")
    print("3. List All Saved Services")
    print("4. Generate a Random Strong Password")
    print("5. Delete an Entry")
    print("6. Exit")

def main():
    print("==========================================")
    print("    [SECURE] Simple CLI Password Manager  ")
    print("==========================================")
    
    master_key = input("Enter your Master Vault Key: ").strip()
    if not master_key:
        print("Master Key cannot be empty. Exiting.")
        sys.exit(1)

    vault = PasswordVault(master_key)

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            service = input("Enter Service/Website name (e.g., GitHub, Netflix): ").strip()
            username = input("Enter Username / Email: ").strip()
            
            gen_prompt = input("Auto-generate a strong password? (y/n, default n): ").strip().lower()
            if gen_prompt == "y":
                password = generate_strong_password()
                print(f"Generated Password: {password}")
            else:
                password = input("Enter Password: ").strip()

            if service and username and password:
                vault.add_entry(service, username, password)
            else:
                print("All fields are required!")

        elif choice == "2":
            service = input("Enter Service name to retrieve: ").strip()
            res = vault.get_entry(service)
            if res:
                svc, user, pwd = res
                print("\n---------------------------------")
                print(f"Service : {svc}")
                print(f"Username: {user}")
                print(f"Password: {pwd}")
                print("---------------------------------")

        elif choice == "3":
            vault.list_services()

        elif choice == "4":
            len_input = input("Password length (default 14): ").strip()
            length = int(len_input) if len_input.isdigit() else 14
            pwd = generate_strong_password(length)
            print(f"\n[KEY] Generated Secure Password: {pwd}")

        elif choice == "5":
            service = input("Enter Service name to delete: ").strip()
            vault.delete_entry(service)

        elif choice == "6":
            print("Vault locked. Stay secure! Goodbye.")
            sys.exit(0)

        else:
            print("Invalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
