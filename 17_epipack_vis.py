# 17
# visualize model on stylized network

import tacoma as tc
from demo_utils import disp
import networkx as nx
import netwulf as nw

dtu = tc.load_json_taco('~/.tacoma/dtu_1_weeks.taco')


dtu_agg = tc.aggregated_network(dtu)


links = []

for key, val in dtu_agg.items():
    links.append((key[0],key[1],val))


network, config, _ = nw.load("dtu_agg.json")

import epipack as epk
import epipack.plottools as epl
import numpy as np
import matplotlib.pyplot as pl

comp = list("SEIARX")

latent_period = 2 #d
R0 = 3
infectious_period = 6 #d
q_rate = 1/12
p = 0.8

I0 = 1e-4

model = epk.StochasticEpiModel(comp,N=dtu.N,edge_weight_tuples=links)

k = model.out_degree

k0 = np.mean(k)

inf_rate = R0 / infectious_period / k0


model.set_link_transmission_processes([
        ("I", "S", inf_rate, "I", "E"),
        ("A", "S", inf_rate, "A", "E"),
    ])

model.set_node_transition_processes([
                ("E", (1-p)/latent_period ,"A"),
                ("E", p/latent_period ,"I"),
                ("I", 1/infectious_period ,"R"),
                ("A", 1/infectious_period ,"R"),
                ("I", q_rate ,"X"),
    ])


model.set_random_initial_conditions({
        'S': dtu.N - 10,
        'I': 10,
    })



from epipack.vis import visualize

visualize(model,
          network,
          sampling_dt = 0.1,
          ignore_plot_compartments=['S'],
          quarantine_compartments=['X'],
          )

