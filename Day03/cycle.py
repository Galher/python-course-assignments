import sys
import math

if len(sys.argv) != 2:
    print("please provide the radius as a command line argument")
    sys.exit(1)

radius = float(sys.argv[1])
if radius <= 0:
    print("please provide a positive number")
    sys.exit(1)

print("Hello, lets calculate the area and the circumference of a circle")
area = math.pi * radius ** 2
print("The area of the circle with radius", radius, "is:", area)
print("The circumference of the circle with radius", radius, "is:", 2 * math.pi * radius)
