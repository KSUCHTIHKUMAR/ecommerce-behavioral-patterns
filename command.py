from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self): ...
    @abstractmethod
    def undo(self): ...

class CartService:  # Receiver
    def __init__(self): self.items, self.discount = [], 0
    def add(self, i): self.items.append(i)
    def remove(self, i): self.items.remove(i)
    def total(self): return sum(p for _, p in self.items) * (1 - self.discount)

class AddItemCommand(Command):
    def __init__(self, cart, item): self.cart, self.item = cart, item
    def execute(self): self.cart.add(self.item)
    def undo(self): self.cart.remove(self.item)

class RemoveItemCommand(Command):
    def __init__(self, cart, item): self.cart, self.item = cart, item
    def execute(self): self.cart.remove(self.item)
    def undo(self): self.cart.add(self.item)

class ApplyCouponCommand(Command):
    def __init__(self, cart, pct): self.cart, self.pct, self.prev = cart, pct, 0
    def execute(self): self.prev, self.cart.discount = self.cart.discount, self.pct
    def undo(self): self.cart.discount = self.prev

class Invoker:  # "UI button"
    def __init__(self): self.undo_s, self.redo_s = [], []
    def run(self, c): c.execute(); self.undo_s.append(c); self.redo_s.clear()
    def undo(self):
        if self.undo_s: c = self.undo_s.pop(); c.undo(); self.redo_s.append(c)
    def redo(self):
        if self.redo_s: c = self.redo_s.pop(); c.execute(); self.undo_s.append(c)