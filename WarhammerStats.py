import numpy as np
import matplotlib.pyplot as plt

stat_file  = open('WarhammerUnitStats.csv', 'r')
armor,charge,meleeA,meleeD,morale = [],[],[],[],[]
for i,line in enumerate(stat_file):
    if i > 0: 
        a,b,c,d,e = line.split("\t")
        armor.append(int(a))
        charge.append(int(b))
        meleeA.append(int(c))
        meleeD.append(int(d))
        morale.append(int(e))

