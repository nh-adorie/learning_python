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
        return 30

class Motorbike(Vehicle):
    def __init__(self, plate_number,cc):
        super().__init__(plate_number)
        self.cc = cc
    
    def show_info(self):
        super().show_info()
        print(f"Cubic Capicity: {self.cc}")
    
    def pay_fee(self):
        return 10

class Truck(Vehicle):
    def __init__(self, plate_number,load):
        super().__init__(plate_number)
        self.load = load

    def show_info(self):
        super().show_info()
        print(f"Payload Capicity: {self.load}T")
    
    def pay_fee(self):
        fee = 50
        if self.load > 10:
            fee += (self.load - 10)*5
        return fee
    
class TollBooth:
    def __init__(self):
        self.vehicle_list = []
        self.total_payment = 0
        self.total_quantity = 0
    
    def add_vehicle(self,vehicle):
        self.vehicle_list.append(vehicle)
    
    def show_vehicle_list(self):
        for vehicle in self.vehicle_list:
            print(f"Type: {type(vehicle).__name__}")
            vehicle.show_info()
            print("--")
      
    def summary_by_type(self):
        total_summary = {}
        for vehicle in self.vehicle_list:
            vehicle_type = type(vehicle).__name__
            if vehicle_type not in total_summary:
                total_summary[vehicle_type] = {
                    "quantity":0,
                    "toll_fee":0,
                }
            total_summary[vehicle_type]["quantity"] += 1
            total_summary[vehicle_type]["toll_fee"] += vehicle.pay_fee()
        return total_summary

    def show_quantity_by_type(self, total_summary):
        total_qty = 0
        for type, info in total_summary.items():
            print(f"{type} quantity: {info['quantity']}")
            total_qty += total_summary[type]["quantity"]
        print("--")
        print(f"Total quantity: {total_qty}")
    
    def show_payment_by_type(self, total_summary):
        total_payment = 0
        for type, info in total_summary.items():
            print(f"{type} payment: ${info['toll_fee']}")
            total_payment += total_summary[type]['toll_fee']
        print("--")
        print(f"Total payment: ${total_payment} ")

class TollBoothManagement:
    def __init__(self,booth):
        self.booth = booth

    def main(self):
        print("Welcome to the Toll Booth Management Program! ")
        print("""
1. Show Vehicle List 
2. Summary Vehicle Quantity by Type
3. Summary Toll Fee by Type
4. Quit
              """)
        while True:
            choice = input("\nPlease choose 1-4 ")
            if choice not in ["1","2","3","4"]:
                print("Please input invalid value ")
            elif choice == "4":
                print("\nGoodbye ~ ")
                break
            elif choice == "1":
                print("\nShow Vehicle List\n")
                booth.show_vehicle_list()
            elif choice == "2":
                print("\nSummary Vehicle Quantity by Type\n")
                booth.show_quantity_by_type(booth.summary_by_type())
            elif choice == "3":
                print("\nSummary Payment by Type\n")
                booth.show_payment_by_type(booth.summary_by_type())
            else:
                None


raw_car_list = [
    {"plate_number": "51A-12345", "seats": 4},
    {"plate_number": "30A-67890", "seats": 7},
    {"plate_number": "60B-11223", "seats": 5},
    {"plate_number": "70B-56748", "seats": 4}
]
raw_truck_list = [
    {"plate_number": "61C-99999", "load": 8},
    {"plate_number": "62C-88888", "load": 12},
    {"plate_number": "63C-77777", "load": 15}
]
raw_motor_list = [
    {"plate_number": "59D-12345", "cc": 125},
    {"plate_number": "33D-67890", "cc": 150},
    {"plate_number": "59D-99999", "cc": 100},
    {"plate_number": "73D-56432", "cc": 125},
    {"plate_number": "60D-44337", "cc": 100}
]

# Build from raw data:

booth = TollBooth()

for car_dict in raw_car_list:
    car_obj = Car(car_dict["plate_number"],car_dict["seats"])
    booth.add_vehicle(car_obj)

for truck_dict in raw_truck_list:
    truck_obj = Truck(truck_dict["plate_number"],truck_dict["load"])
    booth.add_vehicle(truck_obj)

for motor_dict in raw_motor_list:
    motor_obj = Motorbike(motor_dict["plate_number"],motor_dict["cc"])
    booth.add_vehicle(motor_obj)           

# 
booth_app = TollBoothManagement(booth)
booth_app.main()
                







