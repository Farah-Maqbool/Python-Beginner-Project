"""Library Book Reservation System
Design a Python program for a Library Book Reservation System. Create a function 
reserve_book(book_title, student_status) that allows students to reserve a book. If the book is available 
and the student is a regular student, reserve the book; if the student is a VIP student, provide instant 
reservation. Handle cases where the book is not available."""
def reserve_book(book_title,student_status):
    book=[" Paths, Dangers, Strategies","A Modern Approach","Being Human in the Age of Artificial Intelligence",\
          "Foundations of Autonomous Agents"," A Guide for Thinking Humans","Foundations of Computational Agents",\
          "A Very Short Introduction","The Art and Science of Algorithms that Make Sense of Data","A New Synthesis"]
    if book_title in book and student_status=="Regular":
        return"Book is reserve"
    elif book_title not in book and student_status=="Regular":
        book.append(book_title)
        return "Book is reserve"
    elif book_title in book and student_status=="Not Regular":
         return "You are not regular so we don't reserve your book"
    elif book_title in book and student_status=="VIP":
         return "Book is reserve"
    elif book_title not in book and student_status=="VIP":
        book.append(book_title)
        return "Book is reserve"
book_title=input("Enter Book title: ")
student_status=input("Enter Student Status (Regular, Not regular, VIP): ")   
result=reserve_book(book_title,student_status)
print(result)