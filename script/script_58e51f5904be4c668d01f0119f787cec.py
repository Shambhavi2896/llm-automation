
# /// script
# requires-python = ">=3.11"
# dependencies = [
# "os",
# "datetime",
# ]
# ///
import os
from datetime import datetime

# Define the input and output file paths
input_file = os.path.join('/data', 'dates.txt')
out_file = os.path.join('/data', 'dates-wednesdays.txt')

# Initialize a counter for Wednesdays
wednesday_count = 0

# Read the input file and count Wednesdays
try:
    with open(input_file, 'r') as f:
        for line in f:
            date_str = line.strip()
            # Try to parse the date with multiple formats
            for fmt in ("%Y-%m-%d", "%d-%b-%Y", "%Y/%m/%d %H:%M:%S", "%Y/%m/%d", "%b %d, %Y", "%d %B %Y", "%B %d, %Y", "%d.%m.%Y", "%m-%d-%Y", "%A, %B %d, %Y", "%I:%M %p, %d-%b-%Y"):
                try:
                    date_obj = datetime.strptime(date_str, fmt)
                    if date_obj.weekday() == 2:  # 2 represents Wednesday
                        wednesday_count += 1
                    break  # Exit the loop if date is successfully parsed
                except ValueError:
                    continue  # Try the next format
except FileNotFoundError:
    with open(input_file, 'w') as f:
        pass  # Create the file if it does not exist

# Write the count of Wednesdays to the output file
with open(out_file, 'w') as f:
    f.write(str(wednesday_count))