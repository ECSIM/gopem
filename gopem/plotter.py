# embedding_in_qt5.py --- Simple Qt5 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#               2015 Jens H Nielsen
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
import matplotlib
from PyQt5 import QtWidgets
matplotlib.use('Qt5Agg')  # Make sure that we are using QT5

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from gopem.helper import frange

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def update_plot(self, data, x_axis, y_axis):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        self.axes.cla()
        # Major ticks every 20, minor ticks every 5
        self.axes.grid(True, linestyle='-.', which='both')
        if x_axis in data.keys() and y_axis in data.keys():
            self.axes.plot(data[x_axis], data[y_axis], 'r')

        # self.axes.plot(data["I"], data["P"], 'g')
        # self.axes.plot(data["I"], data["V0"], 'b')
        # self.axes.plot(data["I"], data["K"], 'c')
        # self.axes.plot(data["I"], data["V"], 'm')
        # self.axes.plot(data["I"], data["Ph"], 'k')
        self.draw()

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""



    def compute_initial_figure(self):
        pass
        # global plot_vars
        # t = arange(0.0, 2.0, 0.1)
        # for key in plot_vars.keys():
        #     self.axes.plot(t, plot_vars[key])
        # t1 = arange(0.0, 3.0, 0.01)
        # t2 = arange(0.0, 3.0, 0.01)
        # s = sin(2*pi*t)
        # s1 = sin(3*pi*t)
        # s2 = sin(4*pi*t)
        # self.axes.plot(t, s)
        # self.axes.plot(t1, s1)
        # self.axes.plot(t2, s2)


class ApplicationWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(400, 400)
        l = QtWidgets.QVBoxLayout(self)
        self.sc = MyMplCanvas(self, width=20, height=20, dpi=100)

        l.addWidget(self.sc)

    def update_plotter_data(self, data, x_axis, y_axis):
        self.sc.update_plot(data, x_axis, y_axis)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

#
# qApp = QtWidgets.QApplication(sys.argv)
#
# aw = ApplicationWindow()
# aw.setWindowTitle("%s" % progname)
# aw.show()
# sys.exit(qApp.exec_())
# qApp.exec_()

# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# import random
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import setp
# from time import clock
# import os
# import numpy as np
#
#
# # class PlotterWindow(QWidget):
# #     def __init__(self, *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         self.setFixedSize(500, 500)
# #
# #
# #     def plot(self):
# #         c_time = [1,2,3,4,5,6,7,8,9]
# #
# #         python_time = [1,2,3,4,5,6,7,8,9]*2
# #         new_time = [1,2,3,4,5,6,7,8,9]*3
# #
# #         plt.savefig('result.pdf')
# #         fig = plt.figure(1)
# #         ax = plt.axes([0.1, 0.1, 0.8, 0.8])
# #         setp(ax, 'frame_on', False)
# #         # Plot here
# #
# #         ##############################################
# #         degree = np.arange(0, len(c_time))
# #         # python_time = degree  # replace with f(degree)
# #         # c_time = degree + 1 # replace with f(degree)
# #         ##############################################
# #         print('hey', os.getcwd())
# #         ax.plot(degree, c_time, label='Best', marker='o')
# #         ax.plot(degree, python_time, label='Worst', marker='o')
# #         ax.plot(degree, new_time, label='Mean', marker='o')
# #         # End Plot
# #         ax.set_xlabel(r'Iteration (n)')
# #         ax.set_ylabel(r'Competency')
# #         handle, label = ax.get_legend_handles_labels()
# #         ax.legend(handle, label, loc='upper left', bbox_to_anchor=(0.01, 0.99), ncol=1, labelspacing=0.3, fancybox=True,
# #                   shadow=True,
# #                   columnspacing=1, borderpad=0.2, title='', handletextpad=0.1,
# #                   numpoints=1, handlelength=1.5, markerscale=1)
# #         plt.savefig(os.path.join(os.getcwd(), 'result.png'))
# #
#
# c_time = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# python_time = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_time = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# fig = plt.figure(1)
# ax = plt.axes([0.1, 0.1, 0.8, 0.8])
# setp(ax, 'frame_on', False)
# # Plot here
#
# ##############################################
# degree = np.arange(0, len(c_time))
# # python_time = degree  # replace with f(degree)
# # c_time = degree + 1 # replace with f(degree)
# ##############################################
# print('hey', os.getcwd())
# ax.plot(degree, c_time, label='Best', marker='o')
# ax.plot(degree, python_time, label='Worst', marker='o')
# ax.plot(degree, new_time, label='Mean', marker='o')
# # End Plot
# ax.set_xlabel(r'Iteration (n)')
# ax.set_ylabel(r'Competency')
# handle, label = ax.get_legend_handles_labels()
# ax.legend(handle, label, loc='upper left', bbox_to_anchor=(0.01, 0.99), ncol=1, labelspacing=0.3, fancybox=True,
#           shadow=True,
#           columnspacing=1, borderpad=0.2, title='', handletextpad=0.1,
#           numpoints=1, handlelength=1.5, markerscale=1)
# plt.savefig(os.path.join(os.getcwd(), 'result.png'))
