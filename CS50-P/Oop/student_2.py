#solve student.py problem with tuple
def main():
  student = get_student()
  if student['name'] == "Padma":
      student['house'] = "Ravenclaw"
  print(f"{student['name']} from {student['house']}")

def get_student():
  student = {}
  student["name"] = input("Name: ").title()
  student["house"] = input("House: ").title()
  return student

  #name = input("Name: ").title()
 # house = input("House: ").title()
 # return [name, house] #use() for tuple but tuple was not mutable/not changable. but if you use [] list it's mutable

if __name__ == "__main__":
  main()