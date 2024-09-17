def stableMatching(n, menPreferences, womenPreferences):
    man_list = list(range(n))
    man_proposal_dict = {}

    woman_current_match_dict = {}

    while man_list:
        man = man_list.pop(0)

        man_proposal = man_proposal_dict.get(man, None)

        if man_proposal is None:
            man_proposal = set()
            man_proposal_dict[man] = man_proposal

        for woman in menPreferences[man]:
            if woman in man_proposal:
                continue

            current_match = woman_current_match_dict.get(woman, None)

            if current_match is None:
                woman_current_match_dict[woman] = man
                man_proposal.add(woman)
                man_proposal_dict[man] = man_proposal
                break

            current_match_index = womenPreferences[woman].index(current_match)
            current_man_index = womenPreferences[woman].index(man)

            if current_man_index < current_match_index:
                woman_current_match_dict[woman] = man
                man_proposal.add(woman)
                man_proposal_dict[man] = man_proposal
                man_list.append(current_match)
                break

    return convert_dict_to_list(woman_current_match_dict)


def convert_dict_to_list(d):
    array = [None] * (max(d.keys()) + 1)

    for key, value in d.items():
        array[value] = key

    return array


# You might want to test your implementation on the following two tests:
assert (stableMatching(1, [[0]], [[0]]) == [0])
assert (stableMatching(2, [[0, 1], [1, 0]], [[0, 1], [1, 0]]) == [0, 1])
assert (stableMatching(2, [[0, 1], [0, 1]], [[1, 0], [0, 1]]) == [1, 0])

# a   b
# c   d
