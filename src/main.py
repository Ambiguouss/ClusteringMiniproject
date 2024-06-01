import numpy as np
import os
from model import *
from Hierarchical import *
from prepare import *
from K_means import *
from Spectral import *


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_dir, "dane", "data_18D.txt")
dane_2D_1_path =os.path.join(project_dir, "dane", "dane_2D_7.txt")
rpdate_path = os.path.join(project_dir, "dane", "rp.data")
data=np.loadtxt(dane_2D_1_path)
rpdate=np.loadtxt(rpdate_path)


X,Y=prepare2D(data)
#hier = Hierarchical(no_clusters=np.unique(Y).size,linkage="Ward")
#res = hier.cluster(X)
#print(res)
#print(Y)
#print(hier.clusters_to_classes(res,Y))
#kmean=K_means(no_clusters=6,no_iter=10,eps=0.001)
#res=kmean.cluster(X)
#print(kmean.clusters_to_classes(res,Y))
spec=Spectral(graph_type="epsi",eps=5)
res=spec.cluster(X)
CluseterModel.plot(X,res)
print(spec.clusters_to_classes(res,Y))