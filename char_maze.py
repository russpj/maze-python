#!/usr/bin/env python3

# char_maze.py
''' Implement a character-based maze generator'''

from sys import stdin, stdout, stderr, argv
from getopt import getopt, GetoptError
from time import process_time
from maze import Maze, Cell_Type
import png


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


def get_png_rows(maze_map, target_width):
    output = []
    scale = target_width//max(maze_map.num_rows, maze_map.num_columns)
    for row in range(maze_map.num_rows*scale):
        output_row = []
        for col in range(maze_map.num_columns*scale):
            cell_type = maze_map.cell_type((row//scale, col//scale))
            if cell_type == Cell_Type.WALL:
                output_row.append(0)
            else:
                output_row.append(1)
        output.append(output_row)
    return output



def main(arguments):
    program_name = app_name
    command_line_documentation = \
        f'{program_name} --help --verbose [--png file_name] rows columns'
    verbose = False
    png_filename = None

    try:
        opts, args = getopt(arguments, "hvp:", ("help", "verbose", "png="))
    except GetoptError as error:
        print(f'Invalid Arguments: {command_line_documentation}')
        exit(2)

    for opt, arg in opts:	
        if opt in ('-h', '--help'):
            print(f'usage: {command_line_documentation}')
            exit(0)

        if opt in ('-v', '--verbose'):
            verbose = True

        if opt in ('-p', '--png'):
            png_filename = arg

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
    if png_filename:
        if verbose:
            print(f'output to {png_filename}')
        picture_rows = get_png_rows(map, 8*96)
        image = png.from_array(picture_rows, "L;1")
        image.save(png_filename)
    else:
       print_map(map)

    time_end = process_time()
    print(f'Time taken: {time_end - time_start} seconds.')

    return


if __name__ == '__main__':
    if len(argv[1:]) == 0:
        command_line = input(f'enter command line for {app_name}: ')
        argv.extend(command_line.split())
    main(argv[1:])