def count_ways_to_make_sum(coins, target_sum):
    # Create a dp array with size target_sum + 1, initialized to 0
    dp = [0] * (target_sum + 1)

    # Base case: There's one way to make sum 0 (by choosing no coins)
    dp[0] = 1

    # Iterate through each coin
    for coin in coins:
        # Update dp array for all sums from coin to target_sum
        for amount in range(coin, target_sum + 1):
            dp[amount] += dp[amount - coin]

    # The result will be in dp[target_sum]
    return dp[target_sum]


# Example usage
sum_value = 4
coins = [1, 2, 3]
print(f"Number of ways to make sum {sum_value}:", count_ways_to_make_sum(coins, sum_value))
