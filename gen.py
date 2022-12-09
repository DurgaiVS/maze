import random


class Maze:

    class Cell:

        def __init__(self) -> None:
            self.visited = False
            self.value = " "

    def __init__(self, row: int, col: int = None) -> None:
        if col == None:
            col = row
        self.row = (row * 2) - 1
        self.col = (col * 2) - 1
        self.path = []
        self.temp = []
        self.stack = []
        self.prev = None
        self.curr = None
        self.start = 0

        self.init_maze()

    def create_maze(self) -> list[list]:
        self.maze_gen()

        return self.maze

    def init_maze(self) -> None:

        self.maze = [["#"] * self.col for i in range(self.row)]

        for i in range(0, self.row, 2):
            for j in range(0, self.col, 2):
                self.maze[i][j] = self.Cell()

    def path_break(self) -> None:
        if self.prev == None:
            return
        else:
            if self.prev[0] == self.curr[0]:
                self.maze[self.prev[0]][max(
                    self.prev[1], self.curr[1]) - 1] = " "
            else:
                self.maze[
                    max(self.prev[0], self.curr[0]) - 1][self.prev[1]] = " "

    def push_temp(self, row_p: int, col_p: int) -> None:
        if row_p - 2 >= 0 and not self.maze[row_p - 2][col_p].visited:
            self.temp.append((row_p - 2, col_p))
        if col_p - 2 >= 0 and not self.maze[row_p][col_p - 2].visited:
            self.temp.append((row_p, col_p - 2))
        if row_p + 2 < self.row and not self.maze[row_p + 2][col_p].visited:
            self.temp.append((row_p + 2, col_p))
        if col_p + 2 < self.col and not self.maze[row_p][col_p + 2].visited:
            self.temp.append((row_p, col_p + 2))

    def push_stack(self) -> None:
        while len(self.temp):
            val = random.randint(0, len(self.temp) - 1)
            self.stack.append(self.temp[val])
            del self.temp[val]

    def maze_arrange(self) -> None:

        row_p = self.curr[0]
        col_p = self.curr[1]

        cell = self.maze[row_p][col_p]

        if cell.visited:
            return

        cell.visited = True
        self.path.append((row_p, col_p))

        self.path_break()

        self.push_temp(row_p, col_p)

        self.push_stack()

    def maze_gen(self, row: int = 0, col: int = 0) -> None:
        row = row if row % 2 == 0 else row * 2
        col = col if col % 2 == 0 else col * 2

        self.curr = (row, col)
        self.maze_arrange()

        while len(self.stack):
            self.prev = self.curr
            self.curr = self.stack.pop()
            self.maze_arrange()

        for i in range(self.row):
            for j in range(self.col):
                if isinstance(self.maze[i][j], self.Cell):
                    self.maze[i][j] = " "

        self.build_wall()

    def build_wall(self) -> None:
        self.maze.insert(0, ["#"] * self.col)
        self.maze.append(["#"] * self.col)
        self.maze[0][self.start] = "O"
        self.maze[-1][-1] = "X"

        for i in range(len(self.maze)):
            self.maze[i].insert(0, "#")
            self.maze[i].append("#")


# x = Maze(10, 10)
# mat = x.create_maze()
# for i in range(len(mat)):
#     print(mat[i])
