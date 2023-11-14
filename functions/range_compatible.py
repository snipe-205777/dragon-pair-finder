from functions.number_direction import number_direction

def range_compatible(colour_diff_1, colour_diff_2):
    overall_direction = number_direction(colour_diff_1) + number_direction(colour_diff_2)
    if overall_direction == -2 or overall_direction == 2:
        return False
    if abs(colour_diff_1 - colour_diff_2) > 88:
        return False
    return True
