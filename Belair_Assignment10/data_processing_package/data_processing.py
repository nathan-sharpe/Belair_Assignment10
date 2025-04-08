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

# Anything else that's relevant: I (Nathan Sharpe) built the class and combined the methods from other memebers 
# added to their own files to minimize the possibility of merge conflicts occuring. 

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

    def extract_and_print_data_2(self, data):
        """
        Extracts interesting information from the fetched data and prints it in a friendly format.
        @param data dict: The dictionary containing parsed JSON data from the API call.

        """
        print("\nNutrient Levels:")
        fat = data['product']['nutrient_levels']['fat']
        salt = data['product']['nutrient_levels']['salt']
        saturatedfats = data['product']['nutrient_levels']['saturated-fat']
        sugars = data['product']['nutrient_levels']['sugars']

        print(f"Fat: {fat}")
        print(f"Salt: {salt}")
        print(f"Saturated Fat: {saturatedfats}")
        print(f"Sugar: {sugars}")

        print("\nNutrition Macros per 100g:")

        carbs = data['product']['nutriments']['carbohydrates_100g']
        energy = data['product']['nutriments']['energy-kcal_100g']
        fat = data['product']['nutriments']['fat_100g']
        protein = data['product']['nutriments']['proteins_100g']
        salt = data['product']['nutriments']['salt_100g']
        sodium = data['product']['nutriments']['sodium_100g']
        sugar = data['product']['nutriments']['sugars_100g']

        print(f"Carbohydrates: {carbs}g")
        print(f"Energy: {energy} kcal")
        print(f"Fat: {fat}g")
        print(f"Protein: {protein}g")
        print(f"Salt: {salt}g")
        print(f"Sodium: {sodium}g")
        print(f"Sugar: {sugar}g")