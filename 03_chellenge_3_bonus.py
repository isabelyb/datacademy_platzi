
"""Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.
"""

def converter_distance(measure, conversor):
    distance = int(input("type the distance to convert: "))
    result = distance * conversor
    print(f"{result} {measure} ")

intro = """
What do you want to convert today? 

press 1 for miles to km
press 2 for km to miles

Option: """    

option = int(input(intro))

if option == 1:
    converter_distance("km", 1.609344)
else:
    converter_distance("miles", 0.621371)

