
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

# Constants
DATA_DIR = Path('/data/')

def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def extract_emails(file_path):
    email_set = set()
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Assuming we have a function to get the email content from LLM
            response = requests.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', json={"messages":[{"role":"user","content":"Extract the sender/recipient's email address from the following text : " + content}]}, headers={'Authorization': f'Bearer {os.getenv("AIPROXY_TOKEN")}'})
            extracted_emails = response.json()["choices"][0]["message"]["content"].split()  # Assuming space-separated emails
            for email in extracted_emails:
                if is_valid_email(email):
                    email_set.add(email)
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            pass  # Create the file if it does not exist
    except Exception as e:
        print(f"Error processing file: {e}")

    return email_set

def save_emails_to_file(emails, output_file):
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

# Main execution
input_file = DATA_DIR / 'emails.txt'
output_file = DATA_DIR / 'valid_emails.txt'
valid_emails = extract_emails(input_file)
save_emails_to_file(valid_emails, output_file)