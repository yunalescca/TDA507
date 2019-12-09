import sys
import os
import numpy as np
from math import pow, sqrt

# Approach: I loop through all atoms in the second file. For each of these
# atoms, I start looping through the atoms in the first file. Whenever the
# distance between their centers is less than 2 * RADIUS, I save this as
# an overlap, and also increase 'total number of comparisons'. Whenever I
# find one of these overlaps, I break the current loop and move on to the
# next atom in the second file.

# Data structure: I save the atoms from the second file, which overlaps
# with atoms from the first file, in a set. I did this to avoid duplicates,
# but as I break the current loop when there is an overlap, this should 
# not be necessary.

RADIUS = 2  # Å


def main():
    inp1 = input("Input one PDB file: ")
    inp2 = input("Input another PDB file: ")

    with open(inp1, 'r') as f:
        file_1 = f.read().splitlines()

    with open(inp2, 'r') as f:
        file_2 = f.read().splitlines()

    check_overlaps(file_2, file_1)


# Prints the atom number of each atom in the second file that overlaps with at
# least one atom in the first file. Each atom has radius of 2Å.
def check_overlaps(pdb1, pdb2):
    comparisons = 0
    overlaps = set()
    for row1 in pdb1:
        if row1[0:4] == 'ATOM' or row1[0:6] == 'HETATM':
            x1, y1, z1 = get_xyz(row1)

            for row2 in pdb2:
                if row2[0:4] == 'ATOM' or row2[0:6] == 'HETATM':
                    x2, y2, z2 = get_xyz(row2)
                    comparisons += 1

                    if intersect((x1, y1, z1), (x2, y2, z2)):
                        print('Atom number: ', row1[7:11])
                        overlaps.add(row1)
                        break

    print('Total number of clashing atoms: ', len(overlaps))
    print('Total number of comparisons: ', comparisons)


def get_xyz(row):
    x = float(row[30:38].strip())
    y = float(row[38:46].strip())
    z = float(row[46:54].strip())
    return x, y, z


# s1 and s2 two spheres (tuples) with center (x,y,z)
def intersect(s1, s2):
    center_dist = sqrt(
        pow((s1[0] - s2[0]), 2) +
        pow((s1[1] - s2[1]), 2) +
        pow((s1[2] - s2[2]), 2))
    return center_dist <= 2 * RADIUS


main()
