#Class and Object
#3. You are building a Library Management System. Create a `Book` class with properties
#  like `title`, `author`, and `isbn`. Write a method to display book details.

class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def dispaly(self):
        print("The book details are: ")
        print(f"Title: {self.title} \nAuthor: {self.author} \nIsbn: {self.isbn}")

title=input("Enter the title: ")
author=input("Enter the author: ")
Isbn=input("Enter the Isbn: ")
book=Book(title,author,Isbn)
book.dispaly()

# library=[]
# n=int(input("ENter no.of books: "))
# while n>0:
#     title=input("Enter the title: ")
#     author=input("Enter the author: ")
#     Isbn=input("Enter the Isbn: ")
#     n=n-1
#     book=Book(title,author,Isbn)
#     library.append(book)
# for i in library:
#     book.dispaly()
