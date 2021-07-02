# 15
# netwulf intro -> visualize aggregated network

import tacoma as tc
from demo_utils import disp
import networkx as nx

dtu = tc.load_json_taco('~/.tacoma/dtu_1_weeks.taco')


dtu_agg = tc.aggregated_network(dtu)


links = []

for key, val in dtu_agg.items():
    print(key, val)
    links.append((key[0],key[1],{'weight':val}))

G = nx.empty_graph(dtu.N)
G.add_edges_from(links)

import netwulf as nw

network, config = nw.visualize(G)

nw.save("dtu_agg.json",network, config)


