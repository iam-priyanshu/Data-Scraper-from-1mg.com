# Script to read links from a folder containing links 
# and visit Tata1mg.com and getting all html div class class data 
# and writing it to a json file 

import requests
from bs4 import BeautifulSoup
import json
import os
import time

# File paths
URL_FILE = "unique.txt"  # File containing URLs
JSON_FILE = "medicinesData.json"  # Output JSON file

# Headers to avoid being blocked
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Function to scrape medicine details
def scrape_medicine(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"❌ Failed to fetch {url} (Status Code: {response.status_code})")
            return None
        
        soup = BeautifulSoup(response.text, "lxml")

        # Extract Name
        name = soup.find("h1", class_="DrugHeader__title-content___2ZaPo")
        name = name.text.strip() if name else "Not Found"

        # Extract Marketer
        marketer = soup.find("div", class_="DrugHeader__meta-value___vqYM0")
        marketer = marketer.text.strip() if marketer else "Not Found"

        # Extract Salt Composition
        salt = soup.find("div", class_="saltInfo DrugHeader__meta-value___vqYM0")
        salt = salt.text.strip() if salt else "Not Found"

        # Extract Uses
        uses = []
        uses_section = soup.find("ul", class_="DrugOverview__list___1HjxR DrugOverview__uses___1jmC3")
        if uses_section:
            uses = [li.text.strip() for li in uses_section.find_all("li")]

        # Extract Side Effects
        side_effects = []
        side_effects_section = soup.find("div", class_="DrugOverview__list-container___2eAr6")
        if side_effects_section:
            side_effects = [li.text.strip() for li in side_effects_section.find_all("li")]

        # Extract Substitutes
        substitutes = []
        substitutes_section = soup.find("div", class_="SubstituteList__container___iqJpc")
        if substitutes_section:
            for sub in substitutes_section.find_all("div", class_="row SubstituteItem__item___1wbMv"):
                sub_name = sub.find("div", class_="SubstituteItem__name___PH8Al")
                sub_price = sub.find("div", class_="SubstituteItem__unit-price___MIbLo")
                sub_manufacturer = sub.find("div", class_="SubstituteItem__manufacturer-name___2X-vB")

                substitutes.append({
                    "Name": sub_name.text.strip() if sub_name else "Unknown",
                    "Price": sub_price.text.strip() if sub_price else "Unknown",
                    "Manufacturer": sub_manufacturer.text.strip() if sub_manufacturer else "Unknown"
                })

        return {
            "Name": name,
            "Marketer": marketer,
            "Salt Composition": salt,
            "Uses": uses,
            "Side Effects": side_effects,
            "Substitutes": substitutes
        }

    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return None

# Ensure JSON file exists
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)  # Create an empty list in JSON file

# Read URLs from unique.txt
if os.path.exists(URL_FILE):
    with open(URL_FILE, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]
else:
    print(f"❌ {URL_FILE} not found!")
    urls = []

# Process each URL
for url in urls:
    print(f"🔍 Scraping: {url}")
    medicine_info = scrape_medicine(url)
    
    if medicine_info:
        try:
            # Load existing data
            with open(JSON_FILE, "r", encoding="utf-8") as f:
                try:
                    existing_data = json.load(f)
                    if not isinstance(existing_data, list):
                        existing_data = []  # Ensure it's a list
                except json.JSONDecodeError:
                    existing_data = []

            # Append new data
            existing_data.append(medicine_info)

            # Save updated JSON immediately
            with open(JSON_FILE, "w", encoding="utf-8") as f:
                json.dump(existing_data, f, indent=4)

            print(f"✅ Data saved for {url}")
        
        except Exception as e:
            print(f"❌ Error writing JSON: {e}")

    else:
        print(f"❌ Skipping {url} (No data found)")

    time.sleep(1)  # Prevent getting blocked

print(f"✅ All data saved to {JSON_FILE}!")
