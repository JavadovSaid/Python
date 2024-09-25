

def gather(a, b):
    answer =a+b
    print(f"a + b = {answer}")
def subtraction(a, b):
    answer =a-b
    print(f"a - b = {answer}")
def multiplication(a, b):
    answer = a*b
    print(f"a * b = {answer}")
def division(a, b):
    answer = a/b
    print(f" a / b = {answer}")
print("A.Gathering")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")
print("E.Quit")
def running():
    while True:
        choice = input('Enter your input: ').upper()
        if choice == 'A':
            print("A.Gathering")
            a = int(input("Enter that what is a: "))
            b = int(input("Enter that what is b: "))
            gather(a, b)
        elif choice == 'B':
            print("B.Subtraction")
            try:
                try:
                    a = int(input("Enter that what is a: "))
                    b = int(input("Enter that what is b: "))
                except ValueError:
                    print("Invalid,only use numbers!")
                    continue
            except ValueError:
                print("Invalid,only use numbers!")
                continue
            subtraction(a, b)
        elif choice == 'C':
            print("C.Multiplication")
            try:
                a = int(input("Enter that what is a: "))
                b = int(input("Enter that what is b: "))
            except ValueError:
                print("Invalid,only use numbers!")
                continue
            multiplication(a, b)
        elif choice == 'D':
            print("D.Division")
            try:
                a = int(input("Enter that what is a: "))
                b = int(input("Enter that what is b: "))
            except ValueError:
                print("Invalid,only use numbers!")
                continue
            if b == 0:
                print("b can't be 0 while you wanna divide it!")
                continue
            division(a, b)
        elif choice=='E':
            quit()
running()