import abc

class Temperature(abc.ABC):
    '''
    This class represents all the temperature units Celsius, Fahrenheit and Kelvin.
    It contains conversion methods between theses units and returns float number
    as the calculations results.
    '''
    
    def celsius_to_farenheit(temp):
        cel_fah = temp * 9/5 + 32
        return cel_fah

    def celsius_to_kelvin(temp):
        cel_kel = temp + 273.15
        return cel_kel 
    
    def fahrenheit_to_celsius(temp):
        fah_cel = (temp - 32) * 5/9
        return fah_cel
    
    def fahrenheit_to_kelvin(temp):
        fah_kel = (temp - 32) * 5/9 + 273.15
        return fah_kel

    def kelvin_to_celsius(temp):
        kel_cel = temp - 273.15
        return kel_cel

    def kelvin_to_fahrenheit(temp):
        kel_fah = (temp - 273.15) * 9/5 + 32
        return kel_fah

class Length(abc.ABC):
    pass

class Mass(abc.ABC):
    pass

class Time(abc.ABC):
    pass

class Currency(abc.ABC):
    pass