from datetime import datetime

class Notification:

    TYPE_OVERDUE = "OVERDUE"
    TYPE_RESERVATION_AVAILABLE = "RESERVATION_AVAILABLE"
    TYPE_GENERAL = "GENERAL"

    def __init__(self, notificationID, message, recipient):
        self.notificationID = notificationID
        self.message = message
        self.recipient = recipient
        self.creationDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.sentDate = None
        self.isRead = False
        self.notificationType = self.TYPE_GENERAL
    
    def send(self):
        # send notification
        if self.recipient == None:
            return False
        self.sentDate = datetime.now().strftime("%Y-%m-%d")
        
        return True
    

    def markAsRead(self):
        self.isRead = True
        return True
    
    def setNotificationType(self, notificationType):
        self.notificationType = notificationType
        return True
    
    def createReservationAvailableNotification(notificationID, member, bookTitle):
        message = f"The book {bookTitle} you reserved is available!"
        notification = Notification(notificationID, message, member)
        notification.setNotificationType(Notification.TYPE_RESERVATION_AVAILABLE)
        return notification
    
    def createOverdueNotification(notificationID, member, bookTitle, daysOverdue):
        message = f"{member.name}, your borrowed book {bookTitle} is overdue by {daysOverdue} days. Please return it and pay your fine"

        notification = Notification(notificationID, message, member)
        notification.setNotificationType(Notification.TYPE_OVERDUE)
