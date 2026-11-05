def main():
    height = inp_height()
    width = inp_width()
    print_column(height)
    print_row(width)

def inp_height():
    n = int(input("What's the height? "))
    return n    

def inp_width():
    n = int(input("What's the width? "))
    return n

def print_column(height):
    for i in range(height):
        print("#")

def print_row(width):
    # for i in range(width):
     #   print("?", end="") or use this
     print("?" * width)

main()
