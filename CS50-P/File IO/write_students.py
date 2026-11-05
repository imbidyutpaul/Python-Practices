import csv

name = input("What's your name? ")
home = input("Where's your home? ")
with open("students_home_2.csv", "a", newline="") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "home"]) #or you can use csv.writer
  writer.writerow({"name":name, "home":home})