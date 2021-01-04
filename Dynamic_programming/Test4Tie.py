from typing import List, Any, Union


def equalSubSetSumPartition(s):
    if len(s) % 2 == 1:
        return []

    output = []
    for i in s:
        output.append(False)

    half_sum = sum(s) // 2

    def helper(i, sum):
        nonlocal s
        nonlocal output

        if sum == 0:
            return True

        if i == len(s):
            return False

        include = helper(i + 1, sum - s[i])
        exclude = helper(i + 1, sum)

        return include or exclude

    istie = helper(0, half_sum)
    return istie


def t4t(s):
    input_len = len(s)
    if input_len % 2 == 1:
        return False

    min_v = min(s)

    if min_v < 0:
        s1 = [item + (-min_v) for item in s]
    else:
        s1 = s

    target: int = sum(s1) // 2
    # init
    dp: List[List[int]] = [[0 for x in range(target + 1)] for x in range(input_len + 1)]

    for row in range(input_len + 1):
        dp[row][0] = True

    for col in range(1, target + 1):
        dp[-1][col] = False

    for i in range(input_len - 1, -1, -1):
        for sum_a in range(1, target + 1, 1):
            include_res = False

            if sum_a >= s1[i]:
                include_res = dp[i + 1][sum_a - s1[i]]

            dp[i][sum_a] = include_res or dp[i + 1][sum_a]

    result = traversal(s1, dp, target)
    return result


def traversal(input_array, dp, target):
    if not dp[0][target]:
        return []

    result = [False] * len(input_array)
    idx = 0

    while idx > 0 or target != 0:
        element = input_array[idx]

        left = False
        if target - element > 0:
            left = dp[idx + 1][target - element]

        right = dp[idx + 1][target]

        if left:
            result[idx] = True
            idx += 1
            target = target - element
            continue

        if right:
            result[idx] = False
            idx += 1
            continue

    return result


if __name__ == "__main__":
    s = [1, 2, 3, 4, 5, 7]
    # print(equalSubSetSumPartition())
    print(t4t(s))
