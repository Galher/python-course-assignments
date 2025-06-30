import sys
from rectangle_utils import calculate_area, calculate_perimeter

if len(sys.argv) != 3:
    print("Please provide the height and width as command line arguments")
    sys.exit(1)

print("Hello, let's calculate the area and the perimeter of a rectangle")

height = float(sys.argv[1])
width = float(sys.argv[2])

area = calculate_area(height, width)
perimeter = calculate_perimeter(height, width)

print("The area of the rectangle with height", height, "and width", width, "is:", area)
print("The perimeter of the rectangle with height", height, "and width", width, "is:", perimeter)

print("Goodbye!")
