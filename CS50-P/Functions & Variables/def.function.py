#at first we need to define what is hello()
def hell(to="there"):
    print ("hello,", to, end=" ") 

name = input("What,s your name: ").title().strip()
#print name with hello in same line
hell()
print(name)
#print name only
hell(name)