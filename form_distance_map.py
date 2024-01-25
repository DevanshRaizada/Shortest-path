import networkx as nx
import numpy as np
from tqdm.auto import tqdm
import pickle
import time

np.random.seed(999)
edgelist_path = '../data/'+graph_name+'.edgelist'
graph = nx.read_edgelist(edgelist_path, nodetype=int)

nodes = list(graph.nodes)  # [int(i) for i in list(graph.nodes)]
landmarks = np.random.randint(1, len(nodes), 150)

distance_map = {}
distances = np.zeros((len(nodes), ))

for landmark in tqdm(landmarks):
    distances[:] = np.inf
    node_dists = nx.shortest_path_length(graph, landmark)
    for key, value in node_dists.items():
        distances[key-1] = value  # since node labels start from 1.
    distance_map[landmark] = distances.copy()  # copy because array is re-init on loop start

save_path = '../outputs/distance_map_'+graph_name+'_'+str(time.time())+'.pickle'
pickle.dump(distance_map, open(save_path, 'wb'))
print('distance_map saved at', save_path)