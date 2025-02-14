
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

# Define the data directory
DATA_DIR = Path('/data/')

# Function to validate email format using regex
def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

# Function to extract sender/recipient email addresses from text
def extract_emails(email_content):
    # Assuming email_content is a string containing the email text
    # You would typically call the LLM here, but for now, we use regex to find emails
    potential_emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email_content)
    valid_emails = [email for email in potential_emails if is_valid_email(email)]
    return valid_emails

# Read email content from a file
input_file = DATA_DIR / 'emails.txt'
output_file = DATA_DIR / 'valid_emails.txt'

if not input_file.exists():
    with open(input_file, 'w') as f:
        f.write('')  # Create a blank file if it does not exist

with open(input_file, 'r') as f:
    email_content = f.read()

valid_emails = extract_emails(email_content)

# Write valid emails to the output file
with open(output_file, 'w') as f:
    for email in valid_emails:
        f.write(email + '\n')
