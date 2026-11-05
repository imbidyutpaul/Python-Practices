with open("names.txt", "r") as read:
#  lines = read.readlines() or you can do this
  for line in sorted(read, reverse=True): #sorted() for sort from A to Z, reverse=True is for reverse the names from Z to A
    print("hello", line.rstrip().title()) #.rstrip() = end="" same work