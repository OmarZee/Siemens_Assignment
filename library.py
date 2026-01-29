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
    
    def scanBarcode(self, barcode):
        for bookItem in self.bookItems:
            if bookItem.barcode == barcode:
                return bookItem
            
        for member in self.members:
            if member.barcode == barcode:
                return member
        return None