def atm():
    print("Welcome to our ATM")
    pin = "1234"
    balance=1000
    while True:
        entered_pin=input("Please enter your 4-digit PIN or type 'exit to quite:")
        if entered_pin == pin:
            print("\n 1.Check Balance")
            print("\n 2.Withdraw")
            print("\n 3.Deposit Money")
            print("\n 4.Change PIN")
            print("\n 5.Exit")

            choice = input("\n What would you like to do?Enter the number:")
            if choice == '1':
                print ("\n Your Current is $(Balance)")

            elif choice =='2':
                amount = float(input("\n Enter amount to withdrow:$"))
                if amount > balance:
                    print("Insufficient balance")
                else:
                    balance -=amount
                    print(f"\n ${amount} has been withdrawn.Remaining Balance: ${balance}\n")

            elif choice =='3':
                float(input("\n Enter amount to deposit:$"))
                balance +=amount
                print(f"\n ${amount} has been withdrawn.Remaining Balance: ${balance}\n")

            elif choice =='4':
                new_pin = input("\n Enter new 4 digit PIN:")
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin=new_pin
                    print("\n Pin Change Successfully!")
                else:
                    ("\n Invalid PIN Formet.Pin must be in 4 digit")
            elif choice =='5':
                print("\n Thank you for using ATM!Good Bye")
                break
        elif entered_pin.lower()=="exit":
            print("\n Exit the ATM")
            break
        else:
            print("\n Incorrect PIN,Please try again \n")
atm()