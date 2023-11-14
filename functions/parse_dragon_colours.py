from functions.get_colour_number import get_colour_number

def parse_dragon_colours(dragons):
    # get primary number
    dragons["pri_num"] = dragons.apply(lambda row: get_colour_number(row["pri"]), axis = 1)
    # get secondary number
    dragons["sec_num"] = dragons.apply(lambda row: get_colour_number(row["sec"]), axis = 1)
    # get tertiary number
    dragons["tert_num"] = dragons.apply(lambda row: get_colour_number(row["tert"]), axis = 1)
    return dragons
