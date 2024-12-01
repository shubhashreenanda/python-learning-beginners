number = [1,2,3,4,5,6]

try:
    idx = int(input(f"Enter an index(0 to {len(number)-1}):"))
    print(f"The value at index {idx} is {number[idx]}")
except IndexError:
    print("Error: Index out of range.Please enter a valid index")
except ValueError:
    print("Error: Please enter a valid integer for the index")
