import csv
import os

BASE_DIR = os.path.dirname(__file__)

print("CREATE TABLE sowpods (word VARCHAR UNIQUE)")

with open(os.path.join(BASE_DIR, "sowpods.txt")) as file:
    reader = csv.reader(file)
    for row in reader:
        word = row[0]
        print(f"INSERT INTO sowpods (word) VALUES ({word})")

print("COMMIT")
