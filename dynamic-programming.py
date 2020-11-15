import sys
from math import inf


sys.setrecursionlimit(10000)

def align_words(string1, string2):  # O(m*n) n chars in string1, m chars in string2
    calc_opt_alignment(len(string1)-1, len(string2)-1, string1, string2)
    alignment1, alignment2 = best_alignment(string1, string2)
    print(alignment1 + " " + alignment2)

def calc_opt_alignment(pos1, pos2, string1, string2):
    if (pos1, pos2) in cache:
        return cache[pos1, pos2]
    else:
        # Base cases for recursion, when no more chars in string
        if pos1 == -1 and pos2 == -1:
            position, max_gain = 0, 0 
        elif pos1 > -1 and pos2 == -1:  
            position, max_gain = 2, -4 * (pos1+1) 
        elif pos1 == -1 and pos2 > -1: 
            position, max_gain = 1, -4 * (pos2+1)
        else:
            # Calculate max gain if: no '*' added, '*' added after char1, '*' added after char2
            char1, char2 = string1[pos1], string2[pos2]
            gain1, position0 = calc_opt_alignment(pos1-1, pos2-1, string1, string2)
            gain1 += int(cost_matrix[index_letter[char1]][index_letter[char2]]) 

            gain2, position1 = calc_opt_alignment(pos1, pos2-1, string1, string2)
            gain2 -= 4

            gain3, position2 = calc_opt_alignment(pos1-1, pos2, string1, string2)
            gain3 -= 4

            max_gain = max(gain1, gain2, gain3)
            position = 0 if max_gain == gain1 else (1 if max_gain == gain2 else 2)

        cache[(pos1, pos2)] = max_gain, position
        return max_gain, position

def best_alignment(string1, string2):  # O(n)
    best_align1, best_align2 = "",""
    pos1, pos2 = len(string1)-1, len(string2)-1

    while pos1 >= 0 or pos2 >= 0:
        ignore, case = cache[pos1, pos2]

        char1 = string1[pos1] if pos1 >= 0 else '*'
        char2 = string2[pos2] if pos2 >= 0 else '*'

        if case == 0:
            best_align1, best_align2 = char1 + best_align1, char2 + best_align2
            pos1 -= 1
            pos2 -= 1
        elif case == 1:
            best_align1, best_align2 = '*' + best_align1, char2 + best_align2
            pos2 -= 1
        else:
            best_align1, best_align2 = char1 + best_align1, '*' + best_align2
            pos1 -= 1

    return best_align1, best_align2

chars = sys.stdin.readline().strip().split(' ')  
nrb_chars = len(chars)            
index_letter = dict(map(lambda t: (t[1], t[0]), enumerate(chars)))
input = sys.stdin.readlines()
cost_matrix = [list.strip().split(' ') for list in input[0:nrb_chars]]
queries = [line.strip().split(' ') for line in input[nrb_chars+1:]]
cache = {}

for query in queries:    
    align_words(query[0], query[1])
    cache.clear()
    

