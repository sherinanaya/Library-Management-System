#Library Management Software
#Successfully completed

import sys
import shutil
import os
from datetime import datetime

#User Verification
def read_user_credentials(credentials):
    credentials = {}
    with open("/Users/apple/Desktop/Sherin/VIT/Mini Project- Libraray Managament/Users.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(',')
            credentials[username] = password
    return credentials


def login():
    user_credentials = read_user_credentials("/Users/apple/Desktop/Sherin/VIT/Mini Project- Libraray Managament/Users.txt")

    # Get username & password
    print()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print()
    # Check if the entered credentials are correct
    if username in user_credentials and password == user_credentials[username]:
        return (username)
    else:
        return 0
    
def load_books():
    books = []
    with open("/Users/apple/Desktop/Sherin/VIT/Mini Project- Libraray Managament/Bookshelf.txt", "r") as file:
        for line in file:
            book_info = line.strip().split("\t")
            books.append(book_info)
        #print(books)
    file.close()
    return books
    
#Main Menu
def main_page(books, username):
    
    print()
    print("1.List")
    print("2.Lend")
    print("3.Return")
    print("4.Search")
    print("5.Exit")
    print()
    choice = int(input("Enter your choice: "))
    
    print() 
    if choice == 1: 
        listt()
        main_page(books, username)
    elif choice == 2: 
        lend(books, username)
        main_page(books, username)
    elif choice == 3: 
        returnn(books, username)
        main_page(books, username)
    elif choice == 4: 
        search_menu(books, username)
    elif choice == 5:   
        print("Exiting program\n")
        sys.exit()
    else:   
        print("Invalid input choice\n")
        
#Listing the books function
def listt():
    books = load_books()
        
    #formatting heading
    print(f"{'Title' : ^21}{'Author' : ^32}{'Published Date' : ^20}{'Available to Lend?' : ^15}") 
    count = 0
        
    for book in books:
        count += 1
        bkstr = ','.join(map(str, book))
        items = bkstr.split(",")
        #formatting contents
        print(count, f"{items[0] : <30}{items[1] : <22}{items[2] : ^20}{items[3] : ^10}")
     
#Lending the book function            
def lend(books, username):

    dest = "/Users/apple/Desktop/Sherin/VIT/Mini Project- Libraray Managament/Bookshelf.txt"   #source file
    src = "/Users/apple/Desktop/Sherin/VIT/Mini Project- Libraray Managament/Output.txt"      #temp file    
    listt()
    
    #getting user input for book
    bk_no = int(input("\nEnter the book number to lend: "))
    
    if (bk_no < 1):
        print("\nInput Error: Book number below range!\n")
        return;
        
    fin = open(dest, "r")
    fout = open(src, "w")
        
    Lines = fin.readlines()
    count = 0
    bk_count = 0
        
    # Read each line in the file
    for line in Lines:
        count += 1
        book = line.strip().split(',')
        
        if book[4] == username:
            bk_count += 1
        
        if count == bk_no:
            if bk_count > 1:
                print("\nYou have already borrowed 2 books. Please return & try again!\n")
            else:
                if book[3] == "Yes":
                    book[3] = "No"       #changing availability
                    book[4] = username   #updating user
                    print("\nBook is successfully borrowed!\n")
                else:
                    print("\nBook is already lent by an another user\n")
                    
        # updating in main file            
        book_str = "{},{},{},{},{}\n".format(*book)
        fout.write(book_str)
        
    if (bk_no > count):
        print("\nInput Error: Book number exceeded range!\n")
        return; 
                
    fin.close() 
    fout.close()  
    
    #copy temp fie to source file
    shutil.copy(src, dest)
    #remove temp file
    os.remove(src)    
        
    
#Returning the book function       
def returnn(books, username):
    
    dest = "/Users/apple/Desktop/Sherin/VIT/Mini Project- Libraray Managament/Bookshelf.txt"  #source file
    src = "/Users/apple/Desktop/Sherin/VIT/Mini Project- Libraray Managament/Output.txt"      #temp file
    
    listt()
    bk_no = int(input("\nEnter the book number to be returned: "))
    
    if (bk_no < 1):
        print("\nInput Error: Book number below range!\n")
        return;
        
    fin = open(dest, "r")
    fout = open(src, "w")
        
    Lines = fin.readlines()
    count = 0
    
    # Read each line in the file
    for line in Lines:
        count += 1
        book = line.strip().split(',')
         
        if count == bk_no:
            if book[3] == "No" and book[4] != username:
                print("\nThis book is borrowed by an another user\n")
                
            elif (book[3] == "No"  and book[4]== username):
                book[3] = "Yes"    #changing availability
                book[4] = ""       #updating user to nil
                print("\nBook is successfully returned!\n")
            else:
                print("\nYou have not borrowed book - {}\n", book[0])
                
        book_str = "{},{},{},{},{}\n".format(*book)
        fout.write(book_str)
            
    if (bk_no > count):
        print("\nInput Error: Book number exceeded range!\n")
        return;
        
    fin.close() 
    fout.close() 
    
    #copy temp fie to source file
    shutil.copy(src, dest) 
    #remove temp file
    os.remove(src)            

#Searching by category function 
def search_menu(books, username): 

    print("\n1. Search by Title")
    print("2. Search by Author")
    print("3. Search between years")
    print("4. Search Available Books")
    print("5. Search for books borrowed by you")
    print("6. Go to main menu")
    
    print()
    
    file_path = "/Users/apple/Desktop/Sherin/VIT/Mini Project- Libraray Managament/Bookshelf.txt"
    file = open(file_path,'r')
    
    Lines = file.readlines()
    count = 0

    bks = []
    
    # Read each line in the file
    for line in Lines:
        count += 1
        book = line.strip().split(',')
        bks.append(book)
    
    file.close()
        
    #print(bks)
    
    
    try:
        inp = int(input("\nEnter your search choice from above: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        search_menu(books, username)
    
    if inp == 1:
        search_func(bks, username, 1)
        search_menu(books, username)
    elif inp == 2: 
        search_func(bks, username, 2)
        search_menu(books, username)
    elif inp == 3: 
        search_func(bks, username, 3)
        search_menu(books, username)
    elif inp == 4: 
        search_func(bks, username, 4)
        search_menu(books, username)
    elif inp == 5:
        search_func(bks, username, 5)
        search_menu(books, username)
    elif inp == 6:
        main_page(books, user)
    else:
        print("Enter a valid choice of search") 
        return
    
def search_func(bks, username, option):
    
    yr1 = 0
    yr2 = 0
    key_low = "invalid string"
    date_format = "%d/%m/%Y"
    
    if (option == 1) | (option == 2):
        keyword = input("\nEnter the keyword to be searched: ")
        key_low = keyword.lower()
    elif (option == 3):
        yr1 = int(input("Enter the starting year: "))
        yr2 = int(input("Enter the ending year: "))
        
        if (yr1 >= yr2):
            print("Start year is greater than end year\n")
            return
            
    print()
    print(f"{'Title' : ^18}{'Author' : ^32}{'Published Date' : ^20}{'Available to Lend?' : ^20}")

    flag = False
    to_print = False
    for bk in bks: 
        bkstr = ','.join(map(str, bk))
        bkstr_low = bkstr.lower()
        
        # Parse the input string to a datetime object
        date = datetime.strptime(bk[2], date_format)
        # Extract the year
        bk_yr =  date.year
        
        if (bkstr_low.find(key_low) != -1) & ((option == 1) | (option == 2)):
            to_print = True
        elif (yr1 <= bk_yr <= yr2) & (option == 3):
            to_print = True
        elif (bk[3] == "Yes") & (option == 4):
            to_print = True
        elif (bk[4] == username) & (option == 5):
            to_print = True
        
        if (to_print == True):
            flag = True
            print(f"{bk[0] : <30}{bk[1] : <20}{bk[2] : ^20}{bk[3] : ^15}")
        
        to_print = False
            
    if not flag:
        print("No books were published in this year gap!")

# main program
user = login()
if (user == 0): 
    print("Invalid username or password. Access denied!\n")    
else:
    print("Login successful!")
    books = load_books()
    main_page(books,user)
