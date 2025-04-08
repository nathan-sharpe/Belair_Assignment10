# File Name : main.py
# Student Name: Nathan Sharpe
# email: sharpenn@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Fetch JSON data from an API, parse it into a python data structure, 
# extract some insights from it and then convert to CSV format.

# Brief Description of what this module does: Introduces us to working with JSON and how it is structured and fetched.

# Citations: 
# The data source pulled from: https://world.openfoodfacts.org/data
# Their API Documentation: https://openfoodfacts.github.io/openfoodfacts-server/api/

# Anything else that's relevant: 

import json
import requests

class DataProcessing:
    def fetchData(self):
        """
        Fetches JSON data from an the Open Food Facts API on the Nutella Ferrero product and returns it as a python dictionary
        @return python_dict dict: The dictionary containing the parsed JSON data fetched from the API call
        """
        response = requests.get('https://world.openfoodfacts.org/api/v3/product/3017624010701.json')
        json_string = response.content
        python_dict = json.loads(json_string)
        return python_dict

    def extract_and_print_data(self, data):
        """
        Extracts interesting information from the fetched data and prints it in a friendly format.
        @param data dict: The dictionary containing parsed JSON data from the API call.
        """
        if data:
            # Extract interesting fields from the JSON data
            product_name = data.get('product', {}).get('product_name', 'N/A')
            barcode = data.get('code', 'N/A')
            ingredients_text = data.get('product', {}).get('ingredients_text', 'N/A')
            packaging = data.get('product', {}).get('packaging', 'N/A')
            categories = data.get('product', {}).get('categories', 'N/A')
            nutrition_grade = data.get('product', {}).get('nutrition_grades', 'N/A')

            # Print the extracted data in a friendly format
            print("Product Information:")
            print(f"Name: {product_name}")
            print(f"Barcode: {barcode}")
            print(f"Ingredients: {ingredients_text}")
            print(f"Packaging: {packaging}")
            print(f"Categories: {categories}")
            print(f"Nutrition Grade: {nutrition_grade}")
        else:
            print("No data available to extract.")