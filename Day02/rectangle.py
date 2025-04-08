print('Hello, lets calculate the area and the perimeter of a rectangle')
import math
height = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = height * width
perimeter = 2 * (height + width)      
print("The area of the rectangle with height", height, "and width", width, "is:", area)