import math

# Prompt the user to enter a valid number of elements for the array
while True:
    n = input("Enter the number of elements in the array: ")
    if n.isnumeric() and n != '0' :
        n = int(n)
        break
    else:
        print("\t\tInvalid input! Please enter a valid integer.")

# Initialize variables
i = total = 0
array = []

# Collect valid numbers from the user to populate the array
while i < n:
    num = input(f"Enter number {i+1}: ")
    if num.isnumeric():
        array.append(int(num))
        total +=array[i]
        i += 1
    else:
        print(f"Invalid input! - '{num}' Please enter a valid integer.")
avg = total / n 


# Calculate the variance (sum of squared differences from the mean)
variance = sum((x - avg) ** 2 for x in array)

# Calculate the standard deviation
sd = math.sqrt(variance / n)

print(f"\nThe standard deviation of the entered numbers is: {sd}")