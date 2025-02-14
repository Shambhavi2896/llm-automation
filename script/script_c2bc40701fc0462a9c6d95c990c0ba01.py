
# /// script
# requires-python = ">=3.11"
# dependencies = [
# "os",
# "datetime",
# ]
# ///
import os
from datetime import datetime

input_file_path = os.path.join('/data/', 'dates.txt')
output_file_path = os.path.join('/data/', 'wednesday_count.txt')

def count_wednesdays(file_path):
    wednesday_count = 0
    date_formats = [
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
    ]
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                for fmt in date_formats:
                    try:
                        date = datetime.strptime(line, fmt)
                        if date.weekday() == 2:  # Wednesday
                            wednesday_count += 1
                        break
                    except ValueError:
                        continue
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            pass  # Create the file if it does not exist
    return wednesday_count

wednesday_count = count_wednesdays(input_file_path)
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))