import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume


radius=6
print("The volume of the sphere with radius "+str(radius)+" is:", sphere_volume(radius))