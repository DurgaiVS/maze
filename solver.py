import curses
from curses import wrapper
import queue
import time
from stack import Stack
from gen import Maze


# printing the maze to terminal
def print_maze(maze: list, stdscr: object, path: list = []) -> None:
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "-", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)


# returns the start co-ordination
def find_start(maze: list, start: str) -> tuple:
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return (i, j)
    return None


def find_path(maze: list, stdscr: object, algo: int) -> None:
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    if algo in algorithm:
        q = algorithm[algo]()
    else:
        q = algorithm[1]()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        curr_pos, path = q.get()
        row, col = curr_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()
        time.sleep(0.2)

        if maze[row][col] == end:
            # stdscr.clear()
            # print_maze(maze, stdscr, path)
            # stdscr.refresh()
            return path

        neighbours = find_neighbour(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue

            r, c = neighbour
            if maze[r][c] == "#":
                continue
            else:
                # path.append(neighbour)
                new_path = path + [neighbour]
                q.put((neighbour, new_path))
                visited.add(neighbour)


# returns the available neighbours
def find_neighbour(maze: list, row: int, col: int) -> list:
    neighbours = []

    if row > 0:  # up
        neighbours.append((row-1, col))
    if row + 1 < len(maze):  # down
        neighbours.append((row+1, col))
    if col > 0:  # left
        neighbours.append((row, col-1))
    if col + 1 < len(maze):  # right
        neighbours.append((row, col+1))

    return neighbours


def main(stdscr):  # standard output screen

    # algorithm to use
    global algorithm
    algorithm = {
        1: queue.Queue,  # this is breadth-first algo
        2: Stack        # this is depth-first algo
    }

    maze = Maze(15, 15)
    maze1 = maze.create_maze()

    # The maze to be solved
    maze2 = [
        ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
    ]

    # initialising colors
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze1, stdscr, 1)

    # storing colors in variable
    # blue_and_black = curses.color_pair(1)

    # clearing the terminal
    # stdscr.clear()

    # adding input to terminal with co-ordinates
    # stdscr.addstr(0, 0, "Hii man", blue_and_black)
    # stdscr.addstr(1, 0, "Hello man")

    # print_maze(maze, stdscr)

    # refreshing the screen to udpate the value
    # stdscr.refresh()

    # terminating the function when user presses any key
    stdscr.getch()


wrapper(main)
