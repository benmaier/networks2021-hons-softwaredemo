# 08
# how binning influences the group size distribution

import tacoma as tc
from demo_utils import pl, disp

from tacoma.analysis import plot_group_size_histogram

from tacoma.interactive import visualize



fw = tc.load_json_taco('./fw_exmpl.json')

groups = tc.measure_group_sizes_and_durations(fw)


fig, ax = pl.subplots(1,1)
plot_group_size_histogram(groups,ax)

pl.show()



fw_binned = tc.bin(fw,dt=0.4)


groups = tc.measure_group_sizes_and_durations(fw_binned)


fig, ax = pl.subplots(1,1)
plot_group_size_histogram(groups,ax)

pl.show()


visualize([fw,fw_binned],frame_dt=0.05)
