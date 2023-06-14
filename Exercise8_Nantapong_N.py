username_input = input("username : ")
password_input = input("password : ")

if username_input == "chevfy" and password_input == "2548" :
    print ("Login Success. Welcome to Gameshop")
    print("-----------------------------------")
    print("1. Final Fantasy XVI : 1000 THB")
    print("2. The sims 4 : 4000 THB")
    print("3. Call of duty Modern Warfare 2 : 2399 THB")
    print("4. Watch dog 3 : 400 THB" )
    print("5. Grand Theft Autyo VII : 100THB ")
    print("-----------------------------------")
    select = int(input("Choose : "))
    if select == 1 :
        amount = int(input("amount : "))
        result = 1000 * amount
        print("Total : ", result , "THB")
    elif select == 2 :
        amount = int(input("amount : "))
        result = 4000 * amount
        print("Total : ", result , "THB")
    elif select == 3:
        amount = int(input("amount : "))
        result = 2399 * amount
        print("Total : ", result, "THB")
    elif select == 4:
        amount = int(input("amount : "))
        result = 400 * amount
        print("Total : ", result, "THB")
    elif select == 5:
        amount = int(input("amount : "))
        result = 100 * amount
        print("Total : ", result, "THB")
    else :
        print("Undefined")
else :
    print("Username or Password wrong ! ")