import abc
import requests


class Temperature(abc.ABC):
    '''
    This class represents all the temperature units Celsius, Fahrenheit and Kelvin.
    It contains conversion methods between theses units and returns float number
    as the calculations results.
    '''
    
    def celsius2fahr(temp):
        cel_fah = temp * 9/5 + 32
        return cel_fah

    def celsius2kelvin(temp):
        cel_kel = temp + 273.15
        return cel_kel 
    
    def fahr2celsius(temp):
        fah_cel = (temp - 32) * 5/9
        return fah_cel
    
    def fahr2kelvin(temp):
        fah_kel = (temp - 32) * 5/9 + 273.15
        return fah_kel

    def kelvin2celsius(temp):
        kel_cel = temp - 273.15
        return kel_cel

    def kelvin2fahr(temp):
        kel_fah = (temp - 273.15) * 9/5 + 32
        return kel_fah

class Length(abc.ABC): # cm, m, km...
    pass

class Mass(abc.ABC): # mg, g, kg...
    pass

class Time(abc.ABC): # seconds, minutes, hours...
    pass

class Currency(abc.ABC):
    """
    Avaible coins:
    BRL (Real Brasileiro)
    USD (Dolar Americano)
    EUR (Euro)
    """
    pass