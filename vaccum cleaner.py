import random

class VacuumCleaner:
    def __init__(self, grid_size):
        self.grid = [[random.choice(["clean", "dirty"]) for _ in range(grid_size)] for _ in range(grid_size)]
        self.pos = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]

    def print_grid(self):
        for row in self.grid:
            print(" ".join(row))
        print()

    def clean(self):
        row, col = self.pos
        if self.grid[row][col] == "dirty":
            print(f"Cleaning dirty cell at ({row}, {col})")
            self.grid[row][col] = "clean"
        else:
            print(f"Already clean at ({row}, {col})")

    def move_left(self):
        row, col = self.pos
        if col > 0:
            print("Moving left")
            self.pos[1] -= 1
        else:
            print("Already at the left edge")

    def move_right(self):
        row, col = self.pos
        if col < len(self.grid[0]) - 1:
            print("Moving right")
            self.pos[1] += 1
        else:
            print("Already at the right edge")

    def move_up(self):
        row, col = self.pos
        if row > 0:
            print("Moving up")
            self.pos[0] -= 1
        else:
            print("Already at the top edge")

    def move_down(self):
        row, col = self.pos
        if row < len(self.grid) - 1:
            print("Moving down")
            self.pos[0] += 1
        else:
            print("Already at the bottom edge")

def main():
    grid_size = 5
    vacuum = VacuumCleaner(grid_size)

    print("Initial Grid:")
    vacuum.print_grid()

    for _ in range(grid_size * grid_size):
        vacuum.clean()
        move = random.choice(["left", "right", "up", "down"])
        if move == "left":
            vacuum.move_left()
        elif move == "right":
            vacuum.move_right()
        elif move == "up":
            vacuum.move_up()
        elif move == "down":
            vacuum.move_down()

    print("\nFinal Grid:")
    vacuum.print_grid()

if __name__ == "__main__":
    main()
