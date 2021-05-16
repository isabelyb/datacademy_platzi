"""Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen 
de un cilindro.

Recuerda que la base del cilindro es un círculo y necesitarás calcular su área. 
Aplica las fórmulas en tu programa recibiendo datos como altura y radio.
"""

import math

PI = math.pi
height = int(input("height: "))
radius = int(input("radius: "))
 

def main():
    result = vol_cil(height, radius)
    print(f"The cilinder's volume is: {result} cubic cm")

def vol_cil(height, radius):
    area = PI * (radius**2)
    result = round((area * height), 2)
    return result
    
if __name__ == '__main__':
    main()
    
    
    

