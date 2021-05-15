"""Bonus: el programa debe determinar si el triángulo es isósceles, equilátero o escaleno
- isóceles: 2 lados iguales
- equilátero: 3 lados iguales  
- escaleno: nigun lado igual
- área de triángulo rectángulo = (lado a x lado b)/2
"""

base = 50
height = 15
side_a = 42

    
def main():
    total_area = calc_total_area()
    side_b = calc_hypotenuse_b()
    triangle_type = ""

    if side_a == side_b and side_b == base:
        triangle_type = "equilateral"
    elif side_a != side_b and side_b != base and side_a != base:
        triangle_type = "scalene"
    else:
        triangle_type = "isosceles"

    print(f"The triangle's area is: {total_area} square cm and is {triangle_type}")


def calc_total_area():
    total_area = (base * height) / 2
    return total_area


def calc_side_x():
    side_x = ((side_a**2) - (height**2))**0.5 
    return side_x


def calc_hypotenuse_b():
    side_y = base - calc_side_x()
    hypotenuse = ((side_y**2) + (height**2))**0.5
    hypotenuse_b = round(hypotenuse, 4)
    return hypotenuse_b


if __name__ == '__main__':
    main()


