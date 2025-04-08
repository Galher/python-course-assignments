print("Hello, lets calculate the area and the circumference of a circle")
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle with radius", radius, "is:", area)
print("The circumference of the circle with radius", radius, "is:", 2 * math.pi * radius)
