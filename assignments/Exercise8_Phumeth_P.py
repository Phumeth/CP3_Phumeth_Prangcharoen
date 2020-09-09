userName = input("Username :")
passWord = input("Password :")
if userName == "Gundam" and passWord == "destiny":
    print("Welcome to iModelShop")
    print("________iModelShop________")
    print("1. MG Barbatos       1620 THB")
    print("2. RG Astray RED      900 THB")
    print("3. SD Cross           500 THB")
    print("4. HD RX-78           780 THB")
    print("5. RG Wing Zero      1060 THB")
    userSelected = int(input("Which model do you want? (1-5) : "))
    number = int(input("Number : "))
    if userSelected == 1:
        price = 1620
    elif userSelected == 2:
        price = 900
    elif userSelected == 3:
        price = 500
    elif userSelected == 4:
        price = 780
    elif userSelected == 5:
        price = 1060
    else:
        print("Incorrect model choose")
    result = number * price
    print("Price = ", result, "THB")
else:
    print("Username or password incorrect")