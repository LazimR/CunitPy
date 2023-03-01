from libUnit import Temperature

tempCel = 15
tempFah = Temperature.cels_far(tempCel)

print(f'C°: {tempCel}')
print(f'F°: {tempFah}')

print('---------------')
tempFah = 99
tempCel = Temperature.cels_far(tempFah, 1)

print(f'F°: {tempFah}')
print(f'C°: {tempCel:0.2f}')