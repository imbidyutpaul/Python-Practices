def main():
    name = input("What,s your name: ").title().strip()
    hello(name)

def hello(to):
    print("hello,", to)

main()

