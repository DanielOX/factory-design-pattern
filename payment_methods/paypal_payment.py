from .payment import Payment

class PayPalPayment(Payment):
    def pay(self, amount: float):
        print(f'Successfully payed ${amount} of dollars to merchant using a credit card')