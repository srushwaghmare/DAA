def is_subset_sum(set, target_sum):
    # Initialize a dp array with False
    dp = [False] * (target_sum + 1)

    # Base case: There is always a way to get a sum of 0 (by choosing no elements)
    dp[0] = True

    # Loop through each element in the set
    for num in set:
        # Update the dp array backwards to avoid overwriting results from the same step
        for i in range(target_sum, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    # The result will be stored in dp[target_sum]
    return dp[target_sum]


# Example usage
set1 = [3, 34, 4, 12, 5, 2]
sum1 = 9
print(f"Is subset with sum {sum1} possible:", is_subset_sum(set1, sum1))  # Output: True

set2 = [3, 34, 4, 12, 5, 2]
sum2 = 30
print(f"Is subset with sum {sum2} possible:", is_subset_sum(set2, sum2))  # Output: False
