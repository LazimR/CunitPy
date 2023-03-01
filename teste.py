from libUnit import Temperature

tempCel = 15
tempFah = Temperature.celsius_to_farenheit(tempCel)

print(f'C°: {tempCel}')
print(f'F°: {tempFah}')

print('---------------')
tempFah = 99
tempCel = Temperature.celsius_to_farenheit(tempFah, 1)

print(f'F°: {tempFah}')
print(f'C°: {tempCel:0.2f}')