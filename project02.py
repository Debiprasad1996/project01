print("WELCOME TO CENTRAL LIBRARY")
while True:
    user_name=input("Enter your user_name:-").strip()
    password=input("Enter your password(alphanumeric):-").strip()
    if user_name.lower()=="debiprasad" and password=="debi123":
        print("Sucessfully login")
    else:
        print("Plz enter valid username and password")
        continue
    books = {"python": 20, "java": 10, "c++": 5,"math": 10}
    Total_book=0
    for i in books.values():
        Total_book+=i
    borrow_book={}
    ret_book={}
    while True:
        print("Total Avalible Book:", Total_book)
        print('''
        press 1 for add_book
        press 2 for stock details
        press 3 for borrow_book
        press 4 for return_book
        press 5 for exit
        ''')
        choice=input("Enter your choice:--").strip()
        if choice=="1":
            book_name=input("Enter your book:-").strip()
            quantity=int(input("How many book you add:-"))
            if book_name in books:
                books[book_name]+=quantity
                Total_book += quantity
                continue
            books[book_name]=quantity
            Total_book+=quantity
            print(books)
            print("Book added successfully")
        elif choice=="2":
            print("STOCK DETAILS")
            print('''
            press 1 for avalible book details
            press 2 for borrow book details
            press 3 for return book details
            ''')
            uc=input("Enter above option:-").strip()
            if uc=="1":
                print("Avalible Book")
                print("Book Name", "\t", "Quantity")
                for k, v in books.items():
                    print(k, "\t\t", v)
            elif uc=="2":
                print("BORROW BOOK DETAILS")
                print(borrow_book)
            elif uc=="3":
                print("RETURN BOOK DETAILS")
                print(ret_book)
            else:
                print("plz enter valid input")
        elif choice=="3":
            if Total_book==0:
                print("you cann't borrow library is Empty")
                continue
            print("Avalible Book")
            print("Book Name", "\t", "Quantity")
            for k, v in books.items():
                print(k, "\t\t", v)
            student_name=input("Enter your name:-").strip()
            if student_name in borrow_book:
                print(f"{student_name} you already borroow book ")
                continue
            b_borrow=input("which book you want:-").strip()
            b_quantity = int(input("How many book you want:-"))
            if books[b_borrow]==0:
                print(f"{b_borrow} book is out of stock")
                continue
            if b_quantity>books[b_borrow]:
                print("sorry that much quantity you want not avalible")
                continue
            books[b_borrow] -= b_quantity
            Total_book-=b_quantity
            borrow_book[student_name]={b_borrow:b_quantity}
            print("sucessfully borrowed")
        elif choice=="4":
            if borrow_book=={}:
                print("First borrow book then return")
                continue
            student_name=input("Enter your name:-").strip()
            b_return=input("Enter your return book name:-").strip()
            if student_name in borrow_book:
                pass
            else:
                print("enter valid name")
                continue
            if b_return not in borrow_book[student_name]:
                print("plz enter valid book name")
                continue
            r_quantity=int(input("Enter return book quantity:-"))
            if r_quantity > borrow_book[student_name][b_return] :
                print("return quantity is more than your borrow quantity")
                continue
            elif r_quantity < borrow_book[student_name][b_return]:
                print("return quantity is less than your borrow quantity")
                continue
            ret_book[student_name]={b_return:r_quantity}    #add detail of return student
            books[b_return]+=r_quantity
            print("sucessfully return")
            if borrow_book[student_name][b_return]==ret_book[student_name][b_return]:  #delete from borrow_book details if student return book
                del borrow_book[student_name]
            Total_book += r_quantity
        elif choice=="5":
            print("LIBRARY CLOSED")
            break
        else:
            print("plz enter valid option")
            continue
    if choice=="5":
        break

