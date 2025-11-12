from library_books import library_books
from datetime import datetime, timedelta

#starter data


# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def view_available_books():
    for book in library_books:
        if book['available']: #if any book has value true for key available
            print(book['id'],book['title'], book['author']) #print the id, title, and author of the book.



# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books(num_id):
    books_list = []
    for book in library_books:
        if (book['author'].lower()) == num_id.lower() or (book['genre'].lower()) == num_id.lower(): #checking case insensitively if the entered parameter matches the author or genre
            books_list.append(book['title']) # if the author or genre has been found, add the book to the list by its title
    return books_list



# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout_by_id(id_num):
    found = False
    for book in library_books:
        if book['id'].lower() == id_num.lower(): # if it is, check the id case insensitively
            found = True
            if book['available']: #check that the book is available
                book['available'] = False #make it unavailable 
                now = datetime.now() #define the time right now
                due_date = str((now + timedelta(days=14)).date())
                book['due_date'] = due_date
                book['checkouts'] +=1
                print("Your book " + book['title'] + " is due on " + due_date) #specify the borrowed book and its due date
            
            else:
                print("This book is already checked out!")
            
    if found == False: #if the book wasn't found, the id would be invalid
        print("Pleae enter a valid ID")


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_by_id(book_id):
    found = False #set found to false by default. we will set it to true when the desired book is found
    for book in library_books:
        if book['id'].lower() == book_id.lower():
            book['available'] = True #make the book available again now that it has been returned
            book['due_date'] = None #set the due date to none because it was returned
            print(f"Thank you for returning your book, {book['title']}")
            found = True
    if found == False:
        print("ID is invalid. Please enter a valid ID. ") #if the book was not found in the system, the id must have been invalid


# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def check_overdue():
    overdue_list = []
    for book in library_books:
        if book['available'] == False: #checking to see that the book is checked out
            if str(datetime.now().date()) > book['due_date']: #checking if the date the date in which the book was due precedes the date right now
                overdue_list.append(book['title'])
    print(f"These books are overdue: {overdue_list}")
# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
class Book:
    def __init__(self, id, title, author, genre, available, due_date, checkouts): #here is my constructor
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def checkout(id, library_list):
        for book in library_list:
            if book.id.lower() == id.lower(): # if it is, check the id case insensitively
                if book.available: #check that the book is available
                    book.available = False #make it unavailable 
                    now = datetime.now() #define the time right now
                    due_date = now + timedelta(days=14)
                    book.checkouts +=1
                    print(f"Your book, {book.title}, has been successfully checked out!")
                else:
                    print("This book is already checked out!")
        
    def return_book(book_id, library_list):
        found_book = False #the book is by default not found yet. this will be changed as soon as it can be located
        for book in library_list:
            if book.id.lower() == book_id.lower():
                book.available = True
                book.due_date = None #set due date to None
                print(f"Your book, {book.title}, has successfully been returned!")
                found_book = True
        if found_book == False:
            print("We couldn't find a book that matches this ID. Please enter a valid ID. ")


    def view_available(library_list):
        for book in library_list:
            if book.available == True:
                print(book.id,book.title, book.author) #if the book is available, print its id, title, and author

    def search_by_au_ge(id_number, library_list):
        available_list = []
        for book in library_list:
            if (book.author.lower()) == id_number.lower() or (book.genre.lower()) == id_number.lower():
                available_list.append(book.title)

        if len(available_list) > 0:  # if the list of available books has at least one element in it      
            print(f"The books that match your search are : {available_list}")
        else:
            print("There are no available books with this ID/Author name")

    def view_overdue(library_list):
        overdue_books = []
        for book in library_list:
            if book.due_date != None: #if there is a value that is not None for the book's due date, it must be checked out
                if str(datetime.now().date()) > book.due_date: #checking to see if the due date preceded the current date. if so , it is past due
                    overdue_books.append(book.title)
        print(f"These books are overdue: {overdue_books}")
    
    def view_top_three(library_list):
        checkout_counts = []
        for book in library_list:
            checkout_counts.append(book.checkouts) #take all the checkout numbers of all books in this list
        checkout_counts.sort(reverse = True)
        top_counts = checkout_counts[:3] #take the first 3 numbers, which would be the largerst ones because I sorted in descending order
        top_books = []
        for count in top_counts:
            for book in library_list:
                if book.checkouts == count and book.title not in top_books: #making sure I don't add the book title twice
                    top_books.append(book.title)
                    break
        print(f"The most checked out books are {top_books}")
        

                




# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    # Below is where I was testing my functions
    # view_available_books()
    #print(search_books("RiCk RiOrDaN"))
    #print(checkout_by_id("B7"))
    #print(return_by_id("B11"))
    #check_overdue()
    #checkout_by_id("b3")
    # here I am creating my book objects
    b1 = Book("B1", "The Lightning Thief", "Rick Riordan", "Fantasy", True, None, 2)
    b2 = Book("B2", "To Kill a Mockingbird", "Harper Lee", "Historical", False, "2025-11-01", 5)
    b3 = Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True, None, 3)
    b4 = Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4)
    b5 = Book("B5", "Pride and Prejudice", "Jane Austen", "Romance", True, None, 6)
    b6 = Book("B6", "The Hobbit", "J.R.R. Tolkien", "Fantasy", False, "2025-11-10", 8)
    b7 = Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1)
    b8 = Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-Of-Age", False, "2025-11-12", 3)
    library_list = [b1,b2,b3,b4,b5,b6,b7,b8]
    # above is my list of objects

    print("Menu")
    print("1. View Available books")
    print("2. Search books")
    print("3. Checkout book")
    print("4. Return book")
    print("5. View Overdue")
    print("6. View 3 Most Checked Out books")
    print("7. Exit")
    run = True
    while run:
        print()
        choice = input("Please choose the number corresponding to your choice above: ")
        print()
        if choice == str(1):
            Book.view_available(library_list)
        if choice == str(2):
            choose_au_ge = input("Please enter the author or genre of the book you are searching for: ")
            Book.search_by_au_ge(choose_au_ge, library_list)
        if choice == str(3):
            choose_id = input("Please enter the ID of the book you want to check out: ")
            Book.checkout(choose_id, library_list)
        if choice == str(4):
            return_id = input("Please enter the ID of the book you want to return")
            Book.return_book(return_id, library_list)
        if choice == str(5):
            Book.view_overdue(library_list)
        if choice == str(6):
            Book.view_top_three(library_list)
        if choice == str(7):
            run = False
#pass
