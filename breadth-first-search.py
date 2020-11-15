import sys
from collections import deque
import datetime

input_lines = sys.stdin.read().strip().split('\n')
N, Q = (input_lines[0].split(' '))
N ,Q = int(N), int(Q)
graph = {}

def make_node(word):
    graph[word] = []

def edge_exists(word1, word2):
    for char in word1:
        if char in word2:
            word2 = word2.replace(char, '', 1)
        else:
            return False
    return True

def add_neighbours(current_node):
    for node in graph:
        if (edge_exists(current_node[1:], node)) and (not current_node == node):
            neighbours = graph[current_node]
            neighbours.append(node)
            graph[current_node] = neighbours

def BFS(graph, start, end):
    visited = set()
    q = deque([(start, [start])])
    visited.add(start)
    while q:
        (v, path) = q.popleft()
        if (not start == end):
            for w in graph[v]:
                if not w in visited:
                    visited.add(w)
                    q.append((w, path + [w]))   
                if (w == end):
                    print(len(path))
                    return
        else:
            print('0') 
            return
    print("Impossible")

for n in range(N):
    make_node(input_lines[n+1])

for node in graph:
    add_neighbours(node)

for queries in input_lines[N+1:]:
    start_word, end_word = queries.split(' ')
    BFS(graph, start_word, end_word)

