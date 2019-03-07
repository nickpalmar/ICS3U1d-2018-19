from math import pi

def cylinder_vol(radius, height):
    return (pi * radius**2 * height)

def cone_vol(radius, height):
    return(1/3 * pi * radius**2 * height)

def sphere_vol(radius):
    return(4/3 * pi * radius**3)

def main():
    print("The volume of the cylinder is", round(cylinder_vol(radius, height), 1))
    print("The volume of the cone is", round(cone_vol(radius, height), 1))
    print("The volume of the sphere is", round(sphere_vol(radius), 1))

radius = int(input("Enter the radius: "))
height = int(input("Enter the volume: "))

main()