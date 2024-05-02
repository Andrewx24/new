print(34)
print(30)
class Age:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def age(self):
        c = int(self.b) - int(self.a)
        return c
    
print(Age(1990, 2020).age())