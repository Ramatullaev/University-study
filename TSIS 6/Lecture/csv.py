
import csv

# students = []

# with open("students.csv", "r") as file:
#     for line in file:
#         name, faculty = line.rstrip().split(",")
#         students.append({"name":name, "faculty": faculty})

# for student in faculty:
#     print(f"{student["name"]} is in {student["faculty"]}")

name = input("What's your name? ")
address = input("What's your address?" )
with open("student.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "address"])
    writer = writerow({"name": name , "address": address})

