"""Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. 
Para no estar repitiendo este cálculo escribe un programa en que el usuario indique 
una cantidad de millas y en pantalla se muestre el resultado convertido a kilómetros.

Toma en cuenta que en cada milla hay 1.609344 Km

Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.
"""


def miles_to_km():
    miles = int(input("How many miles do you want ton convert into km? "))
    km = miles * 1.609344
    return print(f"{miles} miles are {km} km")

if __name__ == '__main__':
    miles_to_km()

#km = int(input("How many km?"))

    # km_to_miles = km * 0.621371

# def converter(miles):
#     pass


