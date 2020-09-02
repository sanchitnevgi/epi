from typing import List
from collections import deque
from test_framework import generic_test


def flip_color(i: int, j: int, image: List[List[bool]]) -> None:
    ROWS, COLS = len(image), len(image[0])
    color = image[i][j]
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def flip_helper(x, y):
        image[x][y] = not color

        # Add neighbours of i,j which are color
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check invalid cells
            if not (0 <= nx < ROWS and 0 <= ny < COLS and image[nx][ny] == color):
                continue

            flip_helper(nx, ny)

    flip_helper(i, j)

    

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
