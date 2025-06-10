class Vehicle:
    def __init__(self,plate_number):
        self.plate_number = plate_number
    
    def show_info(self):
        print(f"Plate number: {self.plate_number}")

class Car(Vehicle):
    def __init__(self,plate_number,seats):
        super().__init__(plate_number)
        self.seats = seats
    
    def show_info(self):
        super().show_info()
        print(f"Seat number: {self.seats}")

class Motorbike:
    def __init__(self):
        pass

class Truck:
    def __init__(self):
        pass

