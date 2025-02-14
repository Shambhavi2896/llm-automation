
# /// script
# requires-python = ">=3.11"
# dependencies = [
# "os",
# "re",
# "json",
# "requests",
# "pathlib",
# ]
# ///
import os
import re
import json
import requests
from pathlib import Path

# Function to validate email format using regex.
def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

# Function to extract sender/recipient email addresses from the provided text.
def extract_emails(email_content):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, email_content)

# Main function to read email file, extract emails, validate and write to output file.
def process_email_file(input_file, output_file):
    input_path = os.path.join('/data/', input_file)
    output_path = os.path.join('/data/', output_file)

    # Create output file if it doesn't exist
    if not os.path.exists(output_path):
        open(output_path, 'w').close()

    try:
        with open(input_path, 'r') as file:
            email_content = file.read()
            extracted_emails = extract_emails(email_content)
            valid_emails = [email for email in extracted_emails if is_valid_email(email)]

            with open(output_path, 'w') as output:
                for email in valid_emails:
                    output.write(email + '\n')
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
input_file = 'emails.txt'
output_file = 'valid_emails.txt'
process_email_file(input_file, output_file)