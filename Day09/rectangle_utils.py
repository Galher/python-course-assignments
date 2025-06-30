def calculate_area(height, width):
    """
    Calculate the area of a rectangle.

    >>> calculate_area(4, 5)
    20.0
    >>> calculate_area(3.5, 2)
    7.0
    """
    return height * width


def calculate_perimeter(height, width):
    """
    Calculate the perimeter of a rectangle.

    >>> calculate_perimeter(4, 5)
    18.0
    >>> calculate_perimeter(3.5, 2)
    11.0
    """
    return 2 * (height + width)
