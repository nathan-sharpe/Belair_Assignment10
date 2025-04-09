#File Name : Zach.py
#Student Name: Zach Bell
#email:  bellzj@@mail.uc.edu
#Assignment Number: Assignment 10
#Due Date:   April 10 2025
#Course #/Section:   IS4010-001
#Semester/Year:   Spring 2025
# Brief Description of the assignment: Fetch JSON data from an API, parse it into a python data structure, extract some insights from it and then convert to CSV format.
# Brief Description of what this module does: Introduces us to working with JSON and how it is structured and fetched.
#Citations: https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv

import pandas as pd

class JsonToCsvConverter:
    def __init__(self, filename='CSVoutput.csv'):
        self.filename = filename

    def convert(self, data):
        """
        Converts the JSON data into a CSV file using pandas.
        @param: The dictionary containing JSON data from the API call.
        """
        if not data or 'product' not in data:
            print("No valid data to convert.")
            return

        product = data['product']
        output_data = {
            'Name': product.get('product_name', 'N/A'),
            'Barcode': data.get('code', 'N/A'),
            'Ingredients': product.get('ingredients_text', 'N/A'),
            'Packaging': product.get('packaging', 'N/A'),
            'Categories': product.get('categories', 'N/A'),
            'Nutrition Grade': product.get('nutrition_grades', 'N/A'),
            'Fat Level': product.get('nutrient_levels', {}).get('fat', 'N/A'),
            'Salt Level': product.get('nutrient_levels', {}).get('salt', 'N/A'),
            'Saturated Fat Level': product.get('nutrient_levels', {}).get('saturated-fat', 'N/A'),
            'Sugar Level': product.get('nutrient_levels', {}).get('sugars', 'N/A'),
            'Carbohydrates (100g)': product.get('nutriments', {}).get('carbohydrates_100g', 'N/A'),
            'Energy (kcal/100g)': product.get('nutriments', {}).get('energy-kcal_100g', 'N/A'),
            'Fat (100g)': product.get('nutriments', {}).get('fat_100g', 'N/A'),
            'Protein (100g)': product.get('nutriments', {}).get('proteins_100g', 'N/A'),
            'Salt (100g)': product.get('nutriments', {}).get('salt_100g', 'N/A'),
            'Sodium (100g)': product.get('nutriments', {}).get('sodium_100g', 'N/A'),
            'Sugar (100g)': product.get('nutriments', {}).get('sugars_100g', 'N/A'),
        }

        df = pd.DataFrame([output_data])  
        df.to_csv(self.filename, encoding='utf-8', index=False)
        print("\nCSV file '{}' has been created.".format(self.filename))
