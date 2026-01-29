from abc import ABC
from datetime import datetime, timedelta

class Account(ABC):                         # abstract class since this should not be modified
    def __init__(self, name, address, email, phoneNumber, barcode):
        self.name = name
        self.address = address
        self.email = email
        self.phoneNumber = phoneNumber
        self.barcode = barcode
    def getDetails(self):
        return f"Name: {self.name}, Email: {self.email}, Barcode: {self.barcode}"
    

class Member(Account):                                                                            # Interacts with: Library, BookItem, Lending, Reservation, Fine
    def __init__(self, name, address, email, phoneNumber, barcode, membershipDate, memberID):
        super().__init__(name, address, email, phoneNumber, barcode)
        self.membershipDate = membershipDate
        self.totalBooksCheckedOut = 0
        self.booksReserved = 0
        self.memberID = memberID
        self.maxBooksLimit = 5
        self.maxBorrowDays = 10
        self.lendings = []
        self.reservations = []
        self.fines = []

    def returnBook(self, lending):
        if self.totalBooksCheckedOut > 0:
            lending.returnDate = datetime.now().strftime("%Y-%m-%d")            # setting return date to now and converting it to a string
            if lending in self.lendings:
                self.lendings.remove(lending)                                   # remove book from list of lent books 
            self.totalBooksCheckedOut -= 1                 
            return True
        return False
    
    def reserve(self, book, library):
        from management import Reservation                                          # Import reservation class

        if book not in library.books:
            return False
        
        if book.availableCopies > 0:
            return False

        reservationID = f"R-{self.memberID}-{book.ISBN}-{len(self.reservations)}"
        reservation = Reservation(reservationID=reservationID, memberID=self.memberID, bookID=book.ISBN, creationDate=datetime.now().strftime("%Y-%m-%d"), status="Pending")

        self.reservations.append(reservation)                                       # add reservation to list
        self.booksReserved += 1                                                     # increment no. of books that member reserved
        return True
    

    def renewBook(self, lending):
        if self.hasOverdueBooks():
            return False
        # get the old due date and add 10 days
        current_due = datetime.strptime(lending.dueDate, "%Y-%m-%d")
        new_due = current_due + timedelta(days=self.maxBorrowDays)
        lending.dueDate = new_due.strftime("%Y-%m-%d")

        return True
    
    def canCheckout(self):
        return self.totalBooksCheckedOut < self.maxBooksLimit
    
    def checkoutBook(self, lending):
        if self.canCheckout():
            self.lendings.append(lending)                       # add checked out book to lendings list
            self.totalBooksCheckedOut += 1
            return True
        return False
    
    def getTotalFines(self):
        #fine objects
        total = 0.0
        for fine in self.fines:
            total += fine.amount
        return total
    
    def hasOverdueBooks(self):
        #check
        current_date = datetime.now()

        for lending in self.lendings:
            if lending.returnDate == None:
                due_date = datetime.strptime(lending.dueDate, "%Y-%m-%d")
                if current_date > due_date:
                    return True
        return False
    

class Librarian(Account):                                                                       # Interacts with: Library, Book, BookItem, Member, Lending
    def __init__(self, name, address, email, phoneNumber, barcode, employeeID):
        super().__init__(name,  address, email, phoneNumber, barcode)

        self.employeeID = employeeID

    def addBook(self, book, library):
        # interact with library
        return library.addBook(book)

    def issueBook(self, bookItem, member, library):
        #create lending record
        from management import Lending
        from datetime import datetime, timedelta

        if not bookItem.isAvailable():
            return False

        if not member.canCheckout():
            return False
        
        bookItem.checkout()

        creation_date = datetime.now()
        due_date = creation_date + timedelta(days=member.maxBorrowDays)

        lendingID = f"L-{member.memberID}-{bookItem.barcode}"
        lending = Lending(lendingID=lendingID, memberID=member.memberID, bookItemBarcode=bookItem.barcode, creationDate=creation_date.strftime("%Y-%m-%d"), dueDate=due_date.strftime("%Y-%m-%d"))

        bookItem.dueDate = due_date.strftime("%Y-%m-%d")

        member.checkoutBook(lending)

        # if bookItem.book:
        #     bookItem.book.availableCopies -= 1            This is already handled by calling checkout() method

        return True
    
    def removeBook(self, bookID, library):
        # interact with library

        for book in library.books:
            if book.ISBN == bookID:
                library.books.remove(book)
                return True

        return False
    
    def addMember(self, member, library):
        # interact with library
        return library.registerMember(member)
    
    def removeMember(self, memberID, library):
        # interact with library
        for member in library.members:
            if member.memberID == memberID:
                if member.totalBooksCheckedOut == 0:
                    library.members.remove(member)
                    return True
                return False
        return False