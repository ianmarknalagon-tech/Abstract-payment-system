from abc import ABC, abstractmethod

class paymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard (paymentMethod):
    def pay(self, amount):
        print("Charging", amount, "to credit card.")

class paypal (paymentMethod):
    def pay(self, amount):
        print("Charging", amount, "via PayPal")

class Gcash (paymentMethod):
    def pay(self, amount):
        print("Charging", amount, "via Gcash")

methods = [CreditCard(), paypal(), Gcash()]
for m in methods:
    m.pay(49.99)