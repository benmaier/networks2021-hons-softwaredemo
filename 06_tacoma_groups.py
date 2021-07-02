# 06
# group sizes with histogram

import tacoma as tc
from demo_utils import pl, disp

from tacoma.analysis import plot_group_size_histogram



hs13 = tc.load_json_taco('~/.tacoma/hs13.taco')

groups = tc.measure_group_sizes_and_durations(hs13)


fig, ax = pl.subplots(1,1)
plot_group_size_histogram(groups,ax)

pl.show()



