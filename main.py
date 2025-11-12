# Assessment Note: As one can likely tell for my notes, I'm not big on the typical pseudocode style although I
# understand it and am willing to format it as such if necessary for planning/management in an organization. 
# For some reason, whenever I try writing in typical pseudocode style, I just end up writing the final code or 
# visualize what my code would look like in a programming language so the typical pseudocode ends up just consuming 
# valuable time for me. What works very well for me is describing/breaking down what would happen in the code and
# capitalizing the key words that hint towards the utilization of a coding concept (I think the problem is that
# the typical pseudocode style is ultra ultra translatable so I lean towards just writing actual code (instead of
# doing high-level planning) while the style I favor intellectually/descriptively breaks down what needs to happen 
# and is a bit less directly translatable).

from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

# Notes: DEFINE the function with a clear purpose-based NAME -- because we're looking through all the books
# (library_books) that means we're LOOPING through them. We need to check IF the book is AVAILABLE
# (key of a dictionary in the library_books ist) and we want to output (PRINT) book info like the the ID, title, 
# and author KEYS of each book (each instance/case).

def print_available_books():
    for book in library_books:
        if book["available"]:
            print(f"ID: {book["id"]} | Title: {book["title"]} | Author: {book["author"]}")

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

# Notes: AG refers to author or genre.
# DEFINE the function with a clear purpose-based NAME. Now we need to take the users search (INPUT), which will
# be used to check for the CONDITION (if) of whether it MATCHES (==/in) any book in our library (library_books). As
# searches are to be case-insensitive, we can simply use a METHOD to standardize (FORMAT) each search. Checking our
# library_books.py file, it seems as though all author and genre names are written with the first letter
# capitalized, which aligns with the .title() method. Technically, one could also format it however they like
# (.lower(), .upper(), .capitalize(), .swapcase(), BUT that would also need to be applied to the author and genre 
# of each book in the conditional statement, which is slightly extra work). Checking each book individually to see 
# if they match means we're going to LOOP through the library (library_books). 

# I ASSUME the "return" part of the part wants us to PRINT to the command line because this is supposed to be a 
# database service and not printing the results of the search would not be very helpful. I ASSUME "Return a list"
# doesn't refer to the data type, but an acutal list, which can be represented in multiple ways. If I'm not wrong, 
# I know this could easily be achieved by just adding book["title"] to a defined local list variable and then 
# printing it once the loop ends. I also ASSUME that when returning the list of matching books, they want all the 
# data that would be relevant for a user (id, title, availability -- I also added a little extra: Matched A/G (
# author/genre) because it's nice information to have). Lastly, I ASSUME it's okay if the user doesn't fully spell
# something, which is why I used "in" instead of "==".

def print_AG_searched_books():
    found = False
    search = input("Enter your search (author or genre) here: ").title()
    for book in library_books:
        if (search in book["author"]) or (search in book["genre"]):
            print(f"\nID: {book["id"]} | Title: {book["title"]} | Availability: {book["available"]}") # \n Adds stylistic break/space between the prompt and each individual book
            print(f"Matched A/G: {book["author"]}/{book["genre"]}")
            found = True
    if (found == False):
        print("\nNo matches found.") # \n # Adds stylistic break/space between the prompt and each individual book1

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

# Notes: I used W3Schools to read up on/learn about the datetime module in Python | (link: https://www.w3schools.com/python/python_datetime.asp)
# DEFINE the function with a clear purpose-based NAME. Now we need to get (INPUT) the book the user wants to check 
# out by ID, which we will check IF it is available (and making stat updates).

# Create a CONDITIONAL statement so that under the condition that the book is available, it's VALUE for the 
# key "available" will BECOME (=) "unavailable", the VALUE for the key "checkouts" will INCREMENT by 1 (+=1), and 
# the VALUE for the "due_date" key will become a FORMATED (using strftime method) version of the CALCULATED due 
# date of the entry. 
# In the CASE (ELSE) that the book is not available, simply PRINT a status message ("... already checked out.")
def checkout_book_ID():
    entry_due_date = datetime.today() + timedelta(days=14) # To get 14 days from today
    book_ID = input("Enter the ID of the book you are checking out here: ")
    # Seems like we'll have to manually sift through each book as we're looking for a key's value (available)
    # but to do that we have to identify the dictionary by ID (another key's value). 
    for book in library_books:
        if book["id"] == book_ID: # Checks if the value of the ID key is equal to the user's ID input
            if book["available"] == True:
                book["available"] = False
                book["due date"] = entry_due_date.strftime("%Y-%m-%d")
                book["checkouts"] += 1
                print(f"You have successfully checked out {book["title"]}. It is due on {book["due date"]}.")
                break
            else:
                print(f"Our apologizes; this book is already checked out. It is due for return {book["due_date"]}.")
                break


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# Notes: DEFINE a function with a purpose-based name. Inquire (INPUT) the ID of the book being returned. FIND
# (manually LOOP through it) the BOOK IN THE DATABASE (library_books) and IF a book SHARES (==) the given ID,
#  change the values of its "available" (TRUE) and "due_date" (NONE) keys.
def return_book_ID():
    book_ID = input("Enter the ID of the book you are returning here: ")
    for book in library_books:
        if (book["id"] == book_ID):
            if book["available"]: # I added this on as an edge case of sorts
                print(f"This book, {book["title"]}, wasn't checked out!")
                break
            else:
                book["available"] = True
                book["due_date"] = None
                print(f"Thank you for returning {book["title"]}!")

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

