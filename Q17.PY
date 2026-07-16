numbers = [7, 4, 0, -2, 3]
print(numbers)
try:
    idx = int(input("Enter an index: "))
    print("Value at index", idx, "is", numbers[idx])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")
