from datetime import datetime

class Book:
    def __init__(self, ISBN, title, author, subject, publicationDate):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.subject = subject
        self.publicationDate = publicationDate
        self.totalCopies = 0
        self.availableCopies = 0
        self.bookItems = []
    
    def getBookInfo(self):
        return f"ISBN {self.ISBN}, Title {self.title}, Author {self.author}"
    
    def addBookItem(self, bookItem):
        if bookItem.book != self:
            return False
        self.bookItems.append(bookItem)
        self.totalCopies += 1
        if bookItem.isAvailable():
            self.availableCopies += 1

        return True
    
    def removeBookItem(self, bookItem):
        if bookItem.book != self:
            return False
        if bookItem.status == "Checked Out":
            return False
        self.bookItems.remove(bookItem)
        self.totalCopies -= 1
        if bookItem.isAvailable():
            self.availableCopies -= 1
        return True

    def getAvailableBookItem(self):
        for bookItem in self.bookItems:
            if bookItem.isAvailable():
                return bookItem
        return None


    def updateAvailability(self):
        self.availableCopies = 0
        for bookItem in self.bookItems:
            if bookItem.isAvailable():
                self.availableCopies += 1
        return self.availableCopies
    

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
            self.book.availableCopies -= 1
            return True
        return False
    
    def returnBook(self):
        # edit available quantity
        if self.status == "Checked Out":
            self.status = "Available"
            self.dueDate = None
            self.book.availableCopies += 1
            return True
        return False
    
    def setDueDate(self, dueDate):
        if self.status == "Checked Out":
            self.dueDate = dueDate
            return True
        return False
    
    def reserve(self):
        if self.isAvailable():
            self.status = "Reserved"
            self.book.availableCopies -= 1
            return True
        return False
    
    def isOverdue(self):
        if self.status == "Checked Out" and self.dueDate:
            current_date = datetime.now()
            due = datetime.strptime(self.dueDate, "%Y-%m-%d")
            return current_date > due
        return False
    
    