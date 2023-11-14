def colour_range(colour_1, colour_2):
    no_loop = abs(colour_1 - colour_2)
    if no_loop > 88:
        return 176 - no_loop + 2
    return no_loop + 1
