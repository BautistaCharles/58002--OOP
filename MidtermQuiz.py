class TempConversion:
    def __init__(self, temp):
        self.__temp = temp

    def fahrenheit_to_celsius(self):
        return (self.__temp - 32) * 5/9

    def kelvin_to_celsius(self):
        return self.__temp - 273.15

    def celsius_to_fahrenheit(self):
        return (self.__temp * 9/5) + 32

    def kelvin_to_fahrenheit(self):
        return (self.__temp * 9/5) - 459.67

    def celsius_to_kelvin(self):
        return self.__temp + 273.15

    def fahrenheit_to_kelvin(self):
        return (self.__temp + 459.67) * 5/9

    def display(self):
        print(f"{temp} F = {tc.fahrenheit_to_celsius()} C")
        print(f"{temp} K = {tc.kelvin_to_celsius()} C")
        print(f"{temp} C = {tc.celsius_to_fahrenheit()} F")
        print(f"{temp} K = {tc.kelvin_to_fahrenheit()} F")
        print(f"{temp} C = {tc.celsius_to_kelvin()} K")
        print(f"{temp} F = {tc.fahrenheit_to_kelvin()} K")

temp = float(input("Enter temperature: "))
tc = TempConversion(temp)
tc.display()