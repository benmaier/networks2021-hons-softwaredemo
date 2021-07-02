# 11
# define and simulate SIR model

import tacoma as tc
import numpy as np

from demo_utils import disp
import matplotlib.pyplot as pl

dtu = tc.load_json_taco('~/.tacoma/dtu_4_weeks.taco')

dtu = tc.rescale_time(dtu,0,dtu.tmax/(24*3600))



t, mean_k = tc.mean_degree(dtu)

k0 = tc.time_average(t, mean_k, tmax=dtu.tmax)

infectious_period = 3 #days
beta = 1/infectious_period
R0 = 2
alpha = R0 / k0/infectious_period
sir = tc.SIR(dtu.N,
             t_simulation=10*7,
             infection_rate=alpha,
             recovery_rate=beta,
             number_of_initially_infected=10,
             )

tc.gillespie_epidemics(dtu, sir)

pl.figure()
pl.plot(sir.time, sir.I,label='I')
pl.plot(sir.time, sir.R,label='R')
pl.plot(sir.time, dtu.N-np.array(sir.R),label='S')

pl.legend()
pl.show()
