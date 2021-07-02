import epipack as epk

import epipack.plottools as epl
import numpy as np
import matplotlib.pyplot as pl

comp = list("SEIAR")

latent_period = 2 #d
R0 = 3
infectious_period = 6 #d

inf_rate = R0 / infectious_period
p = 0.2

I0 = 1e-4

def temp_infection_rate(t, y):
    return inf_rate * (np.sin(2*np.pi*t/5)**2 + 0.5)

model = (   epk.EpiModel(comp)
               .set_processes([
                        ("S", "I", temp_infection_rate, "E", "I"),
                        ("S", "A", temp_infection_rate, "E", "I"),
                        ("E", (1-p)/latent_period, "I"),
                        ("E", p/latent_period, "A"),
                        ("I", 1/infectious_period, "R"),
                   ])
               .set_initial_conditions({
                    'S': 1 - I0,
                    'I': I0,
                   })
               )

t = np.linspace(0,100,1000)
res = model.integrate(t)

epl.plot(t, res)
pl.legend()

pl.show()
