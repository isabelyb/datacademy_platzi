"""Bonus: agrega otras figuras geométricas a tu programa y que el usuario pueda escoger cuál calcular.
"""

import math

PI = math.pi
 

def main():   
    intro = """
    Select a geometric figure: 
    1 -> Cilinder
    2 -> Pyramid
    3 -> Cone
    4 -> Cube
    5 -> Sphere

    Option: """    

    option = int(input(intro)) 

    if option == 1:
        vol_cilinder()
    elif option == 2:
        vol_pyramid()
    elif option == 3:
        vol_cone()
    elif option == 4:
        vol_cube()
    elif option == 5:
        vol_sphere()
    else:
        print("Select a correct option")


def vol_cilinder():
    height = int(input("Type de cilinder's height in cm: "))
    radius = int(input("Type de cilinder's radius in cm: "))
    area = PI * (radius**2)
    vol_cil = round((area * height), 2)
    print(f"The cilinder's volume is: {vol_cil} cubic cm")

    
def vol_pyramid():
    side_a = int(input("Type de triangle's side_a in cm: "))
    side_b = int(input("Type de triangle's side_b in cm: "))
    height = int(input("Type de triangle's heigh in cm: "))
    vol_pyr = (side_a * side_b * height) / 3
    print(f"The triangle's volume is: {vol_pyr} cubic cm")

def vol_cone():
    radius = int(input("Type de cone's radius in cm: "))
    height = int(input("Type de cone's heigh in cm: "))
    vol_con = (PI * (radius**2) * height) / 3
    print(f"The cone's volume is: {vol_con} cubic cm")


def vol_cube():
    side_a = int(input("Type de cube's side_a in cm: "))
    side_b = int(input("Type de cube's side_b in cm: "))
    height = int(input("Type de cube's heigh in cm: "))
    vol_cub = side_a * side_b * height
    print(f"The cube's volume is: {vol_cub} cubic cm")


def vol_sphere():
    radius = int(input("Type de sphere's radius in cm: "))
    vol_sph = (4 * PI * (radius**3)) / 3
    print(f"The sphere's volume is: {vol_sph} cubic cm")


if __name__ == '__main__':
    main()