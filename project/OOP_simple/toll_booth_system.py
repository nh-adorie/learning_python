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
    
    def show_vehicle_list(self,list):
        for vehicle in self.vehicle_list:
            print(f"Type: {type(vehicle).__name__}")
            vehicle.show_info()
            print("--")
      
    def calculate_total_payment(self,vehicle_list):
        for vehicle in vehicle_list:
            self.total_payment += vehicle.pay_fee()
        return self.total_payment

raw_car_list = [
    {"plate_number": "51A-12345", "seats": 4},
    {"plate_number": "30A-67890", "seats": 7},
    {"plate_number": "60B-11223", "seats": 5}
]

raw_truck_list = [
    {"plate_number": "61C-99999", "load": 8},
    {"plate_number": "62C-88888", "load": 12},
    {"plate_number": "63C-77777", "load": 15}
]

raw_motor_list = [
    {"plate_number": "59D-12345", "cc": 125},
    {"plate_number": "59D-67890", "cc": 150},
    {"plate_number": "59D-99999", "cc": 100}
]

booth = TollBooth()

for car_dict in raw_car_list:
    car_obj = Car(car_dict["plate_number"],car_dict["seats"])
    booth.add_vehicle(car_obj)

for truck_dict in raw_truck_list:
    truck_obj = Truck(truck_dict["plate_number"],truck_dict["load"])
    booth.add_vehicle(car_obj)

for motor_dict in raw_motor_list:
    motor_obj = Motorbike(motor_dict["plate_number"],motor_dict["cc"])
    booth.add_vehicle(car_obj)

booth.show_vehicle_list(booth.vehicle_list)

    


