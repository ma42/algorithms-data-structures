import sys
from graph_element import Edge, Node
from ford_fulkerson import ford_fulkerson

sys.setrecursionlimit(10**9)
N, M, C, P = list(map(int, sys.stdin.readline().strip().split(' '))) 
input = sys.stdin.readlines()
graph = {}

nodes = [ Node(n) for n in range(N) ]
edges = [0] * M
for i in range(M):
    dest1, dest2, cap = map(int, input[i].strip().split(' '))
    edges[i] = Edge(nodes[dest1], nodes[dest2], cap)
P_edges = [ int(line.strip()) for line in input[M:] ]

def update_graph(edge):
    from_node, to_node = edge.destination1, edge.destination2
    if from_node.index not in graph:
        from_node.edges.append(edge)
        graph[from_node.index] = from_node
    else:
        graph[from_node.index].edges.append(edge)
        
    if to_node.index not in graph:
        to_node.edges.append(edge)
        graph[to_node.index] = to_node 
    else:
        graph[to_node.index].edges.append(edge)

# Creating inital graph
for index, edge in enumerate(edges): 
    if index not in P_edges:
        update_graph(edge)

max_flow = 0
# Add an edge from P_edges at a time and get new max_flow until reaching max capacity
while max_flow < C:     
    update_graph(edges[P_edges.pop()])
    max_flow += ford_fulkerson(graph, 0, N-1)  

print(len(P_edges), max_flow)  # len(P_edges) contain how many routes we didn't have to use (aka. removed edges)
