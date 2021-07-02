# 05
# Visualization

import tacoma as tc
from demo_utils import disp

from tacoma.interactive import visualize

dtu = tc.load_json_taco('~/.tacoma/dtu_1_weeks.taco')

dtu = tc.rescale_time(dtu, new_t0=0,new_tmax=dtu.tmax/(24*3600))
dtu.time_unit = 'd'


visualize(dtu,frame_dt=1/24/60*5,config='dtu')

