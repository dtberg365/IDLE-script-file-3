def greaterThan(x, y):
    # Check if x is greater than y
    return x > y

# Main section of the program
a = 2
b = 3

# Call the function and store the result
result = greaterThan(a, b)

# Print the output
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

# Test the scenario with a = 10 and b = 6
a = 10
b = 6
result = greaterThan(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
