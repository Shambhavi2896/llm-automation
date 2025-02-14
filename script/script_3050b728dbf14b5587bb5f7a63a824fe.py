
# /// script
# requires-python = ">=3.11"
# dependencies = [
# "os",
# "re",
# "json",
# "requests",
# ]
# ///
import os
import re
import json
import requests

# Ensure the output directory exists
output_dir = '/data/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to validate email format using regex
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

# Function to extract sender/recipient email addresses from text
def extract_emails(email_content):
    prompt = f'Extract the sender/recipient's email address from the following text: {email_content} and return only the sender/recipient's email address, nothing else'
    # Here, we would normally call the LLM API to get the response
    # For demonstration, let's assume the following function sends a request and gets the email
    response = requests.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', json={'model': 'GPT-4o-Mini', 'messages': [{'role': 'user', 'content': prompt}]})
    extracted_email = response.json()['choices'][0]['message']['content']
    return extracted_email

# Main function to process the email file
def process_email_file(input_file):
    input_path = os.path.join(output_dir, input_file)
    output_file = 'valid_emails.txt'
    output_path = os.path.join(output_dir, output_file)

    try:
        with open(input_path, 'r') as file:
            email_content = file.read()
            extracted_email = extract_emails(email_content)
            if is_valid_email(extracted_email):
                with open(output_path, 'a') as out_file:
                    out_file.write(extracted_email + '\n')
            else:
                print(f'Invalid email extracted: {extracted_email}')  # Log invalid email
    except FileNotFoundError:
        print(f'Error: The file {input_file} does not exist. Creating a blank file.')
        with open(input_path, 'w') as file:
            file.write('')  # Create a blank file
    except Exception as e:
        print(f'An error occurred: {e}')  # Handle other exceptions gracefully

# Example usage
process_email_file('emails.txt')