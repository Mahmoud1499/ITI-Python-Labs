def triangle_area():
    base = float(input("Enter the base of the triangle: \n"))
    height = float(input("Enter the height of the triangle: \n"))
    
    area = 0.5 * base * height
    
    return area

print("The area of the triangle is:", triangle_area())
