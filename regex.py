import re

if __name__ == "__main__":
    test_string = input("Enter your data: ")
    list_of_patterns = [r'.+\s\(\d{4}\)', r'\[Verse\s\d+\].+']
    list_of_matches = []
    for pattern in list_of_patterns:
        list_of_matches.append(re.findall(pattern, test_string))
    print('Search results: ', list_of_matches)
