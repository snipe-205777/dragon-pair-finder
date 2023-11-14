from colours import colours

def get_goal_colour(position):
    colour_found = False

    while not colour_found:
        colour_name = input(f"What is your goal {position} colour? ").lower()

        if colour_name in colours.keys():
            return colour_name
        else:
            print("Colour not found. Try again")
