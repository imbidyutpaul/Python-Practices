class Student:
   def __init__(self, name, house):
      if not name:
        raise ValueError("Missing Name!")
      if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        raise ValueError("Invalid House!")
      self.name = name
      self.house = house

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  #student = Student()
  #student.name = input("Name: ").title()
  #student.house = input("House: ").title()    #or do this
  name = input("Name: ").title()
  house = input("House: ").title()
  return Student(name, house)
  
  
if __name__ == "__main__":
  main()

