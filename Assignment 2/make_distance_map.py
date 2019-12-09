# Josefin Ulfenborg
from pdb_io import read_pdb
from math import pow, sqrt
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#FILE_NAME = '1CDH'
FILE_NAME = '2CSN'

class MakeDistanceMap():

    def __init__(self):
        f = os.path.abspath(FILE_NAME + '.pdb')
        (self.serial,
        self.name,
        self.alt_loc,
        self.res_name,
        self.chain_id,
        self.res_seq,
        self.x,
        self.y,
        self.z) = read_pdb(f)

    
    def print_pdb(self):
        print('#atoms: ', len(self.serial))
        for i in range(0, len(self.serial)):
            print('Serial: ', self.serial[i], '\t Name: ', self.name[i], '\t Res name: ', self.res_name[i],
                  '\t x: ', self.x[i], '\t y: ', self.y[i], '\t z: ', self.z[i])


    def find_closest_pairs(self):
        pairs = []
        dist_threshold = 7
        for i in range(0, len(self.serial) - 1):
            for j in range(i, len(self.serial)):
                x_diff = float (self.x[i]) - float (self.x[j])
                y_diff = float (self.y[i]) - float (self.y[j])
                z_diff = float (self.z[i]) - float (self.z[j])
                dist_i_j = sqrt(pow(x_diff,2) + pow(y_diff,2) + pow(z_diff,2))
                if dist_i_j < dist_threshold:
                    pairs.append(self.res_seq[i] + ' ' + self.res_seq[j])
                    pairs.append(self.res_seq[j] + ' ' + self.res_seq[i])
        
        # df = pd.DataFrame(pairs)
        # df.to_csv(FILE_NAME + '.pairs', header=False, index=False)
    

mdm = MakeDistanceMap()
mdm.print_pdb()
mdm.find_closest_pairs()