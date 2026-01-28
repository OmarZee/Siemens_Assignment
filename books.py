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