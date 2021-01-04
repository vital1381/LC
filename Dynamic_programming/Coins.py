def minimum_coins(coins, value):
    dp = [float('inf')] * (value + 1)
    dp[0] = 0

    for i in range(1, value + 1):
        min_c = float('inf')
        for c in coins:
            if i - c >= 0:
                vc = dp[i - c]
                if vc < min_c:
                    min_c = vc

        dp[i] = min_c + 1

    return dp[value]


if __name__ == '__main__':
    coins = [1, 10, 14]
    a = 25
    print(minimum_coins(coins, a))
