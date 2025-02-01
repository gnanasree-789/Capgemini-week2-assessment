# Polymorphism
# 12. Write a `Payment` class with a method `process_payment()`. 
# Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.

class Payment:
    def process_payment(self,amount):
        self.amount=amount
        print("The payment is processed")
class CreditCardPayment(Payment):
    def process_payment(self,amount):
        print(f"Credit Card Payment: {amount}")
class PayPalPayment(Payment):
    def process_payment(self,amount):
        print(f"PayPal Payment: {amount}")
class BitcoinPayment(Payment):
    def process_payment(self,amount):
        print(f"Bitcoin Payment: {amount}")
    
amount=int(input("ENter the amount: "))
print("Select one payment method: \n1.Credit card \n2.Paypal \n3.Bitcoin")
option=int(input("Select one option: "))
if option == 1:
    payment=CreditCardPayment()
    payment.process_payment(amount)
elif option == 2:
    payment=PayPalPayment()
    payment.process_payment(amount)
elif option == 3:
    payment=BitcoinPayment()
    payment.process_payment(amount)