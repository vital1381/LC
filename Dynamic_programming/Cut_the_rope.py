def cut_the_rope(n):
    # 1 define
    table = [0] * (n + 1)

    # 2 init
    table[0] = 0
    table[1] = 1
    # 3 traversal, 2 -> k -> n, 1 -> k

    # 4 populatw
    for cur_len in range(2, n + 1):
        # max product for current length (size of the problem
        # start from 2 because 0, 1 are base cases - known cases
        max_p = 0
        for left in range(1, cur_len + 1):
            # left side and right side, left increasing, right decreasing
            right = cur_len - left

            # check what is max product for size of right side
            max_prev_cut = table[right]

            # take max of right side if to leave as is, or cut
            max_cut = max(right, max_prev_cut)
            # take prod of left side and max cut if right side
            prod = left * max_cut
            # max product for current length
            max_p = max(max_p, prod)
        # populate table for current length
        table[cur_len] = max_p

    return table[n]


if __name__ == "__main__":
    max_product = cut_the_rope(6)
    print(max_product)