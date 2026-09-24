''' Maze Class'''

import unittest
from enum import Enum


class _Grid_Graph():
    ''' a lightweight graph helper class'''
    def __init__(self, columns, rows):
        self.grid = []
        for row_index in range(rows):
            column = []
            for col_index in range(columns):
                neighbors = []
                column.append(neighbors)
            self.grid.append(column)
        return

    def neighbors(self, col, row):
        return self.grid[row][col]


class Cell_Type(Enum):
    WALL = 1
    UNTOUCHED = 1
    TENTATIVE = 2
    SOLUTION = 3


class Cell:
    def __init__(self, cell_type):
        self.cell_type = cell_type
        return


class Maze_Map:
    def __init__(self, graph_columns, graph_rows):
        map = []
        self.map = map
        for map_row in range(2*graph_rows+1):
            row = []
            for map_col in range(2*graph_columns+1):
                row.append(Cell(Cell_Type.WALL))
            map.append(row)
        self.map = map
        return

    def cell_type(self, column, row):
        cell = self.map[row][column]
        return cell.cell_type

    def map_coords(self, graph_coords):
        graph_col = graph_coords[0]
        graph_row = graph_coords[1]
        return (graph_col*2+1, graph_row*2+1)


class Maze:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.graph = _Grid_Graph(columns, rows)
        self.map = Maze_Map(columns, rows)
        return


class Test_Cell(unittest.TestCase):
    def test_init(self):
        cell = Cell(Cell_Type.WALL)
        self.assertEqual(cell.cell_type, Cell_Type.WALL)
        return


class Test_Graph(unittest.TestCase):
    def test_init(self):
        graph = _Grid_Graph(10, 20)
        grid = graph.grid
        self.assertEqual(len(grid), 20)
        self.assertEqual(len(grid[0]), 10)


class Test_Maze_Map(unittest.TestCase):
    def test_init(self):
        map = Maze_Map(10, 20)
        self.assertEqual(len(map.map), 41)
        self.assertEqual(len(map.map[0]), 21)
        self.assertEqual(map.map_coords((5, 10)), (11, 21))


class Test_Maze(unittest.TestCase):
    def test_init(self):
        maze = Maze(10, 20)
        self.assertEqual(maze.columns, 10)
        self.assertEqual(maze.rows, 20)
        self.assertEqual(maze.graph.neighbors(5, 10), [])
        self.assertEqual(maze.map.cell_type(0,0), Cell_Type.WALL)
        map_coord_cel = maze.map.map_coords((5, 10))
        cell_type = maze.map.cell_type(map_coord_cel[0], map_coord_cel[1])
        self.assertEqual(cell_type, Cell_Type.WALL)


if __name__ == '__main__':
    unittest.main()
