"""El área de un triángulo se describe de la siguiente manera: A = (b * h) / 2 .

Escribe un programa que tome la base y la altura como parámetros y calcule el área del triángulo.

**Bonus: el programa debe determinar si el triángulo es isósceles, equilátero o escaleno**

isóceles: 2 lados iguales

equilátero: 3 lados iguales

escaleno: nigun lado igual

"""

base = 20
height = 50

def calc_area():
    area = (base * height) / 2
    return print(f"The triangle's area is: {area} square cm")
    
if __name__ == '__main__':
    calc_area()

