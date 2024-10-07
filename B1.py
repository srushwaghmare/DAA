def max_shops(S, E, K):
    # Create a list of tuples representing each shop's start and end time
    shops = sorted(zip(S, E), key=lambda x: x[1])

    # Initialize an array to keep track of the end times for each person
    person_end_times = [0] * K

    # Count the total number of shops that can be visited
    total_visits = 0

    # For each shop, try to assign it to one of the K people
    for shop in shops:
        start, end = shop

        # Try to assign the shop to a person optimally
        for i in range(K):
            if person_end_times[i] <= start:
                # If the person can visit this shop (i.e., no timing conflict)
                person_end_times[i] = end  # Update the person's end time
                total_visits += 1  # Increment the count of total visits
                break  # Move to the next shop as this shop is assigned

    return total_visits


# Take input from the user
def get_input():
    N = int(input("Enter the number of shops: "))  # Number of shops
    S = list(map(int, input("Enter the starting times of the shops: ").split()))
    E = list(map(int, input("Enter the ending times of the shops: ").split()))
    K = int(input("Enter the number of people (K): "))

    # Ensure the input sizes match
    if len(S) != N or len(E) != N:
        print("Error: The number of start and end times must be equal to the number of shops.")
        return

    # Calculate and print the result
    result = max_shops(S, E, K)
    print(f"The maximum number of shops that can be visited: {result}")


# Call the input function
get_input()



#Enter the number of shops: 5
#Enter the starting times of the shops: 1 8 3 2 6
#Enter the ending times of the shops: 5 10 6 5 9
#Enter the number of people (K): 2
#The maximum number of shops that can be visited: 4
