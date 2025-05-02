import math
import sys

if len(sys.argv) != 3:
    print("please provide the height and width as command line arguments")
    sys.exit(1)


print('Hello, lets calculate the area and the perimeter of a rectangle')
height = float(sys.argv[1])
width = float(sys.argv[2])
area = height * width
perimeter = 2 * (height + width)      
print("The area of the rectangle with height", height, "and width", width, "is:", area)
print("The perimeter of the rectangle with height", height, "and width", width, "is:", perimeter)

print("Goodbye!")