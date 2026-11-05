def main():
    x = int(input("What's X: "))
    print("X squared is:", square(x))

def square(n):
    return n*n
#or use return n**2
#or use pow(n,2)
main()