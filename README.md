# Data-Scraper-from-1mg.com

# Tata 1mg Medicine Data Scraper  

## Overview  
This project is a Python-based web scraper that extracts medicine-related data from the **Tata 1mg** website. The scraper follows a two-step process: first, it collects all medicine page URLs, and then it visits each URL to extract and store the complete HTML content. The extracted data is saved in structured formats for further analysis or offline use.  

## Features  
✅ **Automated Link Collection:** The script crawls the Tata 1mg website and extracts all medicine page URLs, storing them in a `medicine_links.txt` file.  
✅ **Efficient Data Extraction:** Reads the stored links and systematically visits each page.  
✅ **HTML Data Storage:** Saves the raw HTML content of each medicine page in a structured JSON file.  
✅ **Error Handling & Delay Management:** Includes time delays to prevent getting blocked and handles errors gracefully.  

## Tech Stack  
- **Python:** Core scripting language  
- **BeautifulSoup:** For parsing HTML content  
- **Requests:** For making HTTP requests  
- **OS & JSON:** For file handling and structured data storage  
- **Time:** To manage request delays  

## How It Works  
1. **Scraping Phase:**  
   - `scraper.py` visits the Tata 1mg website and extracts all available medicine page links.  
   - These links are stored in `medicine_links.txt` for further processing.  

2. **Extraction Phase:**  
   - `extractor.py` reads the `medicine_links.txt` file.  
   - It sequentially visits each medicine page, retrieves the HTML content, and saves it into `medicine_data.json`.  

## Installation & Usage  
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/tata1mg-scraper.git
   cd tata1mg-scraper
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the scraper:  
   ```bash
   python scraper.py
   ```  
4. Extract data:  
   ```bash
   python extractor.py
   ```  

## Use Cases  
This project is useful for researchers, developers, and data analysts needing medicine-related HTML data for **NLP models, data extraction, or market research.** 🚀
