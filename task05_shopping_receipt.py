class CustomerInfo:
    def __init__(self, name, product, price, quantity):
        self.name = name
        self.product = product
        self.price = price
        self.quantity = quantity
        
    def expense(self):
        total_price = self.price * self.quantity
        return total_price
    
    def __str__(self):
        print("=" * 40)
        print("        RECEIPT")
        print("=" * 40)
        print(f"Customer: {self.name}")
        print()
        print("Product     Price     Qty")
        print("-" * 40)
        print(f"{self.product}      {self.price}       {self.quantity}")
        print()
        print(f"Total: {self.expense()} ETB")
        print("Thank You For Shopping!")
        print("=" * 40)
        
name = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

customer_1 = CustomerInfo(name, product, price, quantity)
print(customer_1)