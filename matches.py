from colours import colours
from functions.colour_range import colour_range
from functions.get_goal_colour import get_goal_colour
from functions.get_match_dragon import get_match_dragon
from functions.prepare_dragons import prepare_dragons
from functions.range_compatible import range_compatible
from functions.test_for_relation import test_for_relation


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
