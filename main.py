from library_books import library_books
from datetime import datetime, timedelta

#starter data


# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def view_available_books():
    for book in library_books:
        if book['available']:
            print(book['id'],book['title'], book['author'])


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books(input):
    books_list = []
    for book in library_books:
        if (book['author'].lower()) == input.lower() or (book['genre'].lower()) == input.lower():
            books_list.append(book)
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
    for book in library_books:
        if book['id'].lower() == id_num.lower(): # if it is, check the id case insensitively
            if book['available']: #check that the book is available
                book['available'] = False #make it unavailable 
                now = datetime.now() #define the time right now
                due_date = now + timedelta(days=14)
                book['checkouts'] +=1
            else:
                print("This book is already checked out!")

                


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_by_id(book_id):
    for book in library_books:
        if book['id'].lower() == book_id.lower():
            book['available'] = True
            due_date = datetime.none()

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def check_overdue():
    overdue_list = []
    for book in library_books:
        if book['available'] == False:
            if datetime.now() > due_date:
                overdue_list.append(book)


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
class Book:
    def __init__(self, id_num, title, author, genre, available, due_date, checkouts):
        self.id_num = id_num
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def checkout():
        for book in library_books:
            if book['id'].lower() == id_num.lower(): # if it is, check the id case insensitively
                if book['available']: #check that the book is available
                    book['available'] = False #make it unavailable 
                    now = datetime.now() #define the time right now
                    due_date = now + timedelta(days=14)
                    book['checkouts'] +=1
                else:
                    print("This book is already checked out!")
        
    def return_book():

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    # view_available_books()
   #print(search_books("RiCk RiOrDaN"))
   b1 = Book("B1", "The Lightning Thief", "Rick Riordan", "Fantasy", True, None, 2)
   b2 = Book("B2", "To Kill a Mockingbird", "Harper Lee", "Historical", False, "2025-11-01", 5)
   b3 = Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True, None, 3)
   b4 = Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4)
   b5 = Book("B5", "Pride and Prejudice", "Jane Austen", "Romance", True, None, 6)
   b6 = Book("B6", "The Hobbit", "J.R.R. Tolkien", "Fantasy", False, "2025-11-10", 8)
   b7 = Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1)
   b8 = Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-Of-Age", False, "2025-11-12", 3)
   print(checkout_by_id("B7"))
    #pass
