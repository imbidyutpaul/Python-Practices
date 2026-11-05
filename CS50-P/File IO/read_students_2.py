with open("students.csv") as file:

  for line in sorted(
    file, 
         key=lambda line: 
         (line.rstrip().split(",")[1], 
          line.rstrip().split(",")[0])): 
  #lambda was a keyword to crate function without giving function name
    
    name, house = line.rstrip().split(",")
    
    print(f"{name.title()} is in {house.title()}") 