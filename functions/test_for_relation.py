def test_for_relation(match_family_tree, partner_family_tree):
    for char in match_family_tree:
        for character in partner_family_tree:
            if char == character:
                return True
    return False
