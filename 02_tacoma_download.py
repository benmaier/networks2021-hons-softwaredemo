# 02
# Download files


import tacoma as tc
import numpy as np
import matplotlib.pyplot as pl

from demo_utils import disp

# let's download and display a network

hs13 = tc.download_and_convert_sociopatterns_high_school_2013()

disp(hs13)


print(hs13.notes)
