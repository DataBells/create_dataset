import random
import uuid
import csv
from datetime import datetime, timedelta
import pandas as pd

def random_choice_with_probabilities(options, probabilities):
    return random.choices(options, probabilities, k=1)[0]

def generate_random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Predefined lists and probabilities

distributor_names = [
    "Carro", "Carsome", "Cars24", "Carousell", "Carmix", "Olx", "Trust", "Motor", "Oto", "Carmudi", "Automart", "Ahg", "Knox", "Trivett", "Zupps", "APE", "Skipper", "Nufor", "Marchi", "Sobri", "Kamkar"
]
distributor_probs = [0.13, 0.14, 0.15, 0.14, 0.14, 0.14, 0.13, 0.14, 0.13, 0.14, 0.13, 0.14, 0.14, 0.13, 0.14, 0.14, 0.13, 0.13, 0.14, 0.14, 0.13]

locations = [
    "North Carolina", "Tennessee", "California", "Texas", "Florida", "North Carolina", "Oklahoma", "Utah", "New York", "Chicago", "Denver", "Columbus", "Madison", "San Jose", "Detroit", "Portland", "Tucson", "Philadelphia"
]
location_probs = [0.13, 0.15, 0.14, 0.14, 0.13, 0.14, 0.13, 0.14, 0.15, 0.14, 0.14, 0.14, 0.13, 0.14, 0.14, 0.13, 0.14, 0.13]

car_details = {
    "Creta": ("Hyundai", "Hatchback"),
    "Dzire": ("Maruti", "Sedan"),
    "Etriga": ("Maruti", "Hatchback"),
    "i20": ("Hyundai", "Hatchback"),
    "Seltos": ("Kia", "Hatchback"),
    "Kags": ("Renault", "SUV"),
    "Swift": ("Maruti", "Sedan"),
    "Thar": ("Mahindra", "SUV"),
    "Scorpio": ("Mahindra", "SUV"),
    "Fortuner": ("Toyota", "SUV"),
    "Hilux": ("Toyota", "Truck"),
    "Yodha": ("Tata", "Truck"),
    "Plato": ("Prazo", "Convertible")
}
car_probs = [0.13, 0.14, 0.15, 0.14, 0.13, 0.14, 0.13, 0.14, 0.15, 0.14, 0.14, 0.14, 0.13]

colors = ["Red", "Blue", "Black", "White", "Gray"]
color_probs = [0.23, 0.23, 0.23, 0.15, 0.16]

grabboxes = ["Automatic", "Manual"]
grabbox_probs = [0.5, 0.5]

seat_options = [2, 4, 5, 7]
seat_probs = [0.1, 0.4, 0.4, 0.1]

door_options = [2, 4, 5]
door_probs = [0.2, 0.6, 0.2]

energies = ["Petrol", "Diesel", "Electric", "Hybrid"]
energy_probs = [0.25, 0.25, 0.25, 0.25]

feedbacks = ["Excellent", "Good", "Average", "Poor"]
feedback_probs = [0.4, 0.3, 0.2, 0.1]

sales_agents = ["Agent A", "Agent B", "Agent C", "Agent D", "Agent E"]

# Price and mileage functions
def generate_price(manufacturer, car_type, year, energy):
    base_price = 5000
    year_adjustment = (2024 - year) * 100
    type_adjustment = {"Sedan": 1000, "SUV": 2000, "Hatchback": 500, "Convertible": 3000, "Truck": 1500}.get(car_type, 0)
    energy_adjustment = {"Petrol": 500, "Diesel": 600, "Electric": 2000, "Hybrid": 1500}.get(energy, 0)
    return base_price + year_adjustment + type_adjustment + energy_adjustment

def generate_mileage():
    if random.random() < 0.15:
        return random.randint(75000, 1000000)
    return random.randint(1000, 75000)

def generate_engine_power():
    if random.random() < 0.15:
        return random.randint(111, 350)
    return random.randint(90, 110)

# Generate dataset
records = []
for _ in range(10000):
    record_id = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    distributor = random_choice_with_probabilities(distributor_names, distributor_probs)
    location = random_choice_with_probabilities(locations, location_probs)
    car_name = random_choice_with_probabilities(list(car_details.keys()), car_probs)
    manufacturer, car_type = car_details[car_name]
    color = random_choice_with_probabilities(colors, color_probs)
    gearbox = random_choice_with_probabilities(grabboxes, grabbox_probs)
    seats = random_choice_with_probabilities(seat_options, seat_probs)
    doors = random_choice_with_probabilities(door_options, door_probs)
    energy = random_choice_with_probabilities(energies, energy_probs)
    manufactured_year = random.randint(2015, 2024)
    price = generate_price(manufacturer, car_type, manufactured_year, energy)
    mileage = generate_mileage()
    engine_power = generate_engine_power()
    purchased_date = generate_random_date(2015, 2024)
    is_sold = random.random() < 0.22
    sold_date = generate_random_date(purchased_date.year, 2024) if is_sold else None
    if sold_date and (sold_date - purchased_date).days < 60:
        sold_date += timedelta(days=60)
    purchased_price = price - random.randint(500, 2000)
    sold_price = purchased_price + random.randint(-15, 15) if sold_date else None
    margin = ((sold_price - purchased_price) / purchased_price * 100) if sold_price else None
    car_sale_status = "Sold" if is_sold else "Un Sold"
    sales_agent = random.choice(sales_agents)
    sales_rating = random.randint(1, 5)
    sales_commission = (0.002 * (sold_price - purchased_price)) if margin and margin > 0 else 0
    feedback = random_choice_with_probabilities(feedbacks, feedback_probs)

    records.append({
        "ID": record_id,
        "Distributor Name": distributor,
        "Location": location,
        "Car Name": car_name,
        "Manufacturer Name": manufacturer,
        "Car Type": car_type,
        "Color": color,
        "Gearbox": gearbox,
        "Number of Seats": seats,
        "Number of Doors": doors,
        "Energy": energy,
        "Manufactured Year": manufactured_year,
        "Price": price,
        "Mileage": mileage,
        "Engine Power": engine_power,
        "Purchased Date": purchased_date.strftime("%Y-%m-%d"),
        "Car Sale Status": car_sale_status,
        "Sold Date": sold_date.strftime("%Y-%m-%d") if sold_date else None,
        "Purchased Price": purchased_price,
        "Sold Price": sold_price,
        "Margin": margin,
        "Sales Agent Name": sales_agent,
        "Sales Rating": sales_rating,
        "Sales Commission": sales_commission,
        "Feedback": feedback,
    })

# Save to CSV
with open("used_car_sales.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = records[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print("Dataset generated and saved as used_car_sales.csv")

# Save to Excel
df = pd.DataFrame(records)
excel_file_name = "used_car_sales.xlsx"
df.to_excel(excel_file_name, index=False, sheet_name="Car Sales Data")

print(f"Dataset also saved as {excel_file_name}")
