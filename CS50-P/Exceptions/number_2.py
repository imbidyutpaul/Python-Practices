#if user input a string show error, so we create this
for i in range(3):
  try:
    x = int (input("Enter X: "))
  except ValueError:
    print("Please enter integer")
  else:
    print ("X is:", x)
else:
  print("Too many invalid attempts")
#when 3 attemps complete it's over 