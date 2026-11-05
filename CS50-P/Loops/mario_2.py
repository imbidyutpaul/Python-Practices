def main():
    height = inp_height()
    width = inp_width()
    print_brick(height, width)

def inp_height():
    return int(input("What's the height? "))

def inp_width():
    return int(input("What's the width? "))

def print_brick(height, width):
    for i in range(height):
        print("#" * width)

main()