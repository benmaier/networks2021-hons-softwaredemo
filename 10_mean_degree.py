# 10
# compute temporal average of mean degree

import tacoma as tc
import numpy as np

from demo_utils import disp
import matplotlib.pyplot as pl

dtu = tc.load_json_taco('~/.tacoma/dtu_4_weeks.taco')

dtu = tc.rescale_time(dtu,0,dtu.tmax/(24*3600))


disp(dtu)

t, mean_k = tc.mean_degree(dtu)

pl.plot(t,mean_k)

pl.show()

k0 = tc.time_average(t, mean_k, tmax=dtu.tmax)

print(k0)
