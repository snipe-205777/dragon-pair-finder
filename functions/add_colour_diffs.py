from functions.get_colour_diff import get_colour_diff

def add_colour_diffs(dragons, pri, sec, tert):
    # get diff between each colour and goal
    dragons["pri_diff"] = dragons.apply(lambda row: get_colour_diff(row["pri_num"], pri), axis = 1)
    dragons["sec_diff"] = dragons.apply(lambda row: get_colour_diff(row["sec_num"], sec), axis = 1)
    dragons["tert_diff"] = dragons.apply(lambda row: get_colour_diff(row["tert_num"], tert), axis = 1)

    return dragons
