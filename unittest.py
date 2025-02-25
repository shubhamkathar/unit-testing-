from pathlib import Path
import sys
from google import genai

# Initialize Gemini client (Replace with your actual API key)
client = genai.Client(api_key="Replace with yourAPI key")

def read_python_file(file_path):
    """Reads a Python (.py) file and returns its content as a string."""
    return Path(file_path).read_text(encoding="utf-8")

def get_test_cases_from_gemini(code_string):
    """Calls Gemini API to generate test cases based on the input code."""
    prompt_text = f"This is my Python code. I want to do unit testing on it, so only provide all possible test cases no unit testing code :\n\n{code_string}"
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt_text
    )
    
    return response.text if response else "Error: No response from Gemini."

def save_test_cases(test_cases):
    """Saves the generated test cases into a text file."""
    with open("test_cases.txt", "w", encoding="utf-8") as f:
        f.write(test_cases)
    print("\n✅ Test cases saved in test_cases.txt")

def read_test_cases():
    """Reads the test cases from test_cases.txt."""
    return Path("test_cases.txt").read_text(encoding="utf-8")

def generate_unit_test_code(test_cases):
    """Calls Gemini API to generate unit test code based on the test cases."""
    prompt_text = f"Here are some test cases. Generate Python unit test code using unittest module based on them:\n\n{test_cases}"
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt_text
    )
    
    return response.text if response else "Error: No response from Gemini."

def save_unit_test_code(unit_test_code):
    """Saves the generated unit test code into a Python file."""
    with open("unit_test.py", "w", encoding="utf-8") as f:
        f.write(unit_test_code)
    print("\n✅ Unit test code saved in unit_test.py")

# Check if filename is passed as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <filename.py>")
    sys.exit(1)

# Read the file
file_name = sys.argv[1]
pass_to_gs = read_python_file(file_name)

# Get test cases from Gemini
test_cases = get_test_cases_from_gemini(pass_to_gs)

# Save test cases to file
save_test_cases(test_cases)

# Read test cases from file
test_cases_from_file = read_test_cases()

# Generate unit test code from test cases
unit_test_code = generate_unit_test_code(test_cases_from_file)

# Save unit test code to file
save_unit_test_code(unit_test_code)
