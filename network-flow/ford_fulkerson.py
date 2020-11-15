from collections import deque
from copy import deepcopy
from math import inf


def bfs(graph, start, end):  # O(m + n)
    found_path = False
    visited = set()
    visited.add(start)
    q = deque([start])

    while q and not found_path:
        temp_node = q.popleft()
        visited.add(temp_node)
        for temp_edge in temp_node.edges:  
            if temp_edge.destination1 == temp_node:
                next_node = temp_edge.destination2
            else:
                next_node = temp_edge.destination1
            if not (temp_edge.is_full(next_node) or next_node in visited): 
                q.append(next_node)
                next_node.previous_node = temp_node
                next_node.previous_edge = temp_edge
                if next_node == end: 
                    found_path = True
                    break
    return found_path

def ford_fulkerson(graph, start, end): # Is called max C times -> O(C), and each bfs call is O(m) if m>n
    flow = 0
    try: source_node, sink_node = graph[start], graph[end]
    except: return 0
    exists_path = bfs(graph, source_node, sink_node)  

    while exists_path: 
        delta = inf
        temp_node = sink_node

        while temp_node != source_node:
            delta = min(delta, temp_node.previous_edge.get_capacity(temp_node))
            temp_node = temp_node.previous_node
        flow += delta
        temp_node = sink_node

        while temp_node != source_node:  # update flow along the found path O(m)
            temp_node.previous_edge.update_flow(temp_node, delta)
            temp_node = temp_node.previous_node

        exists_path = bfs(graph, source_node, sink_node)
    return flow