# Notes: DEFINE a function with a purpose-based name. Check EVERY (loop) book in the database (library_books).
def print_overdue_books():
    today = datetime.today() # could have been written as datetime.today() in the conditional, but this is cleaner
    for book in library_books:
        # Edge/anti-error case for ones that have None -- Skip books without a due_date (None)
        if book["due_date"] is None:
            continue # skip this case/book basically
        
        due_date = datetime.strptime(book["due_date"], "%Y-%m-%d") # Formatting due date
        if (due_date < today) and (book["available"] == False):
            print(f"\n{book["title"]} is overdue! It was due on {book["due_date"]}.")

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# Notes: I suppose this means the methods will be based on the above functions (that don't need to reference the 
# library; for example, search and view all ___ need to sift through the whole library/database, but checkout 
# doens't because it only refers to info about the book/singular case/object we're looking at) but with variables 
# swapped out with properties from object instances? (OOP vs Function-based/oriented programming). I'll set some 
# defaults like checkouts to obviously 0 for good housekeeping. | It's nice because there's not really a need for 
# for loops as each self is an instance

class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    
    def checkout(self):
        entry_due_date = datetime.today() + timedelta(days=14) # To get 14 days from today
        # Seems like we'll have to manually sift through each book as we're looking for a key's value (available)
        # but to do that we have to identify the dictionary by ID (another key's value). 
        if self.available:
            self.available = False
            self.due_date = entry_due_date.strftime("%Y-%m-%d")
            self.checkouts += 1
            print(f"You have successfully checked out {self.title}. It is due on {self.due_date}.")
            return
        else:
            print(f"Our apologizes; this book is already checked out. It is due for return {self.due_date}.")
            return
    
    def return_book(self):
        if self.available: # I added this on as an edge case of sorts
            print(f"This book, {self.title}, wasn't checked out!")
            return
        else:
            self.available = True
            self.due_date = None
            print(f"Thank you for returning {self.title}!")
    
    def is_overdue(self): # Tweaked to just check if the sole book is overdue
        today = datetime.today() # could have been written as datetime.today() in the conditional, but this is cleaner
        due_date = datetime.strptime(self.due_date, "%Y-%m-%d") # Formatting due date
        if (due_date < today) and (self.available == False): # could also write not book.available
            print(f"{self.title} is overdue! It was due on {self.due_date}.")

# Converted dictionary data (library_books file) into actual books (OBJECTS).
library_books_OOP = [
    Book("B1", "The Lightning Thief", "Rick Riordan", "Fantasy", True, None, 2),
    Book("B2", "To Kill a Mocking Bird", "Harper Lee", "Historical", False, "2025-11-01", 5),
    Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True, None, 3),
    Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4),
    Book("B5", "Pride and Prejudice", "Jane Austen", "Romance", True, None, 6),
    Book("B6", "The Hobbit", "J.R.R. Tolkien", "Fantasy", False, "2025-11-10", 8),
    Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1),
    Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age", False, "2025-11-12", 3),
    Book("B9", "Amari and the Night Brothers", "B. B. Alston", "Fantasy", True, None, 1000)
]

# Note: Creating the menu (a FUNCTION). Use a WHILE LOOP so the manager runs continuously unless exited and options
# are presented once a method has been run

# So while I could create an OOP version & use the dictionary version, I'll just be using the functions here 
# because the previous levels don't say to go back and write in dot notation. If I copy it all and edit new versions,
# there'll be so many lines of code and stuff to sift through in this file.
def menu():
    while True:
        print("\n*-*-*-*-* Library Menu *-*-*-*-*")
        print("1. View all books ") # Could end with \n, but for readability of code, there will just be a bunch of print statements
        print("2. Search by author or genre")
        print("3. Check out a book")
        print("4. Return a book")
        print("5. View overdue books")
        print("6. Exit")

        choice = input("\nEnter your desired action: ")

        if choice == "1":
            print_available_books()
        elif choice == "2":
            print_AG_searched_books()
        elif choice == "3":
            checkout_book_ID()
        elif choice == "4":
            return_book_ID()
        elif choice == "5":
            print_overdue_books()
        elif choice == "6":
            print("Thanks for using the *** Library Menu ***! Goodbye.")
            break # exit the While loop
        else: # edge case for invalid inputs
            print("Invalid choice. Try again.")
            

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog [Chidera's Note: Added as B9 (ID)!]
# - Sort and display the top 3 most checked-out books
# - Partial title/author search [Chidera's Note: Sort of done in line 55 (using "in" instead of "==")]
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions

    # print_available_books()
    # print_AG_searched_books()
    # checkout_book_ID()
    # return_book_ID()
    # print_overdue_books()

    menu()
    pass