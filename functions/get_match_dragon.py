def get_match_dragon(dragons):
    match_dragon_found = False

    while not match_dragon_found:
        input_id = int(input("What is the ID of the dragon you would like to match? "))

        if dragons[dragons["id"] == input_id].empty:
            print("Dragon not found. Try again")
        else:
            # get info of dragon to match
            return dragons[dragons["id"] == input_id].reset_index(drop=True).loc[0]
