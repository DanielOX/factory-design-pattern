![Class Diagram of Implemented Design Pattern](https://github.com/DanielOX/factory-design-pattern/assets/33195456/faee49eb-3cd1-465e-b028-9624a7324503)

Factory Design Pattern
The Factory Design Pattern is a creational design pattern that provides an interface for creating objects in a super factory method. It allows you to create objects without specifying the exact class of the object that will be instantiated. The pattern promotes loose coupling and flexibility in your codebase.

I have used 3 concrete classes
 - GooglePayPayment
 - PayPalPayment
 - CreditCardPayment

Which is being utilised by the creator class PaymentFactory to generate class the relevant subclasses.
- It promotes the Open-Closed Responsibility Principle
- It promotes Single Responsibility Principle
