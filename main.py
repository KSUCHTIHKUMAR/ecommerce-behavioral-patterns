from observer import Product, User
from strategy import CheckoutService, CardPayment, UPIPayment, WalletPayment
from command import CartService, AddItemCommand, RemoveItemCommand, ApplyCouponCommand, Invoker

print("=== Observer: Price Drop Notification ===")
phone = Product("Phone", 20000)
a, b = User("Asha"), User("Ravi")
phone.subscribe(a)
phone.subscribe(b)
phone.set_price(18000)       # both notified
phone.unsubscribe(b)
phone.set_price(17000)       # only Asha notified

print("\n=== Command: Cart with Undo/Redo ===")
cart = CartService()
ui = Invoker()
ui.run(AddItemCommand(cart, ("Phone", 17000)))
ui.run(AddItemCommand(cart, ("Case", 500)))
ui.run(ApplyCouponCommand(cart, 0.10))
print("Total after coupon:", cart.total())
ui.undo()
print("After undo coupon:", cart.total())
ui.redo()
print("After redo coupon:", cart.total())
ui.run(RemoveItemCommand(cart, ("Case", 500)))
print("After removing case:", cart.total())

print("\n=== Strategy: Payment ===")
checkout = CheckoutService(UPIPayment())
checkout.pay(cart.total())
checkout.set_strategy(CardPayment())   # switched at runtime
checkout.pay(cart.total())
checkout.set_strategy(WalletPayment())
checkout.pay(cart.total())