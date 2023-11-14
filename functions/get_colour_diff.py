def get_colour_diff(colour, goal_colour):
    difference = colour - goal_colour
    if difference >= 0:
        if difference < 89:
            return difference
        return difference - 177
    if difference > -89:
        return difference
    return difference + 177
