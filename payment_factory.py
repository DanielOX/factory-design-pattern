from inspect import getmembers, isclass, isabstract
import payment_methods


class PaymentFactory(object):
    payment_implementations = {}

    def __init__(self) -> None:
        self.load_payment_methods()

    def load_payment_methods(self):
        filter_abstract_cls = lambda member: isclass(member) and not isabstract(member)
        implementations = getmembers(payment_methods, filter_abstract_cls)
        for name, _type in implementations:
            print(name, _type)
            if isclass(_type) and issubclass(_type, payment_methods.Payment):
                self.payment_implementations[name] = _type
        print(self.payment_implementations)

    def create(self, payment_type: str):
        if payment_type in self.payment_implementations:
            return self.payment_implementations[payment_type]()
        else:
            raise ValueError(
                f"{payment_type} type is not currently supported as a payment method") 
