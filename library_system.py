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
    