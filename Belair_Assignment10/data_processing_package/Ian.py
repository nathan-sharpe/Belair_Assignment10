#File Name : Ian.py
#Student Name: Ian McDaniel
#email:  mcdaniip@mail.uc.edu
#Assignment Number: Assignment 10
#Due Date:   April 10 2025
#Course #/Section:   IS4010-001
#Semester/Year:   Spring 2025
# Brief Description of the assignment: Fetch JSON data from an API, parse it into a python data structure, 
# extract some insights from it and then convert to CSV format.
# Brief Description of what this module does: Introduces us to working with JSON and how it is structured and fetched.
#Citations: https://brightdata.com/faqs/json/extract-json-response-python

def extract_and_print_data_2(data):
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

 