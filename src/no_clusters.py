import numpy as np
import os
import argparse
import time
from model import *
from Hierarchical import *
from prepare import *
from K_means import *
from Spectral import *
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--set', type=int, default=1,help='set')
parser.add_argument('--dir', type=str, default="results/dane_2D/no_clusters/",help='dir')
args=parser.parse_args()
set=args.set
output_directory=args.dir
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dane_path =os.path.join(project_dir, "dane", f'data_18D.txt')
data=np.loadtxt(dane_path)

X,Y=prepare2D(data)
n=10
eval_table=[]
for i in range(1,n):
    print(i)
    M=K_means(no_clusters=i,no_iter=10)
    res,eval=M.cluster(X,ret_eval=True)
    eval_table.append(eval)


plt.plot(range(1, n), eval_table)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('eval')
plt.xticks(range(1, n))
output_path = os.path.join(output_directory, 'elbow.png')

plt.show()


