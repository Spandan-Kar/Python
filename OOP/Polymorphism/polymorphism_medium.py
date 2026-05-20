class Payment:
    def pay(self):
        print("Processing payment...")

class Credit_Card(Payment):
    def pay(self):
        print("Payment done using credit card.")

class UPI(Payment):
    def pay(self):
        print("Payment done using UPI.")

class Cash(Payment):
    def pay(self):
        print("Payment done using Cash.")

payments= [
    Credit_Card(),
    UPI(),
    Cash()
]

for payment in payments:
    payment.pay()