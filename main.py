def rectangle_area(width, height):
    return height * width
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    def sum_digits(number):
        sum = 0
        for digit in str(number):
            sum += int(digit)
        return sum

        print(rectangle_area(145,209))
        print(is_even(43))
        print(is_even(35))
        print(sum_digits(34))