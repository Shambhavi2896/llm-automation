
# /// script
# requires-python = ">=3.11"
# dependencies = [
# "os",
# "re",
# "json",
# "pathlib",
# ]
# ///
import os
import re
import json
from pathlib import Path

# Function to validate email format using regex
def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

# Function to extract sender/recipient email addresses from a text
def extract_emails(email_content):
    prompt = f"Extract the sender/recipient's email address from the following text: {email_content} and return only the sender/recipient's email address, nothing else"
    # Here you would call the LLM API to get the response
    # For the sake of this example, we assume the response is stored in `response_content`
    response_content = email_content  # Placeholder for actual LLM response
    extracted_emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', response_content)
    return extracted_emails

# Main function to process the email file
def process_email_file(input_file_path, output_file_path):
    if not os.path.exists(input_file_path):
        with open(input_file_path, 'w') as f:
            f.write("")  # Create an empty file if it does not exist
    with open(input_file_path, 'r') as file:
        email_content = file.read()
    emails = extract_emails(email_content)
    valid_emails = [email for email in emails if is_valid_email(email)]
    with open(output_file_path, 'w') as output_file:
        for email in valid_emails:
            output_file.write(email + '\n')

# Define paths
input_file = os.path.join('/data/', 'input_email.txt')
output_file = os.path.join('/data/', 'valid_emails.txt')

# Process the email file
process_email_file(input_file, output_file)