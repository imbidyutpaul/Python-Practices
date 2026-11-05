#if user input a string show error, so we create this, and add a loop when show error for extra
def main():
  y = get_int()
  print ("X is:", y)

def get_int():
  while True:
    try:
      x = int (input("Enter X: "))
      return x
    except ValueError:
      print("Please enter integer")
  
main()