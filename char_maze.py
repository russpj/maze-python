# char_maze.py
''' Implement a character-based maze generator'''

from sys import stdin, stdout, stderr, argv
from getopt import getopt, GetoptError
from time import process_time
from maze import Maze, Cell_Type


app_name = 'char_maze.py'


def print_map(maze_map):
    for row in range(maze_map.num_rows):
        for col in range(maze_map.num_columns):
            cell_type = maze_map.cell_type((row, col))
            if cell_type == Cell_Type.WALL:
                cell_ch = 'XX'
            elif cell_type == Cell_Type.TENTATIVE:
                cell_ch = '++'
            elif cell_type == Cell_Type.SOLUTION:
                cell_ch = '()'
            else:
                cell_ch = '  '
            print(cell_ch, end='')
        print()


def main(arguments):
    program_name = app_name
    command_line_documentation = \
        f'{program_name} --help --verbose rows columns'
    verbose = False

    try:
        opts, args = getopt(arguments, "hv", ("help", "verbose"))
    except GetoptError as error:
        print(f'Invalid Arguments: {command_line_documentation}')
        exit(2)

    for opt, arg in opts:	
        if opt in ('-h', '--help'):
            print(f'usage: {command_line_documentation}')
            exit(0)

        if opt in ('-v', '--verbose'):
            verbose = True

    if len(args) != 2:
        print(f'Invalid Arguments: {command_line_documentation}')
        exit(2)
    rows = int(args[0])
    columns = int(args[1])

    time_start = process_time()
    if verbose:
        print(f'{program_name} with columns={columns}, rows={rows}')

    maze = Maze(rows, columns)
    maze.create_maze_dfs(verbose)
    map = maze.maze_map()
    print_map(map)

    time_end = process_time()
    print(f'Time taken: {time_end - time_start} seconds.')

    return


if __name__ == '__main__':
    if len(argv[1:]) == 0:
        command_line = input(f'enter command line for {app_name}: ')
        argv.extend(command_line.split())
    main(argv[1:])