import numpy as np
import os
import argparse
from model import *
from Hierarchical import *
from prepare import *
from K_means import *
from Spectral import *


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_dir, "dane", "data_18D.txt")
dane_2D_1_path =os.path.join(project_dir, "dane", "dane_2D_8.txt")
rpdate_path = os.path.join(project_dir, "dane", "rp.data")
data=np.loadtxt(dane_2D_1_path)
rpdate=np.loadtxt(rpdate_path)



parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default="Hierarchical",help='model')
parser.add_argument('--clusters', type=int, default=2,help='C')
parser.add_argument('--link', type=str, default=None,help='C')
parser.add_argument('--graph_type', type=str, default='full',help='C')
parser.add_argument('--eps', type=int, default=0.001,help='C')
parser.add_argument('--weight', type=str, default='inverse',help='C')
parser.add_argument('--iter', type=int, default=10,help='C')
args=parser.parse_args()
model_name=args.model
clus=args.clusters
link=args.link
if model_name=="Hierarchical":
    M=Hierarchical(no_clusters=clus,linkage=link)
elif model_name=="Spectral":
    M=Spectral(no_clusters=clus,graph_type=args.graph_type,eps=args.eps,weight_function=args.weight)
elif model_name=="K-means":
    M=K_means(no_clusters=clus,no_iter=args.iter,eps=args.eps)
X,Y=preparerp(rpdate)
#M=Spectral(no_clusters=np.unique(Y).size,graph_type="epsi",eps=5,weight_function="inverse")

res=M.cluster(X)
print(ClusterModel.clusters_to_classes(res,Y))
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