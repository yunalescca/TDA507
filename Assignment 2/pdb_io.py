# Josefin Ulfenborg
import pandas as pd

def read_pdb(pdb_file):
    if not pdb_file.endswith('.pdb'):
        raise Exception('File ',pdb_file,' input should be of .pdb.\n')
    f = pd.read_csv(pdb_file, sep='\t', header=None)
    serial = [] # Index
    name = [] # Atom name
    alt_loc = [] # If atom can appear at multiple locations, this is an index
    res_name = [] # Residual name/type (amino acid)
    chain_id = [] # In this case, just A
    res_seq = [] # Residual sequence, an index
    x = []
    y = []
    z = []
    for index,row in f.iterrows():
        r = row.iloc[0]
        if r[0:4] == 'ATOM' and r[13:16] == 'CA ':
            serial.append(r[7:11].strip()) 
            name.append(r[13:15].strip())
            alt_loc.append(r[15].strip())
            res_name.append(r[17:20])
            chain_id.append(r[21]) 
            res_seq.append(r[23:27].strip())
            x.append(r[30:38].strip())
            y.append(r[38:46].strip())
            z.append(r[46:54].strip())
    
    return serial, name, alt_loc, res_name, chain_id, res_seq, x, y, z