from .payment import Payment

class GooglePayPayment(Payment):
    def pay(self, amount: float):
        print(f'Successfully payed ${amount} of dollars to merchant using a Pay Pal')