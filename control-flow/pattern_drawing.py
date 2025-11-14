# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
row = 0
while row < size:
    # Use for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    # Move to the next row after completing the current row
    print()
    row += 1