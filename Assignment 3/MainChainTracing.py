# Josefin Ulfenborg

# Run this program with `python3 MainChainTracing.py`
import pandas as pd
from math import sqrt, pow

def main(file_name):
    closest_pairs, endpoint = find_closest_neighbors(file_name)
    print_main_chain(closest_pairs, endpoint)


def find_closest_neighbors(file_name):
    txt = pd.read_csv(file_name, sep='\t', header=None)
    closest_pairs = {}

    # Calculate distances between each pair. If below threshold, add as closest neighbor
    for i,row in txt.iterrows():
        x_1 = float(row.iloc[1].split(' ')[0])
        y_1 = float(row.iloc[1].split(' ')[1])
        z_1 = float(row.iloc[1].split(' ')[2])
        p = []
        for j,row in txt.iterrows():
            if i != j:
                x_2 = float(row[1].split(' ')[0])
                y_2 = float(row[1].split(' ')[1])
                z_2 = float(row[1].split(' ')[2])
                d = sqrt(pow((x_1 - x_2), 2) + pow((y_1 - y_2), 2) + pow((z_1 - z_2), 2))
                if d < 4 and len(p) < 2:
                    p.append(j + 1)
        if len(p) == 1: # if alpha carbon only has one neighbor, it means this was an endpoint
            endpoint = i + 1
        closest_pairs[i + 1] = p

    return closest_pairs, endpoint


def print_main_chain(closest_pairs, endpoint):
    print('Each alpha carbon with its two closest neighbors')
    for k,v in closest_pairs.items():
        print(k, '\t=> ', v)
    print()

    current = endpoint
    chain = []
    chain.append(current)
    print(current)
    
    # Between each iteration, update which is current and which is next_in.
    # Since the closest neighbors of "next_in" will contain "current",
    # remove "current", from this list. The remaining neighbor is next in chain.
    for i in range(0,9):
        next_in = closest_pairs[current][0]
        print(next_in)
        chain.append(next_in)
        del(closest_pairs[current])
        closest_pairs[next_in].remove(current)
        current = next_in
    
    print('\nTotal number of alpha carbons: ', len(chain))

main('data_q1.txt')

