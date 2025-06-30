class Customer:
    def __init__(self, name, email, orders):
        self.name = name #string
        self.email = email #string
        self.orders = orders #obj từ class Orders
    
    def display_customer(self):
        print(f"Customer name: {self.name}")
        print(f"Email address: {self.email}")