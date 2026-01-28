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