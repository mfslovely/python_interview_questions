def convert_numbers(numbers):
    formatted_numbers = []  # Create an empty list to store the formatted strings
    
    for number in numbers:
        # Use Python's built-in format function to add commas as thousand separators
        formatted_number = '{:,}'.format(number)
        formatted_numbers.append(formatted_number)  # Append the formatted string to the list
    
    return formatted_numbers

# Example usage:
numbers = [1000000, 2356989, 2354672, 9878098]
formatted_numbers = convert_numbers(numbers)
print(formatted_numbers)

