# 03
# load and rescale time

import tacoma as tc
from demo_utils import disp


hs13 = tc.load_json_taco('~/.tacoma/hs13.taco')

disp(hs13)

hs13 = tc.rescale_time(hs13, new_t0=0, new_tmax=hs13.tmax/(24*3600))
hs13.time_unit = 'd'


disp(hs13)
