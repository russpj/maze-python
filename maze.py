''' Maze Class'''

import unittest


class _Grid_Graph():
    ''' a lightweight graph helper clas'''
    def __init__(self, columns, rows):
        self.grid = []
        for row_index in range(rows):
            column = []
            for col_index in range(columns):
                neighbors = []
                column.append(neighbors)
            self.grid.append(column)
        return


class Maze:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        return


class Test_Graph(unittest.TestCase):
    def test_init(self):
        graph = _Grid_Graph(10, 20)
        grid = graph.grid
        self.assertEqual(len(grid), 20)
        self.assertEqual(len(grid[0]), 10)


class Test_Maze(unittest.TestCase):
    def test_init(self):
        maze = Maze(10, 20)
        self.assertEqual(maze.columns, 10)
        self.assertEqual(maze.rows, 20)


if __name__ == '__main__':
    unittest.main()
