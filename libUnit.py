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
            return True
        except ValueError:
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
            return temp * 9/5 + 32

    def celsius2kelvin(temp):
        if Verify.checkValue(temp):
            return temp + 273.15 
    
    def fahr2celsius(temp):
        if Verify.checkValue(temp):
            return (temp - 32) * 5/9
    
    def fahr2kelvin(temp):
        if Verify.checkValue(temp):
            return (temp - 32) * 5/9 + 273.15

    def kelvin2celsius(temp):
        if Verify.checkValue(temp):
            return temp - 273.15

    def kelvin2fahr(temp):
        if Verify.checkValue(temp):
            return (temp - 273.15) * 9/5 + 32

class Length(abc.ABC):
    '''
    This class represents the length measurement units: nanometer, micrometer
    millimeter, centimeter, meter, kilometer, inch, yard, feet and mile.
    It contains conversion methods between theses units and returns float number
    as the calculations results.
    '''

    # Nanometer
    def nanometer2micrometer(length):
        if Verify.checkValue(length):
            return length / 1000
            
    def nanometer2millimeter(length):
        if Verify.checkValue(length):
            return length / 10**6
            
    def nanometer2centimeter(length):
        if Verify.checkValue(length):
            return length / 10**7
            
    def nanometer2meter(length):
        if Verify.checkValue(length):
            return length / 10**9
            
    def nanometer2kilometer(length):
        if Verify.checkValue(length):
            return length / 10**12
                
    def nanometer2inch(length):
        if Verify.checkValue(length):
            return length / 2.54*10**7
            
    def nanometer2feet(length):
        if Verify.checkValue(length):
            return length / 3.048*10**8
            
    def nanometer2yard(length):
        if Verify.checkValue(length):
            return length / 9.144*10**8
                
    def nanometer2mile(length):
        if Verify.checkValue(length):
            return length / 1.609*10**12
            
    
    # Micrometer
    def micrometer2nanometer(length):
        if Verify.checkValue(length):
            return length * 1000
                
    def micrometer2millimeter(length):
        if Verify.checkValue(length):
            return length / 1000
            
    def micrometer2centimeter(length):
        if Verify.checkValue(length):
            return length / 10000
                
    def micrometer2meter(length):
        if Verify.checkValue(length):
            return length / 10**6
            
    def micrometer2kilometer(length):
        if Verify.checkValue(length):
            return length / 10**9
            
    def micrometer2inch(length):
        if Verify.checkValue(length):
            return length / 25400
            
    def micrometer2feet(length):
        if Verify.checkValue(length):
            return length / 304800
                
    def micrometer2yard(length):
        if Verify.checkValue(length):
            return length / 914400
            
    def micrometer2mile(length):
        if Verify.checkValue(length):
            return length / 1.609*10**9
            
    # Millimeter
    def millimeter2nanometer(length):
        if Verify.checkValue(length):
            return length * 10**6

    def millimeter2micrometer(length):
        if Verify.checkValue(length):
            return length * 1000

    def millimeter2centimeter(length):
        if Verify.checkValue(length):
            return length / 10
    
    def millimeter2meter(length):
        if Verify.checkValue(length):
            return length / 1000

    def millimeter2kilometer(length):
        if Verify.checkValue(length):
            return length / 10**6

    def millimeter2inch(length):
        if Verify.checkValue(length):
            return length / 25.4

    def millimeter2feet(length):
        if Verify.checkValue(length):
            return length / 304.8

    def millimeter2yard(length):
        if Verify.checkValue(length):
            return length / 914.4

    def millimeter2mile(length):
        if Verify.checkValue(length):
            return length / 1609*10**6

    # Centimeter
    def centimeter2nanometer(length):
        if Verify.checkValue(length):
            return length * 10**7
    
    def centimeter2micrometer(length):
        if Verify.checkValue(length):
            return length * 10000

    def centimeter2millimeter(length):
        if Verify.checkValue(length):
            return length * 10

    def centimeter2meter(length):
        if Verify.checkValue(length):
            return length / 100
    
    def centimeter2kilometer(length):
        if Verify.checkValue(length):
            return length / 100000

    def centimeter2inch(length):
        if Verify.checkValue(length):
            return length / 2.54
    
    def centimeter2feet(length):
        if Verify.checkValue(length):
            return length / 30.48

    def centimeter2yard(length):
        if Verify.checkValue(length):
            return length / 91.44
    
    def centimeter2mile(length):
        if Verify.checkValue(length):
            return length / 160900

    # Meter
    def meter2nanometer(length):
        if Verify.checkValue(length):
            return length * 0.000000001
                
    def meter2micrometer(length):
        if Verify.checkValue(length):
            return length * 0.000001
                
    def meter2millimeter(length):
        if Verify.checkValue(length):
            return length * 1000
            
    def meter2centimeter(length):
        if Verify.checkValue(length):
            return length * 100
            
    def meter2kilometer(length):
        if Verify.checkValue(length):
            return length / 1000
                
    def meter2inch(length):
        if Verify.checkValue(length):
            return length * 3.28084
                
    def meter2feet(length):
        if Verify.checkValue(length):
            return length * 3.28084
            
    def meter2yard(length):
        if Verify.checkValue(length):
            return length * 109361
                
    def meter2mile(length):
        if Verify.checkValue(length):
            return length * 1609
            
    # Kilometer
    

