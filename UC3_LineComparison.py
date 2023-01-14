import math


def calculate_length(x1, x2, y1, y2):
    """
        This function calculates length of a line
    :return: Length of line
    """
    line_length = math.sqrt((math.pow((x2-x1), 2) + math.pow((y2-y1), 2)))
    return line_length


if __name__ == '__main__':
    lengths = []
    for i in range(1, 3):
        print(f"For Line{i}:")
        x1 = int(input("Enter the value of First x co-ordinate: "))
        x2 = int(input("Enter the value of Second x co-ordinate: "))
        y1 = int(input("Enter the value of First y co-ordinate: "))
        y2 = int(input("Enter the value of second y co-ordinate: "))
        length_of_line = calculate_length(x1, x2, y1, y2)
        lengths.append(length_of_line)
    if lengths[0] == lengths[1]:
        print("Line1 and Line2 both are Equal")
    elif lengths[0] > lengths[1]:
        print("Line1 is greater than Line2")
    else:
        print("Line1 is less than Line2")

