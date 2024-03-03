import json

input_data = {123456: ('Bob', 18),
              654321: ('Tom', 20),
              123654: ('Alex', 17),
              321456: ('Sem', 22),
              654456: ('Drake', 33),
              125634: ('James', 34)}
with open('text.json', 'w') as file:
    json.dump(input_data, file)