class Mass(abc.ABC): # mg, g, kg, short ton, metric ton, oz, lbs, stone...
    pass

class Time(abc.ABC): # seconds, minutes, hours...
    def sec2min(time):
        return time/60
    
    def sec2hr(time):
        return time/3600
    
    def min2sec(time):
        return time*60

    def min2hr(time):
        return time/60

    def hr2sec(time):
        return time*3600

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

    #DOLLAR
    def USD2BRL(amount):
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
    
    #EURO
    def EUR2BRL(amount):
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
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

    #REAL
    def BRL2USD(amount):
        if Verify.checkValue(amount):
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
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/BRL-JPY")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['BRLJPY']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def BRL2GBP(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/BRL-GBP")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['BRLGBP']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def BRL2CHF(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/BRL-CHF")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['BRLCHF']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def BRL2CAD(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/BRL-CAD")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['BRLCAD']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def BRL2AUD(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/BRL-AUD")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['BRLAUD']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def BRL2CNY(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/BRL-CNY")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['BRLCNY']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
    
    def BRL2EUR(amount):
        if Verify.checkValue(amount):
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
        
    #Iene Japônes
    def JPY2USD(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['JPYUSD']['bid'])*amount/100
                    return f'{coin:.4f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
        else:
            return "Bah"
        
    def JPY2EUR(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-EUR")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['JPYEUR']['bid'])*amount/100
                    return f'{coin:.4f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def JPY2BRL(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-BRL")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['JPYBRL']['bid'])*amount/100
                    return f'{coin:.4f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
            
    def JPY2GBP(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['JPYUSD']['bid'])/100
                    c2 = float((json.loads(c2.content))['GBPUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.4f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def JPY2CHF(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['JPYUSD']['bid'])/100
                    c2 = float((json.loads(c2.content))['CHFUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.4f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def JPY2CAD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['JPYUSD']['bid'])/100
                    c2 = float((json.loads(c2.content))['CADUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.4f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def JPY2AUD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['JPYUSD']['bid'])/100
                    c2 = float((json.loads(c2.content))['AUDUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.4f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def JPY2CNY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['JPYUSD']['bid'])/100
                    c2 = float((json.loads(c2.content))['CNYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.4f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
        
    #Libra Esterlina
    def GBP2USD(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['GBPUSD']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
        
    def GBP2EUR(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-EUR")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['GBPEUR']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def GBP2BRL(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-BRL")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['GBPBRL']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
            
    def GBP2JPY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['GBPUSD']['bid'])
                    c2 = float((json.loads(c2.content))['JPYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def GBP2CHF(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['GBPUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CHFUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def GBP2CAD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['GBPUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CADUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def GBP2AUD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['GBPUSD']['bid'])
                    c2 = float((json.loads(c2.content))['AUDUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def GBP2CNY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['GBPUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CNYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    #Franco Suiço
    def CHF2USD(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['CHFUSD']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
        
    def CHF2EUR(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-EUR")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['CHFEUR']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def CHF2BRL(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-BRL")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['CHFBRL']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
            
    def CHF2GBP(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CHFUSD']['bid'])
                    c2 = float((json.loads(c2.content))['GBPUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def CHF2JPY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CHFUSD']['bid'])
                    c2 = float((json.loads(c2.content))['JPYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def CHF2CAD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CHFUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CADUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def CHF2AUD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CHFUSD']['bid'])
                    c2 = float((json.loads(c2.content))['AUDUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def CHF2CNY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CHFUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CNYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    #Dollar Canadense
    def CAD2USD(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['CADUSD']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
        
    def CAD2EUR(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-EUR")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['CADEUR']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def CAD2BRL(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-BRL")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['CADBRL']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
            
    def CAD2GBP(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CADUSD']['bid'])
                    c2 = float((json.loads(c2.content))['GBPUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"  

    def CAD2CHF(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CADUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CHFUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def CAD2JPY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CADUSD']['bid'])
                    c2 = float((json.loads(c2.content))['JPYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def CAD2AUD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CADUSD']['bid'])
                    c2 = float((json.loads(c2.content))['AUDUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def CAD2CNY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CADUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CNYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    #Dollar Australiano
    def AUD2USD(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['AUDUSD']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
        
    def AUD2EUR(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-EUR")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['AUDEUR']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def AUD2BRL(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-BRL")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['AUDBRL']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
            
    def AUD2GBP(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['AUDUSD']['bid'])
                    c2 = float((json.loads(c2.content))['GBPUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def AUD2CHF(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['AUDUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CHFUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def AUD2CAD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['AUDUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CADUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def AUD2JPY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['AUDUSD']['bid'])
                    c2 = float((json.loads(c2.content))['JPYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    def AUD2CNY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['AUDUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CNYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR" 

    #Yuan
    def CNY2USD(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['CNYUSD']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
        
    def CNY2EUR(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-EUR")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['CNYEUR']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def CNY2BRL(amount):
        if Verify.checkValue(amount):
            try:    
                coin = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-BRL")
                if coin.status_code == 200:
                    coin = json.loads(coin.content)
                    coin = float(coin['CNYBRL']['bid'])*amount
                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"
            
    def CNY2GBP(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CNYUSD']['bid'])
                    c2 = float((json.loads(c2.content))['GBPUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"  

    def CNY2CHF(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CHF-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CNYUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CHFUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def CNY2CAD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CNYUSD']['bid'])
                    c2 = float((json.loads(c2.content))['CADUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def CNY2AUD(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/AUD-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CNYUSD']['bid'])
                    c2 = float((json.loads(c2.content))['AUDUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"

    def CNY2JPY(amount):
        if Verify.checkValue(amount):
            try:    
                c1 = requests.get("http://economia.awesomeapi.com.br/json/last/CNY-USD")
                c2 = requests.get("http://economia.awesomeapi.com.br/json/last/JPY-USD")
                if c1.status_code == 200 and c1.status_code == 200:
                    c1 = float((json.loads(c1.content))['CNYUSD']['bid'])
                    c2 = float((json.loads(c2.content))['JPYUSD']['bid'])

                    if c1 > 1 and c2 > 1 or c1 < 1 and c2 < 1:
                        coin = (c1/c2)*amount
                    elif c1 < 1 and c2 > 1:
                        coin = (c1*(1/c2))*amount
                    else:
                        coin = ((1/c1)*c2)*amount

                    return f'{coin:.2f}'
                else:
                    return "Connection ERROR"
            except:
                return "Conversion ERROR"