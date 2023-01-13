import math


def calculate_length(x1, x2, y1, y2):
    """
        This function calculates length of a line
    :return: None
    """
    line_length = math.sqrt((math.pow((x2-x1), 2) - math.pow((y2-y1), 2)))
    print("Length of a Line:", line_length)


if __name__ == '__main__':
    x1 = int(input("Enter the value of First x co-ordinate: "))
    x2 = int(input("Enter the value of Second x co-ordinate: "))
    y1 = int(input("Enter the value of First y co-ordinate: "))
    y2 = int(input("Enter the value of second y co-ordinate: "))
    calculate_length(x1, y1, x2, y2)
