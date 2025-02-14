
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

# Define the path to the data directory
DATA_DIR = Path('/data/')

# Function to validate email format using regex
def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

# Function to extract sender/recipient email addresses from text
def extract_emails_from_text(email_content):
    prompt = f"Extract the sender/recipient's email address from the following text: {email_content} and return only the sender/recipient's email address, nothing else"
    response = requests.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', json={'model': 'GPT-4o-Mini', 'messages': [{'role': 'user', 'content': prompt}]}, headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {os.getenv("AIPROXY_TOKEN")}'})
    return response.json()["choices"][0]["message"]["content"].strip()

# Function to read email content from input file and extract valid emails
def process_email_file(input_file, output_file):
    input_path = DATA_DIR / input_file
    output_path = DATA_DIR / output_file
    if not input_path.exists():
        print(f"Error: Input file '{input_file}' does not exist. Creating a blank file.")
        input_path.touch()
    valid_emails = []
    with open(input_path, 'r') as file:
        for line in file:
            email_content = line.strip()
            extracted_email = extract_emails_from_text(email_content)
            if is_valid_email(extracted_email):
                valid_emails.append(extracted_email)
    if valid_emails:
        with open(output_path, 'w') as outfile:
            outfile.write('\n'.join(valid_emails))
    else:
        print(f"No valid emails extracted from '{input_file}'.")

# Example usage
process_email_file('emails.txt', 'valid_emails.txt')