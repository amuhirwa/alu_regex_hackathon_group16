import re

# Test string
test_string = """Dates:
1-MAY-2024
25-Dec-2023
14-Feb-2024
31-Oct-2022
02-Mar-2025
20-Sep-2021"""

# Regex pattern to match dates
date_pattern = re.compile(r'\d{2}-[a-zA-z]{3}-\d{4}')

# Test to see if pattern matches them correctly
if len(date_pattern.findall(test_string)) != 0:
    print(f"Matches: {date_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")