import abc

class Temperature(abc.ABC):
    def celsius_to_farenheit(temp):
        fah = (temp * 9/5) + 32
        return fah
    
    def fahrenheit_to_celsius(temp):
        cel = (temp - 32) * 5/9
        return cel

class Distance(abc.ABC):
    pass
