from rdkit import Chem
smiles = []
correct = False

#file = open('/Users/sunitha/Downloads/synopsis/smiles.smi', 'w')

i = 0
with open('COCONUT_DB.smi') as f:
    for line in f.readlines():
        check = Chem.MolFromSmiles(line,sanitize=False)
            
        if check != None and i < 5000:
            smiles.append(line)
            i+=1
            #file.write(line[16:-1])
            #file.write("\n")

#file.close()
#print(smiles)

#Find padel descriptors
print("Size: ", len(smiles)) #3409
print(type(smiles))

from padelpy import from_smiles

descriptors = {}

descriptors.update(from_smiles(smiles[0]))
import pandas as pd
df = pd.DataFrame(descriptors, index = [0])
print(df)

i = 0
for smile in smiles[1:]:
    try:
        #print(from_smiles(smile))
        print("Done ", i)
        row = pd.DataFrame(from_smiles(smile), index = [0])
        #print(row)
        df = pd.concat([df, row])
        i+=1
        
    except RuntimeError:
        continue

#print(df)
df.to_csv('coconut.csv', index=False, header=True)

"""
from padelpy import padeldescriptor

padeldescriptor(mol_dir='/Users/sunitha/Downloads/synopsis/smiles.smi', d_file='descriptors.csv', maxruntime=10000)
"""

"""
import csv

# open the file in the write mode
f = open('/Users/sunitha/Downloads/synopsis/descriptors2.csv', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
i = 0
for smile in smiles:
    try:
        #writer.writerow(from_smiles(smile))
        writer.writerow(x in from_smiles(smile).values)
        print("done")
    except RuntimeError:
        continue
    i+=1

# close the file
f.close()

#print(from_smiles(smiles[0]))

"""
