#! /usr/bin/python3

from scipy import interpolate as ip
import pandas as pd
import numpy as np
import os
# from matplotlib import pyplot as pt
domain='C:\\Users\\mr.tang\\Desktop\\datatreat'
l=os.listdir(domain)
blv = 0
for i in range(0,len(l)):
    if l[i][0:-4].isdigit()==False:
        blv+=-1


if blv<0:
    l.sort()
else:
    l.sort(key=lambda sk:int(sk[0:-4:1]))


column=[' ']
pre_data = np.zeros([3400, len(l)+1])

for x in range(0, 3400, 1):
    pre_data[x,0]=600+x


for i in range(0,len(l),1):
    origin_file = pd.read_csv(domain+'\\'+l[i], header=None)
    column.append(l[i])
    x = origin_file[0]
    y = origin_file[1]
    f = ip.interp1d(x.values, y.values)
    x_new = np.arange(600, 4000, 1)
    y_new = f(x_new)
    for j in range(0, 3400,1):
        pre_data[j, i+1] = y_new[j]

    # pt.plot(x_new, y_new,color='blue')
    # pt.plot(x,y,color='red')
    # pt.show()

final_data = pd.DataFrame(pre_data, columns=column)

afd = final_data.sort_values(by=[" "], ascending=False)
afd.to_csv('C:\\Users\\mr.tang\\Desktop\\final_data.csv',index=None)
print("process finished")
