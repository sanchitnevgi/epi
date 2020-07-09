import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

WHITE, GRAY, BLACK = range(3)

class GraphVertex:
    def __init__(self) -> None:
        self.edges: List['GraphVertex'] = []
        self.color = WHITE


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    def has_cycle(node):
        # Visiting node has already been visited
        if node.color == GRAY:
            return True

        # Mark as in process
        node.color = GRAY

        if any(has_cycle(nxt) for nxt in node.edges if nxt.color != BLACK):
            return True
        
        node.color = BLACK

        return False

    return any(vertex.color == WHITE and has_cycle(vertex) for vertex in graph)


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
