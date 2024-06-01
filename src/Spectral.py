import numpy as np
import networkx as nx
from model import *




class Spectral(CluseterModel):
    
    def __init__(self,no_clusters=2,dist="euclid",graph_type='epsi',weight_function='inverse',eps=None,neighbour=None):
        self.dist=getattr(Spectral,dist,None)
        self.no_clusters=no_clusters
        self.weight_function=self.weight_factory(weight_function,self.dist)
        self.graph_function=self.graph_creator_factory(graph_type,self.dist,self.weight_function,eps,neighbour)

    
    def epsi(X,eps,dist):
        n=X.shape[0]
        A=np.zeros((n,n))
        D=np.zeros((n,n))
        for i,x1 in enumerate(X):
            for j,x2 in enumerate(X):
                if i!=j and dist(x1,x2)<eps:
                    A[i][j]=1
                    D[i][i]+=0.5
                    D[j][j]+=0.5
        return A,D
    def neighbours(X,k,dist,weight_fun):
        pass
    def full(X,weight_fun):
        n=X.shape[0]
        A=np.zeros((n,n))
        D=np.zeros((n,n))
        for i,x1 in enumerate(X):
            for j,x2 in enumerate(X):
                if i!=j:
                    w=weight_fun(x1,x2)
                    A[i][j]=w
                    A[j][i]=w
                    D[i][i]+=w/2
                    D[j][j]+=w/2
        return A,D

    def inverse(X,Y,dist):
        d=dist(X,Y)
        if d==0:
            return 0
        return 1/(d)

    def weight_factory(self,weight_function,dist):
        if weight_function=='inverse':
            def fun(X,Y):
                return Spectral.inverse(X,Y,dist)
            return fun
        return None

    def graph_creator_factory(self,graph_type,dist,weight_function=None,eps=None,neighbour=None):
        if graph_type=='epsi':
            def fun(X):
                return Spectral.epsi(X,eps,dist)
            return fun
        if graph_type=='neighbours':
            def fun(X):
                return Spectral.neighbours(X,neighbour,weight_function,dist)
            return fun
        if graph_type=='full':
            def fun(X):
                return Spectral.full(X,weight_function)
            return fun
        return None
        
    def euclid(X,Y):
        return np.linalg.norm(X-Y)
    

    def cluster(self,X):
        n=X.shape[0]
        A,D=self.graph_function(X)
        #print(A,D)
        L=D-A
        eigenval,eigenvec = np.linalg.eig(L)
        eig_pair = [(eigenval[i], eigenvec[:, i]) for i in range(len(eigenval))]
        eig_pair.sort(key=lambda x: x[0])
        sorted_eigenvalues = np.array([pair[0] for pair in eig_pair])
        sorted_eigenvectors = np.array([pair[1] for pair in eig_pair])
        print(sorted_eigenvalues)
        if sorted_eigenvalues[1]<=0:
            raise Exception("Graph not connected")
        v1=sorted_eigenvectors[1]
        clusters=np.where(v1>0,0,1)
        #print(clusters)
        return clusters


