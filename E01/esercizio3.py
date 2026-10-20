import numpy as np
gs=["lunedì","martedì","mercoledì","giovedì","venerdì","sabato","domenica"]
gm=[]
for i in range(1,32):
    gm.append(i)
gmd={gm[i]:gs[(i+3)%7]for i in range (len(gm))}
print(gmd)


    
