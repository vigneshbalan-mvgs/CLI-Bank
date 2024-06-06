
def show_balance():
    print(f"your balance is ${balance:.2f}")


def deposit():
    amont = float(input('Enter an amont to be deposited: '))

    if amont < 0:
        print("that's not a valid amount")
        return 0
    else:
        return amont


def withdraw():
    amont = float(input("Enter amont to be withdrawn: "))

    if amont > balance:
        print("Insufficient funds")
        return 0
    elif amont < 0:
        print("Amount Must be greater than 0")
        return 0
    else:
        return amont


balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1.show_balance")
    print("2. Deposit")
    print("3. withdraw")
    print("4. Exit")
    choise = input("enter your choise (1-4):")

    if choise == '1':
        show_balance()
    elif choise == '2':
        balance += deposit()
    elif choise == '3':
        balance -= withdraw()
    elif choise == '4':
        is_running = False
    else:
        print('that is not a option here bro ! ')

print('Thnak you! have a nice day')
