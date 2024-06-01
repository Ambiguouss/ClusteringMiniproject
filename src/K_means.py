import numpy as np
from model import *


class K_means(CluseterModel):
    
    def __init__(self,no_clusters=2,dist="euclid",no_iter=10,eps=0.001):
        self.dist=getattr(self,dist,None)
        self.no_clusters=no_clusters
        self.eps=eps
        self.no_iter=no_iter
    
    def euclid(self,X,Y):
        return np.linalg.norm(X-Y)
    
    def evaluate(self,clusters,cent,X):
        m=X.shape[0]
        res=0
        for i in range(m):
            res+=self.dist(X[i],cent[clusters[i]])**2
        return res

    def cluster(self,X):
        k=self.no_clusters
        best_res=None
        best_eval=np.inf
        for _ in range(self.no_iter):
            ind=np.random.choice(X.shape[0], k, replace=False)
            mi=X[ind]
            clusters,cent=self._cluster(X,mi)
            eval=self.evaluate(clusters,cent,X)
            if eval<best_eval:
                best_res=clusters
                best_eval=eval
        return best_res
            

    def _cluster(self,X,mi):
        k=mi.shape[0]
        while True:
            clusters=[[] for _ in range(k)]
            assignment=np.zeros(X.shape[0],dtype=int)
            for ind,x in enumerate(X):
                distance_to_cent = np.apply_along_axis(self.dist, 1, mi, x)
                j=np.argmin(distance_to_cent)
                clusters[j].append(x)
                assignment[ind]=j
            newmi=np.array([np.apply_along_axis(np.mean,0,clusters[i]) for i in range(k)])
            if self.dist(newmi,mi)<self.eps:
                return assignment,newmi
            mi=newmi
        

        
        
        