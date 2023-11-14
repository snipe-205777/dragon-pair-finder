import pandas as pd
from functions.add_colour_diffs import add_colour_diffs
from functions.parse_dragon_colours import parse_dragon_colours

def prepare_dragons(pri, sec, tert):
    dragons = pd.read_csv("dragons.csv", header=0, skipinitialspace=True)
    dragons = dragons.fillna("")
    dragons = parse_dragon_colours(dragons)
    dragons = add_colour_diffs(dragons, pri, sec, tert)
    return dragons
