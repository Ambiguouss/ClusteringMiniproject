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






parser = argparse.ArgumentParser()
parser.add_argument('--set',type=int,default=1,help="set")
parser.add_argument('--model', type=str, default="Hierarchical",help='model')
parser.add_argument('--clusters', type=int, default=2,help='C')
parser.add_argument('--link', type=str, default=None,help='C')
parser.add_argument('--graph_type', type=str, default='full',help='C')
parser.add_argument('--eps', type=float, default=0.001,help='C')
parser.add_argument('--weight', type=str, default='inverse',help='C')
parser.add_argument('--iter', type=int, default=10,help='C')
parser.add_argument('--dir', type=str, default="results/dane_2D/acc/",help='dir')
args=parser.parse_args()
model_name=args.model
clus=args.clusters
link=args.link
dane_path =os.path.join(project_dir, "dane", f'dane_2D_{args.set}.txt')
data=np.loadtxt(dane_path)
X,Y=prepare2D(data)
c=np.unique(Y).size
if model_name=="Hierarchical":
    M=Hierarchical(no_clusters=c,linkage=link)
elif model_name=="Spectral":
    M=Spectral(no_clusters=c,graph_type=args.graph_type,eps=args.eps,weight_function=args.weight)
elif model_name=="K-means":
    M=K_means(no_clusters=c,no_iter=args.iter,eps=args.eps)


start_time=time.time()
res=M.cluster(X)
end_time=time.time()
print(f'Time: {end_time-start_time}s\nAcc: {ClusterModel.clusters_to_classes(res,Y)}')
M.plot(X,res)
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