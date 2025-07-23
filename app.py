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
        if ch['Nam