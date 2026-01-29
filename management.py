from datetime import datetime, timedelta

class Lending:

    FINE_RATE = 100.0

    def __init__(self, lendingID, memberID, bookItemBarcode, creationDate, dueDate):
        self.lendingID = lendingID
        self.memberID = memberID
        self.bookItemBarcode = bookItemBarcode
        self.creationDate = creationDate
        self.dueDate = dueDate
        self.returnDate = None                  # will be set when book is returned

    def calculateFine(self):
        # calculate fine by checking retrnDate > dueDate and do overdue * fine per day
        if self.returnDate == None:
            current_date = datetime.now()
            due = datetime.strptime(self.dueDate, "%Y-%m-%d")

            if current_date > due:
                days_overdue = (current_date - due).days
                return days_overdue * self.FINE_RATE
            return 0.0
        
        return_date = datetime.strptime(self.returnDate, "%Y-%m-%d")
        due_date = datetime.strptime(self.dueDate, "%Y-%m-%d")

        if return_date > due_date:
            days_overdue = (return_date - due_date).days
            fine_amount = days_overdue * self.FINE_PER_DAY
            return fine_amount
        
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