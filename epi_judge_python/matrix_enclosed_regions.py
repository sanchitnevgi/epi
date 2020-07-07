from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    if not board or not board[0]:
        return

    ROWS, COLS = len(board), len(board[0])

    def dfs(x, y):
        if not (0 <= x < ROWS and 0 <= y < COLS and board[x][y] == "W"):
            return
        
        board[x][y] = "G"

        for n_x, n_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            dfs(n_x, n_y)
        
    
    # Go over the boundary and fill W
    for row in range(ROWS):
        dfs(row, 0)
        dfs(row, COLS - 1)

    for col in range(COLS):
        dfs(0, col)
        dfs(ROWS - 1, col)


    # Go over grid and set W to B and G to W
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "W":
                board[row][col] = "B"
            elif board[row][col] == "G":
                board[row][col] = "W"

    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
