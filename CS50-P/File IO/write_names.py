names = []

for i in range(3):
  names.append(input("What's your name? "))

for name in sorted(names):
  print(f"hello, {name}")

with open("names.txt", "a") as file:
  for name in sorted(names):
   file.write(name + "\n")
file.close()