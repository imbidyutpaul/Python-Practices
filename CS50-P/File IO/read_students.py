with open("students.csv") as file:
  for line in sorted(file):
    name, house = line.rstrip().split(",")
    print(f"{name.title()} is in {house.title()}") #or use row[0] for first and row[1] for second