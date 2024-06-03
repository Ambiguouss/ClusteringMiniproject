import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import colorsys

class ClusterModel:
    def cluster(self,X):
        pass

    def clusters_to_classes(clusters,classes):
        #we assume number of clusters==no classes
        n=np.unique(clusters).size
        G = nx.Graph()
        for i in range(n):
            G.add_node(i, bipartite=0)
            G.add_node(i+n, bipartite=1)
        for i in range(n):
            for j in range(n):
                weight = np.sum((clusters==i) & (classes==j))
                G.add_edge(i, j+n, weight=weight)
        matching = nx.max_weight_matching(G, maxcardinality=True)
        res=0
        for a,b in matching:
            weight = G.get_edge_data(a, b).get('weight',None)
            res+=weight
        return res/clusters.size

    def plot(self,X,Y,save=None):
        k=np.unique(Y).size
        hues = [(i/k, 1.0, 1.0) for i in range(k)]
        colors = [colorsys.hsv_to_rgb(*h) for h in hues]
        C=[]
        for i in range(k):
            C.append(X[Y==i])
        for i in range(k):
            plt.scatter(C[i][:, 0], C[i][:, 1], color=colors[i])
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.title(self.signature)
        
        # Show the plot
        if save is None:
            plt.show()
        else:
            plt.savefig(save)
