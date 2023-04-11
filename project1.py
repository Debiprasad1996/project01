Total_Seats = 150
Recliner_seats = 20
Normal_seats = 130
Normal_seat_price = 250
recliner_seat_price = 400
while True:
    print("WELCOME TO ION-DIGITAL THEATRE")
    print('''
       PRICE LIST
       NORMAL SEAT=250
       RECLINER SEAT=380
       POP_CORN=100
       COLD_DRINK=50
       ''')
    print("Avalible seats:-", Total_Seats)
    print("Avalible Normal seats:-", Normal_seats)
    print("Avalible Recliner seats:-", Recliner_seats)
    total_price=0
    pop_corn = 100
    cold_drink = 50
    if Total_Seats == 0:
        print("HOUSE FULL")
        break
    name = input("Enter your name:--")
    if Normal_seats == 0:
        print("Normal Seat Not Avalible")
        customer = input("Do you want Recliner seat[yes|no]:")
        if customer == "yes":
            print("select 2 for Recliner seat")
        else:
            continue
    elif Recliner_seats == 0:
        print("Recliner Seat Not Avalible")
        customer = input("Do you want Normal seat[yes|no]:")
        if customer == "yes":
            print("Select 1 for Normal Seat")
        else:
            continue
    print('''
        select your seat Type
            1 Normal seat
            2 Recliner seat
            ''')
    userchoice = int(input("Enter your seat type:--"))
    if userchoice == 1:
        choice = "250"
        print("you select Normal seat")
        quantity = int(input("How many seats you want:--"))
        if quantity> Normal_seats:
            print("sorry that much seat you want not avalible")
            continue
        total_price = Normal_seat_price * quantity
        Normal_seats -= quantity
        Total_Seats -= quantity
        uc = input("Do you want some extra item (popcorn,cold_drink),[yes|no]:--")
        if uc == "yes":
            print('''
        select your item
          1 popcorn
          2 cold_drink
                ''')
            add_item = int(input("plz select your item:--"))
            if add_item == 1:
                choice1 = "100"
                print("you select popcorn")
                quantity1 = int(input("How many pop_corn packet you want:-- "))
                pop_corn *= quantity1
                total_price += pop_corn
            else:
                choice1 = "50"
                print("you select cold_drink")
                quantity1 = int(input("How many cold drink bottle you want:-- "))
                cold_drink*= quantity1
                total_price += cold_drink
    elif userchoice == 2:
        choice = "400"
        print("you select Recliner seat")
        quantity = int(input("How many seats you want:--"))
        if quantity> Recliner_seats:
            print("sorry that much seat you want not avalible")
            continue
        total_price = recliner_seat_price * quantity
        Recliner_seats -= quantity
        Total_Seats -= quantity
        uc = input("Do you want some extra item (popcorn,cold_drink),[yes|no]:--")
        if uc == "yes":
            print('''
                  select your item
                  1 popcorn
                  2 cold_drink
                  ''')
            add_item = int(input("plz select your item:--"))
            if add_item == 1:
                choice1 = "100"
                print("you select popcorn")
                quantity1 = int(input("How many pop_corn packet you want:-- "))
                pop_corn *= quantity1
                total_price += pop_corn
            else:
                choice1 = "50"
                print("you select cold_drink")
                quantity1 = int(input("How many cold_drink bottle you want:-- "))
                cold_drink *= quantity1
                total_price += cold_drink
    if uc == "yes":
        print(name, "your bill is:--")
        print("-" * 55)
        print("Items", " " * 20, "price", " " * 10, "Quantity", " " * 20)
        print("Ticket", " " * 19, choice, " " * 15, quantity, " " * 28)
        print("Extra", " " * 20, choice1, " " * 15, quantity1, " " * 28)
        print("-" * 55)
        print("Total price =", " " * 30, total_price)
        print("-" * 55)
    else:
        print(name, "your bill is:--")
        print("-" * 55)
        print("Items", " " * 20, "price", " " * 10, "Quantity", " " * 20)
        print("Ticket", " " * 19, choice, " " * 15, quantity, " " * 28)
        print("-" * 55)
        print("Total price =", " " * 30, total_price)
        print("-" * 55)
    customer = input("Do you want to another customer[yes|no]:-")
    if customer == "yes":
        continue
    else:
        print("show time is over")
        break




