from abc import ABC

class Account(ABC):
    def __init__(self, name, address, email, phoneNumber, barcode):
        self.name = name
        self.address = address
        self.email = email
        self.phoneNumber = phoneNumber
        self.barcode = barcode
    def getDetails(self):
        return f"Name: {self.name}, Email: {self.email}, Barcode: {self.barcode}"
    

class Member(Account):
    def __init__(self, name, address, email, phoneNumber, barcode, membershipDate, memberID):
        super().__init__(name, address, email, phoneNumber, barcode)
        self.membershipDate = membershipDate
        self.totalBooksCheckedOut = 0
        self.booksReserved = 0
        self.memberID = memberID
        self.maxBooksLimit = 5
        self.maxBorrowDays = 10

    def returnBook(self):
        if self.totalBooksCheckedOut > 0:
            self.totalBooksCheckedOut -= 1
            return True
        return False
    
    def reserve(self):
        self.booksReserved += 1
        return True
    
    def renewBook(self):
        return True
    
    def canCheckout(self):
        return self.totalBooksCheckedOut < self.maxBooksLimit
    
    def checkoutBook(self):
        if self.canCheckout():
            self.totalBooksCheckedOut += 1
            return True
        return False
    
    def getTotalFines(self):
        #fine objects
        return 0.0
    
    def hasOverdueBooks(self):
        #check
        return False
    

class Librarian(Account):
    def __init__(self, name, address, email, phoneNumber, barcode, employeeID):
        super().__init__(name,  address, email, phoneNumber, barcode)

        self.employeeID = employeeID

    def addBook(self, book):
        # interact with library
        return True

    def issueBook(self, bookItem, member):
        #create lending record
        return True
    
    def removeBook(self, bookID):
        # interact with library
        return True
    
    def addMember(self, member):
        # interact with library
        return True
    
    def removeMember(self, memberID):
        # interact with library
        return True
    
class Book:
    def __init__(self, ISBN, title, author, subject, publicationDate):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.subject = subject
        self.publicationDate = publicationDate
        self.totalCopies = 0
        self.availableCopies = 0
    
    def getBookInfo(self):
        return f"ISBN {self.ISBN}, Title {self.title}, Author {self.author}"
        

class BookItem:
    def __init__(self, barcode, rackNo, status, book, price):
        self.barcode = barcode
        self.rackNo = rackNo
        self.status = status
        self.book = book                    # reference Book object
        self.dueDate = None
        self.price = price

    def isAvailable(self):
        # check if available
        return self.status == "Available"
    
    def checkout(self):
        # edit available quantity
        if self.isAvailable():
            self.status = "Checked Out"
            return True
        return False
    
    def returnBook(self):
        # edit available quantity
        if self.status == "Checked Out":
            self.status = "Available"
            self.dueDate = None
            return True
        return False
    
class Lending:
    def __init__(self, lendingID, memberID, bookItemBarcode, creationDate, dueDate):
        self.lendingID = lendingID
        self.memberID = memberID
        self.bookItemBarcode = bookItemBarcode
        self.creationDate = creationDate
        self.dueDate = dueDate
        self.returnDate = None                  # will be set when book is returned

    def calculateFine(self):
        # calculate fine by checking retrnDate > dueDate and do overdue * fine per day
        return 0.0


class Reservation:
    def __init__(self, reservationID, memberID, bookID, creationDate, status):
        self.reservationID = reservationID
        self.memberID = memberID
        self.bookID = bookID
        self.creationDate = creationDate
        self.status = status

    def cancel(self):
        # cancel reservation
        if self.status == "Pending":
            self.status = "Cancelled"
            return True
        return False

    def notify(self):
        # send notifcation 
        return True
    

class Fine:
    def __init__(self, fineID, memberID, amount):
        self.fineID = fineID
        self.memberID = memberID
        self.amount = amount

    def collectFine(self):
        # collect calculated fine 
        return True
    
class Notification:
    def __init__(self, notificationID, message, recipient):
        self.notificationID = notificationID
        self.message = message
        self.recipient = recipient
    
    def send(self):
        # send notification
        return True


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.bookItems = []
    
    def searchByTitle(self, title):
        results = []
        for book in self.books:
            if title.lower() in book.title.lower():
                results.append(book)
        return results
    
    def searchByAuthor(self, author):
        results = []
        for book in self.books:
            if author.lower() in book.author.lower():
                results.append(book)
        return results
    
    def searchBySubject(self, subject):
        results = []
        for book in self.books:
            if subject.lower() in book.subject.lower():
                results.append(book)
        return results
    
    def searchByPublicationDate(self, date):
        results = []
        for book in self.books:
            if book.publicationDate == date:
                results.append(book)
        return results
    
    def searchByISBN(self, isbn):
        for book in self.books:
            if book.ISBN == isbn:
                return book
        return None
    
    def addBook(self, book):
        self.books.append(book)
        return True
    
    def registerMember(self, member):
        self.members.append(member)
        return True
    
    def scanBarcode(self):
        # scan
        return "Scanned_Barcode"