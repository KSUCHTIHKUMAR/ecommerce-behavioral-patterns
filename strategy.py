from abc import ABC, abstractmethod
class PaymentStrategy(ABC):
    @abstractmethod
    def execute(self, amount): ...

class CardPayment(PaymentStrategy):
    def execute(self, amount): print(f"Paid ₹{amount} by Card")
class UPIPayment(PaymentStrategy):
    def execute(self, amount): print(f"Paid ₹{amount} via UPI")
class WalletPayment(PaymentStrategy):
    def execute(self, amount): print(f"Paid ₹{amount} from Wallet")

class CheckoutService:
    def __init__(self, strategy): self._strategy = strategy
    def set_strategy(self, s): self._strategy = s
    def pay(self, amount): self._strategy.execute(amount)