import re

if __name__ == "__main__":
    test_string = input("Enter your data: ")
    patterns = r'ISBN \d{3}-\d-\d{3}-\d{5}-\d'
    matches = re.findall(patterns, test_string)
    print('Search results: ', matches)
