def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False

# or use this 
# def is_even(n):
# return True if n % 2 == 0 else False

# or use this
# def is_even(n):
# return n % 2 == 0

main()

