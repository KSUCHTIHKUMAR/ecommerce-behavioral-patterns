from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, product): ...

class User(Observer):
    def __init__(self, name): self.name = name
    def update(self, product):
        print(f"{self.name}: {product.name} now ₹{product.price}!")

class Product:
    def __init__(self, name, price):
        self.name, self._price, self._observers = name, price, []
    @property
    def price(self): return self._price
    def subscribe(self, o): self._observers.append(o)
    def unsubscribe(self, o): self._observers.remove(o)
    def notify(self):
        for o in self._observers: o.update(self)
    def set_price(self, new):
        dropped = new < self._price
        self._price = new
        if dropped: self.notify()