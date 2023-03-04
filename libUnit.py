import abc
import requests
import json

class Temperature(abc.ABC):
    '''
    This class represents the temperature measurement units: Celsius, Fahrenheit and Kelvin.
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

class Length(abc.ABC):
    '''
    This class represents the lenght measurement units: nanometer, millimeter, centimeter, meter, kilometer, yard, feet and mile.
    It contains conversion methods between theses units and returns float number
    as the calculations results.
    '''
    pass

class Mass(abc.ABC): # mg, g, kg, short ton, metric ton, oz, lbs, stone...
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
    def USD2BRL(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['USDBRL']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"
    
    def USD2EUR(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/USD-EUR")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['USDEUR']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def EUR2BRL(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-BRL")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['EURBRL']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"
        
    def EUR2USD(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-USD")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['EURUSD']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"
        
    def BRL2USD(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/BRL-USD")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['BRLUSD']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"
    
    def BRL2EUR(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/BRL-EUR")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['BRLEUR']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"