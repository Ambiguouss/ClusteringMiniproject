import numpy as np
from model import *


class Hierarchical(ClusterModel):
    
    def single_linkage(A,B):
        return [0.5,0.5,0,-0.5]
    def complete_linkage(A,B):
        return [0.5,0.5,0,0.5]
    def average_linkage(A,B):
        return [A/(A+B),B/(A+B),0,0]
    def centroid_linkage(A,B):
        return [A/(A+B),B/(A+B),-A*B/((A+B)**2),0]
    def Ward_linkage(A,B):
        return [(2*A+B)/(2*A+2*B),(A+2*B)/(2*A+2*B),-(A+B)/(2*A+2*B),0]
    linkage_table={
        "single":single_linkage,
        "complete":complete_linkage,
        "average":average_linkage,
        "centroid":centroid_linkage,
        "Ward":Ward_linkage
    }

    def __init__(self,no_clusters=None,dist="euclid",linkage="single"):
        self.dist=getattr(self,dist,None)
        self.linkage=Hierarchical.linkage_table[linkage]
        self.no_clusters=no_clusters
        self.signature=f'{self.__class__.__name__}({linkage})'
    
    def euclid(self,X,Y):
        return np.linalg.norm(X-Y)
    
    

    def cluster(self,X):
        n=X.shape[0]
        result=np.zeros((n,n))
        clusters=np.arange(n)
        dist_vectorized=np.vectorize(self.dist,signature='(n),(n)->()')
        D=dist_vectorized(X[:,np.newaxis],X)
        D_indices=clusters
        D_sizes=np.ones(n)
        result[0]=clusters
        for i in range(n-1):
            a,b = min_pair(D)
            Da=D_indices[a]
            Db=D_indices[b]
            Sa=D_sizes[a]
            Sb=D_sizes[b]
            if Da>Db:
                a,b=b,a
                Da,Db=Db,Da
            alpha1,alpha2,beta,gamma=self.linkage(Sa,Sb)
            new_row=alpha1*D[:][a]+alpha2*D[:][b]+beta*D[a][b]+gamma*np.abs(D[:][a]-D[:][b])
            Da=D_indices[a]
            Db=D_indices[b]
            clusters[clusters==Db]=Da
            D=np.vstack((D,new_row))
            new_row=np.append(new_row,0)
            D=np.hstack([D,new_row.reshape(-1,1)])
            D=np.delete(D,[a,b],axis=0)
            D=np.delete(D,[a,b],axis=1)
            D_sizes=np.delete(D_sizes,[a,b])
            D_sizes=np.append(D_sizes,Sa+Sb)
            D_indices=np.delete(D_indices,[a,b])
            D_indices=np.append(D_indices,Da)
            result[i+1]=clusters
        if self.no_clusters is None:
            return result
        _, inverse_indices = np.unique(result[n-self.no_clusters], return_inverse=True)
        scaled_array = inverse_indices
        return scaled_array

    

def min_pair(X):
    mask = ~np.eye(X.shape[0], dtype=bool)
    masked_X = np.where(mask, X, np.inf)
    min_index_flat = np.argmin(masked_X)
    return np.unravel_index(min_index_flat, X.shape)

