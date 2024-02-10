import re

if __name__ == "__main__":
    test_string = input("Enter your data: ") # Enter User Data FRom Input
    patterns = r'\[Verse\s+\d+\].+'
    result = re.findall(patterns, test_string)
    print('Search results: ', results)
