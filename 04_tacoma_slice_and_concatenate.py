# 04
# slice and concatenate

import tacoma as tc
from demo_utils import disp

dtu = tc.load_json_taco('~/.tacoma/dtu_1_weeks.taco')

dtu = tc.rescale_time(dtu, new_t0=0,new_tmax=dtu.tmax/(24*3600))
dtu.time_unit = 'd'

disp(dtu)

sliced = tc.slice(dtu, 3, 4)

disp(sliced)

sliced2 = tc.slice(dtu, 5, 6)

cat = tc.concatenate([sliced, sliced2])

disp(cat)
