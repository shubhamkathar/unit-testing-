Automated Unit Test Case Generator

This Python script automates the process of generating unit test cases using Google's Gemini AI. Given a Python script as input, it:

Extracts the code from the file.

Generates all possible test cases using the Gemini API.

Saves the test cases to a text file (test_cases.txt).

Generates unit test code using the unittest module.

Saves the unit test code in unit_test.py.

Prerequisites

Python 3.8 or later

Google Gemini API key

Required Python packages (see requirements.txt)

Installation

Clone or download this repository.

Install the dependencies using:

pip install -r requirements.txt

Usage

Run the script with a Python file as input:

python script.py <filename.py>

Example

python unittest.py for_test.py

This will generate:

test_cases.txt: Contains generated test cases.

unit_test.py: Contains unittest code based on the generated test cases.

Configuration

Replace Replace with yourAPI key in the script with your actual Gemini API key.

Files

unittest.py – Main script for generating test cases and unit tests.

test_cases.txt – Stores generated test cases.

unit_test.py – Stores generated unittest code.

requirements.txt – Lists dependencies.

Dependencies

Check requirements.txt for necessary packages.