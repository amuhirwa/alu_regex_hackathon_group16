import re

if __name__ == "__main__":
    test_string = input("Enter your data: ") 
    patterns = r"[A-Za-z\s]+ S\d{2}E\d{2}: [A-Za-z\s]+"
    matches = re.findall(patterns, test_string)
    if matches:
        print('Search results: ', matches)
    else:
        print('No match found!')
