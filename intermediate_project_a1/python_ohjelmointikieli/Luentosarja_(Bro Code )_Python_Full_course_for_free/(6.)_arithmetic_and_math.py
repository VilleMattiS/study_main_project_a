from math import pi , sqrt

"""
New 
Augmented assigment operators
a = a + b  <=>  a += b
a = a - b  <=>  a -= b
a = a * b  <=>  a *= b
a = a / b  <=>  a /= b
a = a ** b <=> a **= b
a = a % b <=> a %= b

AAO operations update the variables value on the left side to be the value on the right side.
Math package has alot of useful mathematical functions.
"""

#Circumference and area of a circle calculator 
radius = int(input("Please give radius of your circle: ")) 
circumference = 2 * pi*radius
area = pi * radius**2
print(f"The circumference of your circle, when rounded to two decimals is {round(circumference, 2)} and the area is {round(area, 2)}")


#The hypotenusa of a right triangle
print(" ")
print(" ")
left_side_right_triangle = int(input("Insert left side of a right triangle: "))
right_side_right_triangle = int(input("Insert right side of a right triangle: "))
hypotenusa = sqrt(pow(left_side_right_triangle, 2) + pow(right_side_right_triangle, 2))
print(f"The hypotenusa is {hypotenusa}")