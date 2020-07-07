from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    color = image[x][y]
    ROWS, COLS = len(image), len(image[0])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def flip_helper(i, j):
        if not (0 <= i < ROWS and 0 <= j < COLS and image[i][j] == color):  
            return

        image[i][j] = not color

        for dx, dy in directions:
            n_i, n_j = i + dx, j + dy
            flip_helper(n_i, n_j)

    flip_helper(x, y)

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
