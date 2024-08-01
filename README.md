# Flipkart-Mobile-Scraping-Project

This project scrapes mobile phone data from Flipkart and saves it to a CSV file. The data includes the mobile name, price, and specifications.

## Project Structure

- **web_scraping_script.py**: The main script for web scraping mobile data.
- **Mobile_Data.csv**: The output file containing the scraped data.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/Flipkart-Mobile-Scraping-Project.git
    cd Flipkart-Mobile-Scraping-Project
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the web scraping script:
    ```sh
    python web_scraping_script.py
    ```

2. The data will be saved in `Mobile_Data.csv` in the `Downloads` directory.

## Requirements

- Python 3.x
- requests
- beautifulsoup4
- pandas

To install the required packages, you can run:
```sh
pip install requests beautifulsoup4 pandas
