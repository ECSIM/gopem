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
