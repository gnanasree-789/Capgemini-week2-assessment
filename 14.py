# Polymorphism
# •	14. Implement method overriding for a `Notification` class where `send()` is overridden 
# in `EmailNotification` and `SMSNotification`.

class Notification:
    def send(self):
        print("The notification is sent")
class EmailNotification(Notification):
    def send(self):
         print("Email notification is sent") 
class SMSNotification(Notification):
    def send(self):
        print("The SMS Notification is sent")

e=EmailNotification()
e.send()
s=SMSNotification()
s.send()