# 14
# symbolic model

import epipack as epk
import epipack.plottools as epl
import numpy as np
import matplotlib.pyplot as pl

import sympy as sy

S, E, I, A, R = comp = sy.symbols("S E I A R")

latent_period = sy.symbols("t_L") #d
R0 = sy.symbols("R_0")
infectious_period = sy.symbols("t_I") #d
inf_rate = R0 / infectious_period
p = sy.symbols("p")
t = sy.symbols("t")

temporal_infection_rate = inf_rate * (sy.sin(2*sy.pi*t/5)**2+0.5)
#return inf_rate * (np.sin(2*np.pi*t/5)**2+0.5)


model = ( epk.SymbolicEpiModel(comp)
             .set_processes([
                    (S,I, temporal_infection_rate ,E, I),
                    (S,A, temporal_infection_rate ,E, I),
                    (E, (1-p)/latent_period ,A),
                    (E, p/latent_period ,I),
                    (I, 1/infectious_period ,R),
                    (A, 1/infectious_period ,R),
                 ])
             #.set_initial_conditions({
             #       'S' : 1-I0,
             #       'I' : I0,
             #    })
             )


#t = np.linspace(0,100,1000)
#result = model.integrate(t)

for ode in model.ODEs():
    print(ode)

#epl.plot(t, result)

pl.show()
