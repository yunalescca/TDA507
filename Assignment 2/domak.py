# Josefin Ulfenborg
from pdb_io import read_pdb
from math import pow, sqrt
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

class Domak():

    def __init__(self):
        f = os.path.abspath('2CSN.pdb')
        (self.serial,
        self.name,
        self.alt_loc,
        self.res_name,
        self.chain_id,
        self.res_seq,
        self.x,
        self.y,
        self.z) = read_pdb(f)


    # start: first index to include
    # end: first index to exclude
    def calculate_internal_contacts(self, start, end):
        internal_contacts = 0
        dist_threshold = 5

        for i in range(start, end - 1):
            for j in range(i + 1, end):
                x_diff = float (self.x[i]) - float (self.x[j])
                y_diff = float (self.y[i]) - float (self.y[j])
                z_diff = float (self.z[i]) - float (self.z[j])
                dist_i_j = sqrt(pow(x_diff,2) + pow(y_diff,2) + pow(z_diff,2))
                if dist_i_j < dist_threshold:
                    internal_contacts += 1
        return internal_contacts


    def calculate_external_contacts(self, split):
        external_contacts = 0
        dist_threshold = 5

        for i in range(0, split):
            for j in range(split, len(self.serial)):
                x_diff = float (self.x[i]) - float (self.x[j])
                y_diff = float (self.y[i]) - float (self.y[j])
                z_diff = float (self.z[i]) - float (self.z[j])
                dist_i_j = sqrt(pow(x_diff,2) + pow(y_diff,2) + pow(z_diff,2))
                if dist_i_j < dist_threshold:
                    external_contacts += 1
        return external_contacts


    def calculate_domak_score(self):
        max_score = 0
        final_i = 0
        scores = []
        for i in range(1, len(self.serial)):
            int_A = self.calculate_internal_contacts(0, i)
            int_B = self.calculate_internal_contacts(i, len(self.serial))
            ext_AB = self.calculate_external_contacts(i)
            domak_score = (int_A / ext_AB) * (int_B / ext_AB)
            scores.append(domak_score)
            if domak_score > max_score:
                max_score = domak_score
                final_i = i
        
        print('Maximum DOMAK score: ', max_score, '\t at residue: ', final_i - 1)
        self.plot_domak_scores(scores)
    

    def plot_domak_scores(self, scores):
        plt.plot(list(range(len(scores))), scores)
        plt.show()

domak = Domak()
domak.calculate_domak_score()