def main():
    input_size =int(input("What's the size: "))
    print_square(input_size)

def print_square(size):
    #for each row in square
    for i in range(size):
          #for each brick in row
         # for j in range(size):
               #print brick
              # print("#", end="")
         # print() or use this
      print("#" * size)

main()