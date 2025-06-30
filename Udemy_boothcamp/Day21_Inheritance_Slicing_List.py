# Class Inheritance
class Animal:
    def __init__(self):
        pass
    
    def breathe(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("doing this underwater")
    
    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()

#slicing work with list and tuple

# list  
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(f"C is: {piano_keys[2:5]}")
print(piano_keys[::-1])

# tuple
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[2:5])


