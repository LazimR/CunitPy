import abc
import requests
import json

class Verify(abc.ABC):
    '''
    This class is a value verifier.
    It contains a method which verifies the variable type of the parameter
    and is called by all conversion methods from measurement units classes.
    '''
    def checkValue(value):
        try:
            float(value)
        except:
            print('Invalid value. Numbers only.')
            return False

class Temperature(abc.ABC):
    '''
    This class represents the temperature measurement units: Celsius, Fahrenheit and Kelvin.
    It contains conversion methods between theses units and returns float number
    as the calculations results.
    '''
    
    def celsius2fahr(temp):
        if Verify.checkValue(temp):
            cel_fah = temp * 9/5 + 32
            return cel_fah

    def celsius2kelvin(temp):
        if Verify.checkValue(temp):
            cel_kel = temp + 273.15
            return cel_kel 
    
    def fahr2celsius(temp):
        if Verify.checkValue(temp):
            fah_cel = (temp - 32) * 5/9
            return fah_cel
    
    def fahr2kelvin(temp):
        if Verify.checkValue(temp):
            fah_kel = (temp - 32) * 5/9 + 273.15
            return fah_kel

    def kelvin2celsius(temp):
        if Verify.checkValue(temp):
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
    def metter2nanometer(lenght):
        if Verify.checkValue(lenght):
            pass


class Mass(abc.ABC): # mg, g, kg, short ton, metric ton, oz, lbs, stone...
    pass

class Time(abc.ABC): # seconds, minutes, hours...
    pass

class Currency(abc.ABC):
    #Padrão de converção de moedas sem registro na API
    #1 libra = (1/1.20) dólar
    #1 dólar = 0.0074 iene
    #1 libra = ((1/1.20) * 0.0074) iene
    #1 libra = 0.0061666667 iene (aproximando para 7 casas decimais)
    
    """
    Avaible coins:
    BRL (Real Brasileiro)
    USD (Dollar)
    EUR (Euro)
    JPY (Japanese Yen)
    GBP (Pound Sterling)
    Franco Suíço (CHF)
    CAD (Canadian Dollar) 
    AUD (Australian Dollar) 
    Yuan (CNY)
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
    
    def USD2JPY(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/USD-JPY")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['USDJPY']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def USD2GBP(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/USD-GBP")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['USDGBP']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def USD2CHF(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/USD-CHF")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['USDCHF']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def USD2CAD(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/USD-CAD")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['USDCAD']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def USD2AUD(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/USD-AUD")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['USDAUD']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def USD2CNY(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/USD-CNY")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['USDCNY']['bid'])*amount
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
    
    def EUR2JPY(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-JPY")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['EURJPY']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def EUR2GBP(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-GBP")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['EURGBP']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def EUR2CHF(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-CHF")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['EURCHF']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def EUR2CAD(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-CAD")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['EURCAD']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def EUR2AUD(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-AUD")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['EURAUD']['bid'])*amount
                return f'{coin:.2f}'
            else:
                return "Connection ERROR"
        except:
            return "Conversion ERROR"

    def EUR2CNY(amount):
        try:    
            coin = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-CNY")
            if coin.status_code == 200:
                coin = json.loads(coin.content)
                coin = float(coin['EURCNY']['bid'])*amount
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
    
    def BRL2JPY(amount):
        pass

    def BRL2GBP(amount):
        pass

    def BRL2CHF(amount):
        pass

    def BRL2CAD(amount):
        pass

    def BRL2AUD(amount):
        pass

    def BRL2CNY(amount):
        pass

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