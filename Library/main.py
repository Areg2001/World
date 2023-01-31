from student import Student
from library import Library
from book import Book

book1 = Book("Mark Lutz, Python")
book2 = Book("Bjarne Stroustrup, A Tour of C++")
book3 = Book("Marc Deisenroth, Math")

print(book1)
print(book2)
print(book3)

library = Library("IT library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library)

student1 = Student("Varazdat", "Hakobyan", 25)
student2 = Student("Hamo", "Mxoyan", 20)
student3 = Student("Karlen", "Isoyan", 23)

print(student1)
print(student2)
print(student3)

student1.take_book(library, "Mark Lutz, Python")
student2.take_book(library, "Bjarne Stroustrup, A Tour of C++")
student3.take_book(library, "Marc Deisenroth, Math")
print(library)

print(student1)
print(student2)
print(student3)

student1.take_book(library, "Mark Lutz, Python")
student2.take_book(library, "Mark Lutz, Python")

print(student1.books)
print(student2.books)

student1.return_book(library, "Mark Lutz, Python")

print(student1.books)
print(library.books)

student2.take_book(library, "Mark Lutz, Python")
print(student2.books)

student1.return_book(library, "Mark Lutz, Python")
student1.take_book(library, "Marc Deisenroth, Math")
student3.take_book(library, "Mark Lutz, Python")
student1.take_book(library, "Bjarne Stroustrup, A Tour of C++")

print(student1.books)
print(student2.books)
print(student3.books)



