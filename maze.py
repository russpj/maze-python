''' Maze Class'''

import unittest
from enum import Enum
import random


class _Grid_Graph():
    ''' a lightweight graph helper class'''
    def __init__(self, rows, columns):
        self.grid = []
        for row_index in range(rows):
            column = []
            for col_index in range(columns):
                neighbors = []
                column.append(neighbors)
            self.grid.append(column)
        return

    def neighbors(self, row, col):
        return self.grid[row][col]

    def set_neighbors(self, coords1, coords2):
        grid = self.grid
        neighbors1 = grid[coords1[0]][coords1[1]]
        neighbors1.append(coords2)
        neighbors2 = grid[coords2[0]][coords2[1]]
        neighbors2.append(coords1)


class Cell_Type(Enum):
    WALL = 1
    UNTOUCHED = 2
    TENTATIVE = 3
    SOLUTION = 4


class Cell:
    def __init__(self, cell_type):
        self.cell_type = cell_type
        return


class Maze_Map:
    def __init__(self, graph_rows, graph_columns):
        map = []
        self.map = map
        for map_row in range(2*graph_rows+1):
            row = []
            for map_col in range(2*graph_columns+1):
                row.append(Cell(Cell_Type.WALL))
            map.append(row)
        self.map = map
        return

    def map_coords(self, graph_coords):
        graph_row = graph_coords[0]
        graph_col = graph_coords[1]
        return (graph_row*2+1, graph_col*2+1)

    def cell_type(self, coords):
        cell = self.map[coords[0]][coords[1]]
        return cell.cell_type

    def set_cell_type(self, coords, cell_type):
        self.map[coords[0]][coords[1]] = Cell(cell_type)


class Maze:
    def __init__(self, rows, columns):
        self.columns = columns
        self.rows = rows
        self.graph = _Grid_Graph(rows, columns)
        return

    def maze_map(self):
        map = Maze_Map(self.rows, self.columns)
        for row in range(self.rows):
            for col in range(self.columns):
                map_coords = map.map_coords((row, col))
                map.set_cell_type(map_coords, Cell_Type.UNTOUCHED)
        return map

    def create_maze_dfs(self):
        random.seed()
        grid = self.graph.grid
        rows = len(grid)
        if rows == 0:
            return
        cols = len(grid[0])
        if cols == 0:
            return
        self.start_cell = (0, random.randrange(0, self.columns))
        self.end_cell = (self.rows-1, random.randrange(0, self.columns))
        visited_cells = set()
        return
    
    
class Test_Cell(unittest.TestCase):
    def test_init(self):
        cell = Cell(Cell_Type.WALL)
        self.assertEqual(cell.cell_type, Cell_Type.WALL)
        return


class Test_Graph(unittest.TestCase):
    def test_init(self):
        graph = _Grid_Graph(20, 10)
        grid = graph.grid
        self.assertEqual(len(grid), 20)
        self.assertEqual(len(grid[0]), 10)
        self.assertEqual(grid[10][5], [])

    def test_neighbors(self):
        graph = _Grid_Graph(20, 10)
        graph.set_neighbors((5, 6), (5, 7))
        self.assertTrue((5,6) in graph.neighbors(5, 7))
        self.assertTrue((5,7) in graph.neighbors(5, 6))


class Test_Maze_Map(unittest.TestCase):
    def test_init(self):
        map = Maze_Map(20, 10)
        self.assertEqual(len(map.map), 41)
        self.assertEqual(len(map.map[0]), 21)
        self.assertEqual(map.map_coords((10, 5)), (21, 11))


class Test_Maze(unittest.TestCase):
    def test_init(self):
        maze = Maze(20, 10)
        self.assertEqual(maze.columns, 10)
        self.assertEqual(maze.rows, 20)
        self.assertEqual(maze.graph.neighbors(10, 5), [])
        map = maze.maze_map()
        self.assertEqual(map.cell_type((0,0)), Cell_Type.WALL)
        map_coords_cell = map.map_coords((10, 5))
        cell_type = map.cell_type(map_coords_cell)
        self.assertEqual(cell_type, Cell_Type.UNTOUCHED)

    def test_dfs(self):
        maze = Maze(20, 10)
        maze.create_maze_dfs()
        self.assertEqual(maze.start_cell[0], 0)
        self.assertEqual(maze.end_cell[0], maze.rows-1)
        

if __name__ == '__main__':
    unittest.main()
