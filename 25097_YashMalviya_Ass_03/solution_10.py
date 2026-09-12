# Create 5x5 grid filled with "."
grid = [["." for col in range(5)] for row in range(5)]

# Place food
grid[2][3] = "F"

# Take snake coordinates
row = int(input("Enter row: "))
col = int(input("Enter column: "))

# Place snake
grid[row][col] = "S"

if row == 2 and col == 3:
    print("Yum! The snake ate the food!")

for row in grid:
    print(" ".join(row))