# 13
# epipack stochastic 

import epipack as epk
import epipack.plottools as epl
import numpy as np
import matplotlib.pyplot as pl

comp = list("SEIAR")

latent_period = 2 #d
R0 = 3
infectious_period = 6 #d
inf_rate = R0 / infectious_period
p = 0.8

I0 = 1e-4

def temporal_infection_rate(t, y):
    return inf_rate * (np.sin(2*np.pi*t/5)**2+0.5)

model = ( epk.EpiModel(comp,initial_population_size=1000)
             .set_processes([
                    ("S","I", temporal_infection_rate ,"E", "I"),
                    ("S","A", temporal_infection_rate ,"E", "I"),
                    ("E", (1-p)/latent_period ,"A"),
                    ("E", p/latent_period ,"I"),
                    ("I", 1/infectious_period ,"R"),
                    ("A", 1/infectious_period ,"R"),
                 ])
             .set_initial_conditions({
                    'S' : 1000-10,
                    'I' : 10,
                 })
             )


t, result = model.simulate(100)

epl.plot(t, result)

pl.show()
