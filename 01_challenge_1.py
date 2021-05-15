"""El área de un triángulo se describe de la siguiente manera: A = (b * h) / 2 .
Escribe un programa que tome la base y la altura como parámetros y calcule el área del triángulo.
"""

base = 20
height = 50
    
def main():
    area = calc_area()
    print(f"The triangle's area is: {area} square cm")

def calc_area():
    area = (base * height) / 2
    return area


if __name__ == '__main__':
    main()





