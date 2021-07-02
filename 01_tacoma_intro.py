# 01
# Edge activity plots 

import tacoma as tc
import numpy as np
import matplotlib.pyplot as pl

# let's construct a temporal network

tn = tc.edge_lists()

tn.N = 8
tn.t = [ 0.0, 1.0, 1.5, 3.0, 4.0, 7.0, 7.31 ]
tn.tmax = 8.1
tn.edges = [
               [ (0, 1), (1, 7) ],
               [ (0, 1) ],
               [ (0, 1), (1, 7) ],
               [ (2, 5), (1, 7) ],
               [ (2, 5) ],
               [ (0, 1), (2, 5) ],
               [ (0, 1) ]
           ]

tn.time_unit = 's'
tn.notes = 'This experiment was conducted as a test.'
tn.int_to_node = {
                   0 : 'Alice',
                   1 : 'Bob',
                   2 : 'Clara',
                   3 : 'Darren',
                   4 : 'Elle',
                   5 : 'Felicitas',
                   6 : 'George',
                   7 : 'Harriett',
                 }

# and illustrate the darn thing

from tacoma.drawing import edge_activity_plot

edge_activity_plot(tn)
pl.show()


# also, let's define a function to make our lives easier

def disp(tn):
    edge_activity_plot(tn)
    pl.show()


from rich import print

# convert this `edge_lists` object an `edge_changes` object


tn_ch = tc.convert(tn)

print(type(tn_ch))

help(tn_ch)

print(tn_ch.edges_initial)
print(tn_ch.edges_in)
print(tn_ch.edges_out)

