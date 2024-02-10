import re

# Sample text containing jokes
text = "Why did the chicken cross the road? Because it wanted to get to the other side."

# Regular expression pattern
pattern = r"Why did the .* ? Because.*"

# Search for the pattern in the text
match = re.search(pattern, text)

# Check if a match is found
if match:
    print("Joke found:", match.group())
else:
    print("No joke found.")
