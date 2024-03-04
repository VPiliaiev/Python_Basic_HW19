import json
import csv
import random

with open('text.json') as file:
    data = json.load(file)

with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['ID', 'Name', 'Age', 'Phone'])

    for key, value in data.items():
        phone_number = ''
        for i in range(10):
            phone_number += str(random.randint(0, 9))
        writer.writerow([key, value[0], value[1], phone_number])
