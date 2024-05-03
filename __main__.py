from payment_factory import PaymentFactory

factory = PaymentFactory()
payment = factory.create('CreditCardPayment')
payment.pay(100)
payment = factory.create('GooglePayPayment')
payment.pay(50)
payment = factory.create('PayPalPayment')
payment.pay(70)