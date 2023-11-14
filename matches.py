import pandas as pd
from colours import colours

def get_goal_colour(position):
    colour_found = False

    while not colour_found:
        colour_name = input(f"What is your goal {position} colour? ").lower()

        if colour_name in colours.keys():
            return colour_name
        else:
            print("Colour not found. Try again")

def get_match_dragon(dragons):
    match_dragon_found = False

    while not match_dragon_found:
        input_id = int(input("What is the ID of the dragon you would like to match? "))

        if dragons[dragons["id"] == input_id].empty:
            print("Dragon not found. Try again")
        else:
            # get info of dragon to match
            return dragons[dragons["id"] == input_id].reset_index(drop=True).loc[0]

def number_direction(number):
    if number == 0:
        return 0
    if number < 0:
        return -1
    return 1

def range_compatible(colour_diff_1, colour_diff_2):
    overall_direction = number_direction(colour_diff_1) + number_direction(colour_diff_2)
    if overall_direction == -2 or overall_direction == 2:
        return False
    if abs(colour_diff_1 - colour_diff_2) > 88:
        return False
    return True

def test_for_relation(match_family_tree, partner_family_tree):
    for char in match_family_tree:
        for character in partner_family_tree:
            if char == character:
                return True
    return False

def get_colour_number(colour):
    return colours[colour.lower()]

def colour_range(colour_1, colour_2):
    no_loop = abs(colour_1 - colour_2)
    if no_loop > 88:
        return 176 - no_loop + 2
    return no_loop + 1

def get_colour_diff(colour, goal_colour):
    difference = colour - goal_colour
    if difference >= 0:
        if difference < 89:
            return difference
        return difference - 177
    if difference > -89:
        return difference
    return difference + 177

def add_colour_diffs(dragons, pri, sec, tert):
    # get diff between each colour and goal
    dragons["pri_diff"] = dragons.apply(lambda row: get_colour_diff(row["pri_num"], pri), axis = 1)
    dragons["sec_diff"] = dragons.apply(lambda row: get_colour_diff(row["sec_num"], sec), axis = 1)
    dragons["tert_diff"] = dragons.apply(lambda row: get_colour_diff(row["tert_num"], tert), axis = 1)

    return dragons

def parse_dragon_colours(dragons):
    # get primary number
    dragons["pri_num"] = dragons.apply(lambda row: get_colour_number(row["pri"]), axis = 1)
    # get secondary number
    dragons["sec_num"] = dragons.apply(lambda row: get_colour_number(row["sec"]), axis = 1)
    # get tertiary number
    dragons["tert_num"] = dragons.apply(lambda row: get_colour_number(row["tert"]), axis = 1)
    return dragons

def prepare_dragons(pri, sec, tert):
    dragons = pd.read_csv("dragons.csv", header=0, skipinitialspace=True)
    dragons = dragons.fillna("")
    dragons = parse_dragon_colours(dragons)
    dragons = add_colour_diffs(dragons, pri, sec, tert)
    return dragons

def get_matches(dragons, match_dragon):
    # compare pri values
    dragons["pri_compatible"] = dragons.apply(lambda row: range_compatible(row["pri_diff"], match_dragon["pri_diff"]), axis = 1)
    # get total pri range
    dragons["pri_range"] = dragons.apply(lambda row: colour_range(row["pri_num"], match_dragon["pri_num"]), axis = 1)
    # compare sec values
    dragons["sec_compatible"] = dragons.apply(lambda row: range_compatible(row["sec_diff"], match_dragon["sec_diff"]), axis = 1)
    # get total sec range
    dragons["sec_range"] = dragons.apply(lambda row: colour_range(row["sec_num"], match_dragon["sec_num"]), axis = 1)
    # compare tert values
    dragons["tert_compatible"] = dragons.apply(lambda row: range_compatible(row["tert_diff"], match_dragon["tert_diff"]), axis = 1)
    # get total tert range
    dragons["tert_range"] = dragons.apply(lambda row: colour_range(row["tert_num"], match_dragon["tert_num"]), axis = 1)
    # get probability of outcome
    dragons["probability"] = dragons.apply(lambda row: round((1/row["pri_range"]) * (1/row["sec_range"]) * (1/row["tert_range"]), 4), axis = 1)
    # test if related
    dragons["related"] = dragons.apply(lambda row: test_for_relation(match_dragon["family_tree"], row["family_tree"]), axis = 1)

    # filter potential matches to opposite sex
    matches = dragons[dragons["sex"] != match_dragon["sex"]]

    # remove related dragons
    matches = matches[matches["related"] == False]

    # filter for compatible primary
    matches = matches[matches["pri_compatible"] == True]

    # filter for compatible secondary
    matches = matches[matches["sec_compatible"] == True]

    # filter for compatible tertiary
    matches = matches[matches["tert_compatible"] == True]

    # sort matches by probability
    matches = matches.sort_values(
        "probability", ascending=False, ignore_index=True)

    # reindex matches
    matches = matches.reset_index(drop=True)

    if matches.empty:
        print("\nNo matches were found")
    else:
        print("\n+-----------+------------------+-----+-----+------+--------+\n\
|    ID     |       NAME       | PRI | SEC | TERT |  PROB  |\n\
+-----------+------------------+-----+-----+------+--------+")

        for i in range(matches.shape[0]):
            partner = matches.loc[i]
            id = f"         {partner['id']}"[-9:]
            name = f"{partner['name']}                "[:16]
            pri = f"   {partner['pri_range']}"[-3:]
            sec = f"   {partner['sec_range']}"[-3:]
            tert = f"    {partner['tert_range']}"[-4:]
            prob = f"{partner['probability']}000000"[:6]

            print(f"| {id} | {name} | {pri} | {sec} | {tert} | {prob} |")

        print("+-----------+------------------+-----+-----+------+--------+")


if __name__ == "__main__":
    # pri = "black"
    # sec = "white"
    # tert = "fuchsia"

    pri = get_goal_colour("primary")
    sec = get_goal_colour("secondary")
    tert = get_goal_colour("tertiary")

    # get values for goal colours
    pri = colours[pri]
    sec = colours[sec]
    tert = colours[tert]

    dragons = prepare_dragons(pri, sec, tert)

    match_dragon = get_match_dragon(dragons)

    get_matches(dragons, match_dragon)
