def show_balance():
    pass
def withdraw():
    pass
def deposit():
    pass

balance = 0
is_running = True
while is_running:
    print("---Banking program---")
    print("1.Your balance: ")
    print("2.Your withdraw: ")
    print("3.Banking: ")
    print("quit: ")
    input_of_user = input("What do you wanna choose (1-4) ")

    if input_of_user =='1':
        show_balance()
    elif input_of_user=='2':
        withdraw()
    elif input_of_user =='3':
        deposit()
    elif input_of_user == '4':
        is_running =False
    else:
        print("That wasn't valid option.")
print("Thank you have a great day!")




