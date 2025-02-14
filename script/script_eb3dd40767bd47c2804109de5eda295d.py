
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

# Ensure the output directory exists
output_dir = Path('/data/')
output_dir.mkdir(parents=True, exist_ok=True)

# Function to validate email format using regex
def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

# Function to extract sender/recipient emails from a file
def extract_emails(input_file, output_file):
    input_path = output_dir / input_file
    output_path = output_dir / output_file
    if not input_path.is_file():
        with open(input_path, 'w') as f:
            f.write('')  # Create a blank file if it doesn't exist
    with open(input_path, 'r') as f:
        email_content = f.read()
    # Simulate LLM request
    # Here, you would call the LLM API to extract emails
    extracted_emails = re.findall(r'[\w\.-]+@[\w\.-]+', email_content)
    valid_emails = [email for email in extracted_emails if is_valid_email(email)]
    with open(output_path, 'w') as f:
        f.write('\n'.join(valid_emails))  # Write valid emails to the output file

# Example usage
extract_emails('input.txt', 'output.txt')