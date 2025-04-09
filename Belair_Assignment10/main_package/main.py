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

# Anything else that's relevant: I (Nathan Sharpe) handled main to avoid merge conflicts while everyone else worked
# within their own files in the data processing package.

from data_processing_package.data_processing import *

from data_processing_package.Evan import *
from data_processing_package.Ian import *
from data_processing_package.Zach import *


if __name__ == "__main__":
    # Instantiate the DataProcessing class and call the fetchData method on the class object
    api_data_processing = DataProcessing()
    data = api_data_processing.fetchData()

    # Extract and print data to the console
    api_data_processing.extract_and_print_data(data)
    api_data_processing.extract_and_print_data_2(data)

    # Write results to CSV file
    csv_converter = JsonToCsvConverter("nutella_data.csv")
    csv_converter.convert(data)
