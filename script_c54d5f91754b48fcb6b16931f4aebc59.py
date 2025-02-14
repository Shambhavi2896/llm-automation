
# /// script
# requires-python = ">=3.11"
# dependencies = [
# "os",
# "datetime",
# ]
# ///
import os
import datetime

# Define the input and output file paths
input_file_path = os.path.join('/data/', 'dates.txt')
output_file_path = os.path.join('/data/', 'wednesday_count.txt')

# Initialize a counter for Wednesdays
wednesday_count = 0

# Read the input file and count Wednesdays
try:
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            for date_format in [
                '%Y-%m-%d',
                '%d-%b-%Y',
                '%Y/%m/%d %H:%M:%S',
                '%Y/%m/%d',
                '%b %d, %Y',
                '%d %B %Y',
                '%B %d, %Y',
                '%d.%m.%Y',
                '%m-%d-%Y',
                '%A, %B %d, %Y',
                '%I:%M %p, %d-%b-%Y'
            ]:
                try:
                    date_obj = datetime.datetime.strptime(line, date_format)
                    if date_obj.weekday() == 2:  # 2 represents Wednesday
                        wednesday_count += 1
                    break  # Exit the for loop if a valid date is found
                except ValueError:
                    continue  # Skip to the next format if the current one fails
except FileNotFoundError:
    with open(input_file_path, 'w') as file:
        pass  # Create a blank file if it does not exist

# Write the count of Wednesdays to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))