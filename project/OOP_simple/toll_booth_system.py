class Vehicle:
    def __init__(self,plate_number):
        self.plate_number = plate_number
    
    def show_info(self):
        print(f"Plate number: {self.plate_number}")

    def pay_fee(self):
        return 0

class Car(Vehicle):
    def __init__(self,plate_number,seats):
        super().__init__(plate_number)
        self.seats = seats
    
    def show_info(self):
        super().show_info()
        print(f"Seat number: {self.seats}")
    
    def pay_fee(self):
        return 30000

class Motorbike(Vehicle):
    def __init__(self, plate_number,cc):
        super().__init__(plate_number)
        self.cc = cc
    
    def show_info(self):
        super().show_info()
        print(f"Cubic Capicity: {self.cc}")
    
    def pay_fee(self):
        return 10000

class Truck(Vehicle):
    def __init__(self, plate_number,load):
        super().__init__(plate_number)
        self.load = load

    def show_info(self):
        super().show_info()
        print(f"Payload Capicity: {self.load}T")
    
    def pay_fee(self):
        fee = 50000
        if self.load > 10:
            fee += (self.load - 10)*5000
        return fee
    
class TollBooth:
    def __init__(self):
        self.vehicle_list = []
        self.total_payment = 0
    
    def add_vehicle(self,vehicle):
        self.vehicle_list.append(vehicle)
    
    def calculate_total_payment(self,vehicle_list):
        for vehicle in vehicle_list:
            self.total_payment += vehicle.pay_fee()
        return self.total_payment

