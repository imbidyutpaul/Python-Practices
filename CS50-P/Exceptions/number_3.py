#if user input a string show error, so we create this, and add a loop when show error for extra
def main():
  y = get_int("Enter X: ")
  print ("X is:", y)

def get_int(anything):
  while True:
    try:
      x = int (input(anything))
      return x
    except ValueError:
      pass #it pass error and not show any comment just new session was open to enter int
  
main()