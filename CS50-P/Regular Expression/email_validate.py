#check email is valid or not
import re #re for understanding patterns in input

email = input("What's your email? ").strip()    

if re.search(r"^\w+@\w+\.[a-zA-Z]$", email) and email.count("@") == 1: #\. = real .  #you can write \w as [A-Za-z0-9_]
  print("Valid!")
else:
  print("Invalid!")



