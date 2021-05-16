"""Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. 
Para no estar repitiendo este cálculo escribe un programa en que el usuario indique 
una cantidad de millas y en pantalla se muestre el resultado convertido a kilómetros.

Toma en cuenta que en cada milla hay 1.609344 Km
"""

miles = int(input("How many miles do you want to convert into km? "))


def main():
    km = miles_to_km()
    print(f"{miles} miles are {km} km")


def miles_to_km():
    km = miles * 1.609344
    return km


if __name__ == '__main__':
    main()

