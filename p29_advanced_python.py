"""
Advanced Python excercise
you get all the instructions by unzipping the file named "unzip_me_for_instructions.zip"

Instructions after extraction:
Good work on unzipping the file!
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-#### 
Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
Good luck!
"""

import shutil
import re
import os

shutil.unpack_archive('unzip_me_for_instructions.zip', '', 'zip')

with open(f"extracted_content{os.sep}Instructions.txt") as f:
    content = f.read()
    print("\nInstructions\n")
    print(content)

PATTERN = r'\d{3}-\d{3}-\d{4}'

def search_pattern(file, regex):
    """ Searches for the regex in the given file """
    current_file = open(file, 'r')
    text = current_file.read()
    current_file.close()

    search = re.search(regex, text)
    if search:
        return search

current_directory = os.getcwd()
for path, directory, files in os.walk(current_directory + os.sep + 'extracted_content'):
    for f in files:
        search_path = path + os.sep + f
        result = search_pattern(search_path, PATTERN)
        if result is not None:
            print("\nFound the number", result.group())
            break
