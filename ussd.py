ussdCode = "*123#"
print("Welcome to MTN self-service center")
# print(f"Enter {ussdCode}")
ussd = input(f"dial {ussdCode}: ")
# CheckBalance = "1"
# BuyAirtime = "2"
# BuyData = "3"
# shareData = "4"
# print(f"Buy airtime\nEnter the amount")
# amount = int(input("Enter the amount of airtime: "))
# print("Your airtime purchase of #5000 was successful\nTHANK YOU FOR CHOOSING US")


while True:
    if ussd == ussdCode:
        print("Choose an option")
    # print("Enter", ussdCode)
    else:
        print(f"Incorrect entry. dial {ussdCode}")
        break
    print("MENU\n1. Check Balance\n2. Buy Airtime\n3. Buy Data\n4. Share Data\nChoose an option.")
    balance = 3300
    Data_Bal = 5000
    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Your balance is N{balance}")
    elif choice == "2":
        amount = int(input("Enter the amount of airtime you want to buy: "))
        balance += amount
        print(f"Your total airtime balance is N{balance}")
    elif choice == "3":
        amount = int(input("Enter the amount of airtime you want to buy: "))
        Data_Bal += amount
        print(f"Your data purchase was successful. Your new data balance is {Data_Bal}MB")
    elif choice == "4":
        amount = int(input("Enter the amount of data you want to share: "))
        if amount <= Data_Bal:
            Data_Bal -= amount
            print(f"You have share {amount}.\nYour data balance emains {Data_Bal}MB")
        else: 
            print("Insufficient data balance. Buy data and try again.")
        break
    else:
        print("Invalid option. Input the right number")




      