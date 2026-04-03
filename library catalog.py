import os 

library_catalog ={}

def clear_screen () :
   os.system("Cls") if os.name == "nt" else os.system("clear")

def add_book (library_catalog) :
   while True : 
     id = input("Enter ISBN : ")
     titel = input("Enter title : ")
     author = input("Enter author : ")
     library_catalog[id] = {"titel":titel ,"author" :author , "Available" : "True"}
     print(f"Book '{titel}' by [auther] added to the library catalog with ISBN {id}.")
     user_input = input ("Do you want to add another book ? (y/n) : ")
     if user_input == 'y' :
        clear_screen()
     else :
        break 
        
def list_books (library_catalog,titel) :
   print(f"""Library Catalog :
         [library_catalog]""")
   

def Check_out_book (library_catalog,titel) :
   while True :
    Check_out_ISBN = input("Enter ISBN to chek out : ")
    if  library_catalog[Check_out_ISBN["Available"]] == "True" :
      print(f"Book {library_catalog[Check_out_ISBN[titel]]} checked out successfully.")
      library_catalog[Check_out_ISBN["Available"]] = "False"
    else :
       print("sorry, the book is currently checked out.")
    user_input = input ("Do you want to che book ? (y/n) : ")
    if user_input == 'y' :
        clear_screen()
    else :
        break    

def check_in_book (library_catalog,titel) :
   while True :
      Check_in_ISBN = input("Enter ISBN to  check in : ")
      if Check_in_ISBN in library_catalog :
         print(f"Book {library_catalog[Check_in_ISBN[titel]]} checked in successfully.")
         library_catalog[Check_in_ISBN["Available"]] = "True"
            
      else :
         print("Book not found in the catalog.")
      user_input = input ("Do you want to che book ? (y/n) : ")
      if user_input == 'y' :
        clear_screen()
      else :
          break         

def Exit () :
   print("Exiting the program ")


print("""
Menu :
1. Add book
2. Check out book
3. Check in book 
4. List books
5. Exit                    
""")

user_choice = input ("Enter your choice (1-5): ")
if user_choice == '1' :
   add_book(library_catalog)
elif user_choice == '2' : 
   Check_out_book(library_catalog)
elif user_choice == '3' : 
   check_in_book(library_catalog)
elif user_choice == '4' :
   list_books(library_catalog)
elif user_choice == "5" :
   Exit ()
else :
   print("Please Enter right choice")   




   





    
    
    
