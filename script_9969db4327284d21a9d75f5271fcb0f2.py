
# /// script
# requires-python = ">=3.11"
# dependencies = [
# "os",
# "datetime",
# "collections",
# ]
# ///
import os
from datetime import datetime
from collections import Counter

# Define the path to the input file and output file
input_file_path = os.path.join('/data/', 'dates.txt')
out_file_path = os.path.join('/data/', 'wednesday_count.txt')

# Initialize a counter for Wednesdays
wednesday_count = 0

# Read the input file and count Wednesdays
try:
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            # Try different date formats
            for fmt in ['%Y-%m-%d', '%d-%b-%Y', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d',
                        '%b %d, %Y', '%d %B %Y', '%B %d, %Y', '%d.%m.%Y',
                        '%m-%d-%Y', '%A, %B %d, %Y', '%I:%M %p, %d-%b-%Y']:
                try:
                    date_obj = datetime.strptime(line, fmt)
                    if date_obj.weekday() == 2:  # 2 corresponds to Wednesday
                        wednesday_count += 1
                    break  # Exit the loop if date is parsed successfully
                except ValueError:
                    continue  # Try the next format
except FileNotFoundError:
    # Create the input file if it doesn't exist
    with open(input_file_path, 'w') as file:
        pass  # Create a blank file

# Write the count of Wednesdays to the output file
with open(out_file_path, 'w') as out_file:
    out_file.write(f'{wednesday_count}')