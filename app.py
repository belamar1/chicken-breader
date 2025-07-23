import csv
import re

CSV_FILE = "chicken_data.csv"

# --------------------- Validation Functions ---------------------

def valid_country(country):
    return bool(re.match(r"^[A-Za-z\s]{2,}$", country))

def valid_breed(breed):
    return bool(re.match(r"^[A-Za-z0-9\s\-]{2,}$", breed))

def valid_name(name):
    return bool(re.match(r"^[A-Za-z\s\-']{2,}$", name))

def valid_number(value):
    return bool(re.match(r"^\d+$", value))

def normalize_text(text):
    return text.strip().capitalize()

# --------------------- Load & Save ---------------------

def load_chickens():
    chickens = []
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                chickens.append(row)
    except FileNotFoundError:
        pass
    return chickens

def save_chickens(chickens):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ['Country', 'Breed', 'Name', 'Amount', 'Loss']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(chickens)

# --------------------- Menu Functions ---------------------

def view_chickens(chickens):
    if not chickens:
        print("No records found.")
        return
    print(f"{'Country':<12}{'Breed':<15}{'Name':<12}{'Amount':<8}{'Loss'}")
    print("-" * 55)
    for ch in chickens:
        print(f"{ch['Country']:<12}{ch['Breed']:<15}{ch['Name']:<12}{ch['Amount']:<8}{ch['Loss']}")

def filter_by_country(chickens):
    user_input = input("Enter country to filter by: ").strip()
    pattern = f"^{re.escape(user_input)}$"
    filtered = [ch for ch in chickens if re.match(pattern, ch['Country'], re.IGNORECASE)]
    view_chickens(filtered)

def add_chicken(chickens):
    while True:
        country = input("Enter country: ").strip()
        if valid_country(country): break
        print("❌ Invalid country. Letters and spaces only.")

    while True:
        breed = input("Enter breed: ").strip()
        if valid_breed(breed): break
        print("❌ Invalid breed. Only letters, numbers, hyphens allowed.")

    while True:
        name = input("Enter name: ").strip()
        if valid_name(name): break
        print("❌ Invalid name. Only letters, hyphens, apostrophes allowed.")

    while True:
        amount = input("Enter amount: ").strip()
        if valid_number(amount): break
        print("❌ Invalid amount. Must be a non-negative number.")

    while True:
        loss = input("Enter loss: ").strip()
        if valid_number(loss): break
        print("❌ Invalid loss. Must be a non-negative number.")

    chickens.append({
        'Country': normalize_text(country),
        'Breed': normalize_text(breed),
        'Name': normalize_text(name),
        'Amount': amount,
        'Loss': loss
    })
    save_chickens(chickens)
    print("✅ Record added.")

def update_chicken(chickens):
    view_chickens(chickens)
    name = input("Enter the name of the chicken to update: ").strip()
    for ch in chickens:
        if ch['Name'].lower() == name.lower():
            new_country = input(f"New country [{ch['Country']}]: ").strip()
            if new_country and valid_country(new_country):
                ch['Country'] = normalize_text(new_country)

            new_breed = input(f"New breed [{ch['Breed']}]: ").strip()
            if new_breed and valid_breed(new_breed):
                ch['Breed'] = normalize_text(new_breed)

            new_name = input(f"New name [{ch['Name']}]: ").strip()
            if new_name and valid_name(new_name):
                ch['Name'] = normalize_text(new_name)

            new_amount = input(f"New amount [{ch['Amount']}]: ").strip()
            if new_amount and valid_number(new_amount):
                ch['Amount'] = new_amount

            new_loss = input(f"New loss [{ch['Loss']}]: ").strip()
            if new_loss and valid_number(new_loss):
                ch['Loss'] = new_loss

            save_chickens(chickens)
            print("✅ Record updated.")
            return
    print("⚠️ Chicken not found.")

def delete_chicken(chickens):
    view_chickens(chickens)
    name = input("Enter the name of the chicken to delete: ").strip()
    for i, ch in enumerate(chickens):
        if ch['Name'].lower() == name.lower():
            confirm = input(f"Are you sure you want to delete {ch['Name']}? (y/n): ").strip().lower()
            if confirm == 'y':
                del chickens[i]
                save_chickens(chickens)
                print("🗑️ Record deleted.")
            else:
                print("Cancelled.")
            return
    print("⚠️ Chicken not found.")

def show_summary(chickens):
    try:
        total = sum(int(ch['Amount']) for ch in chickens)
        loss = sum(int(ch['Loss']) for ch in chickens)
        print(f"📊 Total Chickens: {total}")
        print(f"📉 Total Loss: {loss}")
    except ValueError:
        print("⚠️ Invalid number in data. Check 'Amount' and 'Loss' fields.")

# --------------------- Main App ---------------------

def main():
    chickens = load_chickens()
    while True:
        print("\n🐔 Chicken-UI Menu")
        print("0 - Exit")
        print("1 - View All Records")
        print("2 - Filter Records by Country")
        print("3 - Add New Chicken Record")
        print("4 - Update Existing Record")
        print("5 - Delete a Record")
        print("6 - Show Summary (Total Chickens, Losses)")
        choice = input("Enter your choice: ").strip()
        if choice == '0':
            print("👋 Exiting app.")
            break
        elif choice == '1':
            view_chickens(chickens)
        elif choice == '2':
            filter_by_country(chickens)
        elif choice == '3':
            add_chicken(chickens)
        elif choice == '4':
            update_chicken(chickens)
        elif choice == '5':
            delete_chicken(chickens)
        elif choice == '6':
            show_summary(chickens)
        else:
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
