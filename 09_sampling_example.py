# 09 
# Sampling

import tacoma as tc
from demo_utils import pl, disp

from tacoma.analysis import plot_group_size_histogram

from tacoma.interactive import visualize



fw = tc.load_json_taco('./fw_exmpl.json')

groups = tc.measure_group_sizes_and_durations(fw)


fig, ax = pl.subplots(1,1)
plot_group_size_histogram(groups,ax)

pl.show()



fw_sampled = tc.sample(fw,dt=0.4)


groups = tc.measure_group_sizes_and_durations(fw_sampled)


fig, ax = pl.subplots(1,1)
plot_group_size_histogram(groups,ax)

pl.show()


visualize([fw,fw_sampled],frame_dt=0.05)
