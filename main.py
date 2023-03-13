def find_smallest_number(numbers):
    # Initialize the smallest number as the first number in the list
    smallest = numbers[0]
    # Iterate through the list
    for num in numbers:
        # If the current number is smaller than the current smallest, update smallest
        if num < smallest:
            smallest = num
    # Return the smallest number
    return smallest

# Test the function with the input list
list1 = [5, 7, 9, 14, 10, 20, 4]
print(find_smallest_number(list1))
