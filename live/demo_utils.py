from tacoma.drawing import edge_activity_plot
import matplotlib.pyplot as pl

def disp(tn):
    edge_activity_plot(tn,time_unit=tn.time_unit)
    pl.show()
