import sys
from datetime import datetime

female_prefs_inverted = {}
male_prefs = {}

def invert_list(l):
    inverted_list = [0]*(N)
    i = 1
    for x in l:
        inverted_list[x-1] = i
        i = i+1
    return inverted_list

def process_person(list):
    if (not (list[0] in female_prefs_inverted)):
        female_prefs_inverted[int(list[0])] = invert_list(list[1:])
    else: 
        male_prefs[int(list[0])] = list[1:]

input_file = sys.stdin.read().strip().split('\n')
N = int(input_file[0])
all_input_numbers = [int(x) for line in input_file[1:] for x in line.split()]

while all_input_numbers:
    process_person(all_input_numbers[0:N+1])
    all_input_numbers = all_input_numbers[N+1:]

all_men = [man for man in male_prefs]
# List with pairs, where index in list is index of women and elements is index of man. Element on position i is the pair of (pairs[w-1],i) 
pairs = [0]*(N)

while all_men:
    m = all_men[0]
    w = male_prefs[m]
    w = w[0]
    m2 = pairs[w-1] # Gets the man woman currently is engaged with. 0 if not engaged. 

    if (m2 == 0):
        pairs[w-1] = m
        all_men = all_men[1:]
    elif (not m2 == 0):
        w_prefs = female_prefs_inverted[w]
        if w_prefs[m-1] < w_prefs[m2-1]:
            pairs[w-1] = m
            all_men.append(m2)
            all_men = all_men[1:]
        else: 
            all_men = all_men[1:]
            all_men.append(m)
    male_prefs[m] = male_prefs[m][1:] # Removes woman from m's pref list

for i in pairs:
    print(i)

