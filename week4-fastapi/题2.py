class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return  self.celsius * 9 / 5 + 32

    def describe(self):
        return f"{self.celsius}°C"
print(Temperature(0).to_fahrenheit())