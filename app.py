import os
import csv

CSV_FILE = "chicken_data.csv"

# --------------------- Utilities ---------------------

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_chickens():
    chickens = []
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            chickens = [row[0] for row in reader if row]
    except FileNotFoundError:
        # No file yet, start with defaults
        chickens = ["George", "Fleur", "Devon", "Casey", "Marigold", "Apple Mint"]
        save_chickens(chickens)
    return chickens

def save_chickens(chickens):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for chicken in chickens:
            writer.writerow([chicken])

# --------------------- Menu Functions ---------------------

def print_menu():
    print("\nChicken Record System")
    print("0 - Exit App")
    print("1 - Print List of Chicken Records")
    print("2 - Create New Chicken Record")
    print("3 - Update Existing Chicken Record")
    print("4 - Delete a Chicken Record")

def list_chickens(chickens):
    if chickens:
        print("\nChicken Records:")
        for i, name in enumerate(chickens, 1):
            print(f"{i}. {name}")
    else:
        print("No chicken records found.")

def add_chicken(chickens):
    name = input("Enter new chicken name: ").strip()
    if name:
        chickens.append(name)
        save_chickens(chickens)
        print(f"{name} added.")
    else:
        print("Invalid name.")

def update_chicken(chickens):
    list_chickens(chickens)
    try:
        idx = int(input("Enter record number to update: ")) - 1
        if 0 <= idx < len(chickens):
            new_name = input("Enter new name: ").strip()
            chickens[idx] = new_name
            save_chickens(chickens)
            print("Record updated.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def delete_chicken(chickens):
    list_chickens(chickens)
    try:
        idx = int(input("Enter record number to delete: ")) - 1
        if 0 <= idx < len(chickens):
            removed = chickens.pop(idx)
            save_chickens(chickens)
            print(f"{removed} deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

# --------------------- Main Program ---------------------

def main():
    chickens = load_chickens()
    while True:
        clear()
        print_menu()
        choice = input("Choose an option: ")
        if choice == '0':
            print("Exiting app.")
            break
        elif choice == '1':
            list_chickens(chickens)
        elif choice == '2':
            add_chicken(chickens)
        elif choice == '3':
            update_chicken(chickens)
        elif choice == '4':
            delete_chicken(chickens)
        else:
            print("Invalid option.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
