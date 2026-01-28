class Notification:
    def __init__(self, notificationID, message, recipient):
        self.notificationID = notificationID
        self.message = message
        self.recipient = recipient
    
    def send(self):
        # send notification
        return True