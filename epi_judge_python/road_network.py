import collections
import functools
import itertools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

HighwaySection = collections.namedtuple('HighwaySection',
                                        ('x', 'y', 'distance'))


def find_best_proposals(H: List[HighwaySection], P: List[HighwaySection],
                        n: int) -> HighwaySection:
    # Build min dist graph
    graph = [[float("inf")] * i + [0] + [float("inf")] * (n - i - 1) for i in range(n)]

    # Add known distances to graph
    for h in H:
        # Undirected graph
        graph[h.x][h.y] = graph[h.y][h.x] = h.distance

    def floyd_warshall(graph):
        for k, i, j in itertools.product(range(n), repeat=3):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    floyd_warshall(graph)

    best_distance_saving = float("-inf")
    best_distance_proposal = HighwaySection(-1, -1, 0)

    for p in P:
        proposal_saving = 0

        for a, b in itertools.product(range(n), repeat=2):
            saving = graph[a][b] - min(
                    graph[a][p.x] + p.distance + graph[p.y][b], 
                    graph[a][p.y] + p.distance + graph[p.x][b]
                )
            proposal_saving += max(saving, 0)

        if proposal_saving > best_distance_saving:
            best_distance_saving = proposal_saving
            best_distance_proposal = p
    
    return best_distance_proposal


@enable_executor_hook
def find_best_proposals_wrapper(executor, H, P, n):
    H = [HighwaySection(*x) for x in H]
    P = [HighwaySection(*x) for x in P]

    return executor.run(functools.partial(find_best_proposals, H, P, n))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('road_network.py',
                                       'road_network.tsv',
                                       find_best_proposals_wrapper,
                                       res_printer=res_printer))
