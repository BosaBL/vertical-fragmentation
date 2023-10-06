def fragment(
    use_matrix: list[int],
    freq_matrix: list[int],
    ca_matrix: list[int],
    order: list[int],
    freq_sum: list[int],
):
    fragment_candidates = []

    for i in range(len(order) - 1):
        up_set = order[: i + 1]
        bot_set = order[i + 1 :]

        ctq = 0
        cbq = 0
        coq = 0

        # Check for querys that are only on the upper set.
        for q_num, query in enumerate(use_matrix):
            flag = True
            for attribute_idx in range(len(query)):
                if attribute_idx not in up_set and query[attribute_idx] == 1:
                    flag = False
                    break
            if flag == True:
                ctq += freq_sum[q_num]

        # Check for querys that are only on the bottom set.
        for q_num, query in enumerate(use_matrix):
            flag = True
            for attribute_idx in range(len(query)):
                if attribute_idx in up_set and query[attribute_idx] == 1:
                    flag = False
                    break
            if flag == True:
                cbq += freq_sum[q_num]

        # Check for querys that have both cases at the same times.
        for q_num, query in enumerate(use_matrix):
            flag_one = False
            flag_two = False
            for attribute_idx in range(len(query)):
                if attribute_idx in up_set and query[attribute_idx] == 1:
                    flag_one = True
                if attribute_idx in bot_set and query[attribute_idx] == 1:
                    flag_two = True

            if flag_one == True and flag_two == True:
                coq += freq_sum[q_num]

        value = ctq * cbq - coq**2
        fragment_candidates.append([value, up_set, bot_set])

    best_fragment = max(fragment_candidates, key=lambda x: x[0])

    for i in range(1, 3):
        if 0 not in best_fragment[i]:
            best_fragment[i].append(0)

    best_fragment[1].sort()
    best_fragment[2].sort()

    return (best_fragment[1], best_fragment[2])
