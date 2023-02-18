#Find skin cancer drug ids

drugs = []
drug = ''
approved = False

with open('id.txt') as f:
    for line in f.readlines():
        
        if 'TTDDRUID'in line:
            drug = line[9:-1]
            
        if 'ICD-11:' in line:
            if '2C43' or '2C44' in line:
                approved = True
            else:
                approved = False
                
        if approved and 'INDICATI' in line:
            if 'Approved' in line:
                approved = True
            else:
                approved = False
        
        if approved:
            drugs.append(drug)
                
#print(drugs)
#LATER: Only append drugs if they're approved

#Find Smile strings

from rdkit import Chem
smiles = []
correct = False

#file = open('/Users/sunitha/Downloads/synopsis/smiles.smi', 'w')


with open('list.txt') as f:
    for line in f.readlines():
        
        if 'DRUG__ID' in line:
            if drugs.count(line[16:-1]) > 0:
                correct = True
            else:
                correct = False
            
        if correct and 'DRUGSMIL' in line:
            check = Chem.MolFromSmiles(line[16:-1],sanitize=False)
            
            if check != None:
                smiles.append(line[16:-1])
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
for smile in smiles[1:]:
    try:
        #print(from_smiles(smile))
        print("Done")
        row = pd.DataFrame(from_smiles(smile), index = [0])
        #print(row)
        df = pd.concat([df, row])
        
    except RuntimeError:
        continue

#print(df)
df.to_csv('descriptors2.csv', index=False, header=True)

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
