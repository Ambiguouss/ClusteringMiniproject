import numpy as np
import os
import argparse
import time
from model import *
from Hierarchical import *
from prepare import *
from K_means import *
from Spectral import *


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


dane_path =os.path.join(project_dir, "dane", "data_18D.txt")
data=np.loadtxt(dane_path)
X=data

M=[Spectral(graph_type="epsi",eps=100),Spectral(graph_type="full"),K_means(),Hierarchical(no_clusters=2,linkage="single"),
   Hierarchical(no_clusters=2,linkage="Ward")]

res_table=[]
for i,m in enumerate(M):
    res_table.append(m.cluster(X))

for i in range(len(res_table)):
    for j in range(len(res_table)):
        print(ClusterModel.clusters_to_classes(res_table[i],res_table[j]),end=' ')
    print("\n")


#hier = Hierarchical(no_clusters=np.unique(Y).size,linkage="Ward")
#res = hier.cluster(X)
#print(ClusterModel.clusters_to_classes(res,Y))
#hier.plot(X,res)
#print(res)
#print(Y)
#print(hier.clusters_to_classes(res,Y))
#kmean=K_means(no_clusters=np.unique(Y).size,no_iter=10,eps=0.001)
#res=kmean.cluster(X)
#print(ClusterModel.clusters_to_classes(res,Y))
#kmean.plot(X,res)
#spec=Spectral(no_clusters=np.unique(Y).size,graph_type="full",eps=3,weight_function="gauss")
#res=spec.cluster(X)
#print(ClusterModel.clusters_to_classes(res,Y))
#spec.plot(X,res)