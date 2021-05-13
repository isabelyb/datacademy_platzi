"""En tu programa pide al usuario ingresar 3 números: un límite inferior, 
un límite superior y uno de comparación.

Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.

En caso de estar por debajo del inferior o arriba del superior, también muéstralo en pantalla y
pide ingresar otro número para repetir el proceso.
"""
import random

def numbers():
    number_comp = random.choice(range(0, 100)) 
    number_min = int(input("insert an inferior limit: "))
    number_max = int(input("insert a superior limit: "))
    number_user = int(input("insert a number to compare: "))

    if number_comp == number_user:
        print(f"Congratulations, you guessed it!")
    elif number_comp >= number_min and number_comp <= number_max:
        print(f"My number was {number_comp}")
    else:
        print(f"My number was {number_comp} and is not in the range. Don't worry, let's go again!")
        numbers()

if __name__ == '__main__':
    numbers()