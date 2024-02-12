import re

# Define the pattern
episode_title_pattern = r".+ S\d{2}E\d{2}:.+"

# Test strings
test_strings = [
    "Friends S01E01: The One Where Monica Gets a Roommate",
    "Breaking Bad S05E14: Ozymandias",
    "Game of Thrones S08E03: The Long Night",
    "The Office S02E12: The Injury",
    "Stranger Things S03E08: The Battle of Starcourt",
    "The Mandalorian S02E06: The Tragedy",
    "Sherlock S01E01: A Study in Pink",
    "The Crown S04E10: War",
    "Black Mirror S03E01: Nosedive",
    "The Simpsons S06E07: Bart's Girlfriend"
]

# Test the pattern
for test_string in test_strings:
    if re.match(episode_title_pattern, test_string):
        print(f"{test_string}: matches the pattern")
    else:
        print(f"{test_string}: does not match the pattern")
