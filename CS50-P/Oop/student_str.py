class Student:
  def __init__(self, name, house, patronus):
    if not name:
      raise ValueError("Missing Name!")
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid House!")
    self.name = name
    self.house = house
    self.patronus = patronus
  def __str__(self):
    return f"{self.name} from {self.house}"
  
  def charm(self):
    match self.patronus:
      case "Stag":
        return "🦌"
      case "Otter":
        return "🦦"
      case "Jack Russell Terrier":
        return "🐶"
      case _:
        return "🪄"

def main():
  student = get_student()
  print("Expecto Patronum!")
  print(student.charm())
  #print(f"{student.name} from {student.house}")

def get_student():
  name = input("Name: ").title()
  house = input("House: ").title()
  patronus = input("Patronus: ").title()
  return Student(name, house, patronus)
  
  
if __name__ == "__main__":
  main()

