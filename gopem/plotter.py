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
import sys
import os
import random
import matplotlib
from PyQt5 import QtCore, QtWidgets
from numpy import arange, sin, pi
matplotlib.use('Qt5Agg')  # Make sure that we are using QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

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


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.cla()
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()


class ApplicationWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(400, 400)
        l = QtWidgets.QVBoxLayout(self)
        sc = MyStaticMplCanvas(self, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self, width=5, height=4, dpi=100)

        l.addWidget(sc)
        l.addWidget(dc)

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
#qApp.exec_()

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
