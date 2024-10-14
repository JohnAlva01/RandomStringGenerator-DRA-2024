def increment_recursive(lst, index):
    # Base case: If index is less than 0, stop the recursion (no more digits to increment)
    if index < 0:
        return
    
    # Increment the current element
    if lst[index] < 9:
        lst[index] += 1  # If the current element is less than 9, increment and stop
    else:
        lst[index] = 0  # Reset the current element to 0
        increment_recursive(lst, index - 1)

numbers = [0] * 5  # Example: list of 5 integers, all starting at 0

# Loop to simulate the increments (just an example)
for _ in range(200):  # Run it 200 times to see the process
    print(numbers)
    increment_recursive(numbers, len(numbers) - 1)  # S