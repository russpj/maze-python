#!/usr/bin/env python3

# char_maze.py
''' Implement a character-based maze generator'''

from sys import stdin, stdout, stderr, argv
from getopt import getopt, GetoptError
from time import process_time
from maze import Maze, Maze_Map, Cell_Type
import png


app_name = 'char_maze.py'


def print_map(maze_map, show_deadends = False):
    string_map = {Cell_Type.WALL: "XX",
                  Cell_Type.SOLUTION: "()",
                  Cell_Type.UNTOUCHED: "  ",
                  Cell_Type.DEADEND: "++"}
    if not show_deadends:
        string_map[Cell_Type.DEADEND] = string_map[Cell_Type.UNTOUCHED]
    
    for row in range(maze_map.num_rows):
        for col in range(maze_map.num_columns):
            cell_type = maze_map.cell_type((row, col))
            cell_ch = string_map[cell_type]
            print(cell_ch, end='')
        print()


def get_png_rows(maze_map: Maze_Map, target_width: int, color_map):
    output = []
    scale = target_width//max(maze_map.num_rows, maze_map.num_columns)
    for row in range(maze_map.num_rows*scale):
        output_row = []
        for col in range(maze_map.num_columns*scale):
            cell_type = maze_map.cell_type((row//scale, col//scale))
            output_row.extend(color_map[cell_type])
        output.append(output_row)
    return output


def make_image(map: Maze_Map, show_deadends = False) -> png.Image:
    color_map = {Cell_Type.WALL: [32, 0, 96],
                 Cell_Type.DEADEND: [192, 24, 24],
                 Cell_Type.SOLUTION: [0, 255, 0],
                 Cell_Type.UNTOUCHED: [255, 255, 255]}
    if not show_deadends:
        color_map[Cell_Type.DEADEND] = color_map[Cell_Type.UNTOUCHED]
    
    picture_rows = get_png_rows(map, 8*96, color_map)
    image = png.from_array(picture_rows, "RGB")
    return image


def main(arguments):
    program_name = app_name
    command_line_documentation = \
        (f'{program_name} --help --verbose  --solve '
        '--failures [--png file_name] rows columns')
    verbose = False
    solve = False
    show_failures = False
    png_filename = None

    try:
        opts, args = getopt(arguments, "hvsfp:", 
                            ("help", "verbose", "solve", "failures" "png="))
    except GetoptError as error:
        print(f'Invalid Arguments: {command_line_documentation}')
        exit(2)

    for opt, arg in opts:	
        if opt in ('-h', '--help'):
            print(f'usage: {command_line_documentation}')
            exit(0)

        if opt in ('-v', '--verbose'):
            verbose = True

        if opt in ('-s', '--solve'):
            solve = True

        if opt in ('-f', '--failures'):
            show_failures = True

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
    if solve:
        map.solve(verbose)

    if png_filename:
        if verbose:
            print(f'output to {png_filename}')
        image = make_image(map, show_deadends=show_failures)
        image.save(png_filename)
    else:
       print_map(map, show_deadends=show_failures)

    time_end = process_time()
    print(f'Time taken: {time_end - time_start} seconds.')

    return


if __name__ == '__main__':
    if len(argv[1:]) == 0:
        command_line = input(f'enter command line for {app_name}: ')
        argv.extend(command_line.split())
    main(argv[1:])