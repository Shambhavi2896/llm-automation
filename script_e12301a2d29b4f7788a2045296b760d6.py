
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

# Function to validate email format using regex.
def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

# Function to extract sender/recipient email addresses from email content.
def extract_emails(email_content):
    # Ask LLM to extract emails
    # Simulated response from LLM
    extracted_emails = re.findall(r'[\w\.-]+@[\w\.-]+', email_content)
    valid_emails = [email for email in extracted_emails if is_valid_email(email)]
    return valid_emails

# File paths
input_file_path = os.path.join('/data/', 'emails.txt')
output_file_path = os.path.join('/data/', 'valid_emails.txt')

# Ensure input file exists or create it
if not os.path.isfile(input_file_path):
    with open(input_file_path, 'w') as f:
        f.write('')  # Create a blank file if it doesn't exist

# Read email content from the input file
with open(input_file_path, 'r') as f:
    email_content = f.read()

# Extract valid emails
valid_emails = extract_emails(email_content)

# Write valid emails to the output file
with open(output_file_path, 'w') as f:
    for email in valid_emails:
        f.write(email + '\n')