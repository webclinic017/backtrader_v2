#used for plotting and checking that stradegy looks right
import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime

class Plot_Stradegy:
    def __init__(self):
        self.close_list = []
        self.stradegy_list = []
    
    def append_close(self, close):
        self.close_list.append(close)
    
    def append_stradegy(self, stradegy_value):
        self.stradegy_list.append(stradegy_value)

    def plot(self):
        x_list = [i for i in range(len(self.close_list))]
        plt.figure()
        plt.plot(x_list, self.close_list, 'b')
        plt.plot(x_list, self.stradegy_list, 'r')
        plt.tight_layout()
        # plt.savefig("stradegies\plotting\plots\strat_plot.png")
        plt.show()