import sys
import heapq as h
import collections

input_lines = sys.stdin.read().strip().split('\n')
N, M = map(int, input_lines[0].split(' '))
graph = {}

for m in range(M):                                              # Loop with time complexity O(m)
    input_line = list(map(int, input_lines[1+m].split(' ')))
    u, v, w = input_line
    graph.setdefault(u,[]).append([v, w])
    graph.setdefault(v,[]).append([u, w])

def prim(graph):
    total_cost = 0
    visited = set()                                             # Python set implemented with Hash Table -> O(1)  
    root = next(iter(graph)) 
    unexplored = [(0, root)]
    while unexplored:                                           # Worst case iteration O(n)
        edge_cost, closest_node = h.heappop(unexplored)         # O(log n) for heappop 
        if closest_node not in visited:
            visited.add(closest_node)                           # We only add nodes once -> O(n)
            total_cost += edge_cost
            for neighbour, edge_cost in graph[closest_node]:
                if neighbour not in visited:                    # Set lookup O(1)
                    h.heappush(unexplored, (edge_cost, neighbour)) # O(log n) heappush
    print(total_cost)

prim(graph)