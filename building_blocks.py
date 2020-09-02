import collections
import itertools

def bin_search(A, k):
    """Basic Binary search"""
    lo, hi = 0, len(A) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if A[mid] == k:
            return mid
        elif A[mid] < k: # Search right
            lo = mid + 1
        else: # A[mid] > k, Search left
            hi = mid - 1
    
    # Search finished, not found
    return -1

def build_graph(edges):
    """Building a graph (adj list) from edges"""
    graph = collections.defaultdict(set)
    for u, v in edges:
        graph[u].add(v)

# TODO: bisect_left

# TODO: bisect_right

# TODO: BFS
visited = set()
def bfs(graph, s):
    q = collections.deque((s, 0))
    while q:
        node, dist = q.popleft()
        for nb in node.edges:
            if nb not in visited:
                visited.add(nb)
                q.append((node, dist + 1))

# TODO: DFS
visited = set()
def dfs(node):
    # Check if node is valid (within grid bounds and not visited)
    if not node or node in visited:
        return
    
    # Visit this node
    visited.add(node)

    # Visit all neighbours
    for nb in node.edges:
        dfs(nb)


# TODO: DFS, Cycle Finding

# TODO: Minimum spanning tree

# TODO: Djikstra shortest path

def floyd_warshall():
    '''All-pairs shortest path'''
    
    # Init graph with inf
    # Set self dist to 0 and add edge distances
    graph = [[]]

    for k, i, j in itertools.product(range(len(graph)), repeat=3):
        # The shortest distance b/w i and j is either the shortest dist found, or distance from i to k and k to j
        # If k lies on the shortest path
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][i])