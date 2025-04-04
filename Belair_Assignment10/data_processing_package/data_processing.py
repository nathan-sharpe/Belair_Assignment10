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