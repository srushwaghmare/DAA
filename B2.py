def maxProfit(arr):
    if not arr or len(arr) < 2:
        return 0  # No profit possible if there are fewer than 2 days

    min_price = arr[0]  # Initialize with the first day's price
    max_profit = 0  # Initialize max profit to zero

    # Loop through the array, starting from the second day
    for i in range(1, len(arr)):
        # Update min_price if current price is lower
        if arr[i] < min_price:
            min_price = arr[i]

        # Calculate current profit
        current_profit = arr[i] - min_price

        # Update max_profit if current profit is higher than previous max_profit
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit


# Example usage:
arr1 = [2, 3, 5]
arr2 = [5, 1]

print("Maximum Profit for arr1:", maxProfit(arr1))  # Output: 3 (Buy at 2, sell at 5)
print("Maximum Profit for arr2:", maxProfit(arr2))  # Output: 0 (No profit possible)
