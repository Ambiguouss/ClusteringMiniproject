import numpy as np
import networkx as nx


class CluseterModel:
    def cluster(self,X):
        pass
    
    def clusters_to_classes(self,clusters,classes):
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