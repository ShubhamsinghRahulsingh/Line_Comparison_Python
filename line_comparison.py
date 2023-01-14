# Line Comparison using Class Method
import math


class Line:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calculate_length(self):
        line_length = math.sqrt((math.pow((self.x2-self.x1), 2) + math.pow((self.y2-self.y1), 2)))
        return line_length


if __name__ == '__main__':
    line1 = Line(10, 15, 25, 32)
    line1_length = line1.calculate_length()
    line2 = Line(10, 25, 25, 42)
    line2_length = line2.calculate_length()
    if line1_length == line2_length:
        print("Both the Lines are Equal")
    elif line1_length > line2_length:
        print("Line1 is greater than Line2")
    else:
        print("Line1 is less than Line2")

