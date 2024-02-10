import matplotlib.pyplot as plt
import numpy as np

plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def bres(x1, y1, x2, y2):
    # Determine if the slope is steep
    is_steep = abs(y2 - y1) > abs(x2 - x1)

    # If the slope is steep, swap x and y coordinates
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Ensure the line is always drawn from left to right
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = abs(y2 - y1)
    error = dx / 2
    y_step = 1 if y1 < y2 else -1
    y = y1

    # Initialize the plotting points
    points = []

    for x in range(x1, x2 + 1):
        # Append points depending on the steepness of the slope
        points.append((y, x) if is_steep else (x, y))

        error -= dy
        if error < 0:
            y += y_step
            error += dx

    # Determine the size of the grid
    size_y = max(y1, y2) + 1 
    size_x = max(x1, x2) + 1 

    # Create a grid of zeros representing the coordinates
    grid = np.zeros((size_y, size_x))

    # Fill the grid with 1s at the coordinates
    for point in points:
        y, x = point
        if 0 <= y < size_y and 0 <= x < size_x:
            grid[y, x] = 1

    # Show the grid as an image with filled squares
    plt.imshow(grid, cmap='gray', origin='lower')

    # Add borders to the blocks
    for point in points:
        y, x = point
        if 0 <= y < size_y and 0 <= x < size_x:
            plt.plot([x - 0.5, x + 0.5, x + 0.5, x - 0.5, x - 0.5], 
                     [y - 0.5, y - 0.5, y + 0.5, y + 0.5, y - 0.5], color='black')

    plt.show()

def main():
    x1 = 1
    y1 = 1
    x2 = 8
    y2 = 4

    bres(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
