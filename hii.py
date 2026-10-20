# with open("fille.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("fille.txt", "w") as file:
#     file.write("This is a new line of text.\n")
#     file.write("This is another line of text.\n")

# with open("fille.txt", "a") as file:
#     file.write("This line will be appended to the file.\n")

# import csv , json 




data = [
    {"name": "Alice", "age": 30, "city": "New York  "},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}   ]

import json
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)