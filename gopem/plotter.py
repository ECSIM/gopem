from __future__ import unicode_literals
import matplotlib
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')  # Make sure that we are using QT5


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        The Constructor of MatPlotLib Canvas for plotter
        :param parent: The QWidfet Parent
        :param width: The initial width of canvas
        :param height: The initial height of canvas
        :param dpi: The dpi of the canvas
        """
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
        """
        Update the Data and axis range of the canvas
        :param data: A dictionary that contains the data points
        :param x_axis: The ticks on X axis
        :param y_axis: The ticks on Y axis
        :return: None
        """
        self.axes.cla()
        self.axes.grid(True, linestyle='-.', which='both')
        if x_axis in data.keys() and y_axis in data.keys():
            self.axes.plot(data[x_axis], data[y_axis], 'r')
            self.axes.set_xlabel(x_axis)
            self.axes.set_ylabel(y_axis)

        self.draw()


class ApplicationWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(400, 400)
        l = QtWidgets.QVBoxLayout(self)
        self.sc = MyMplCanvas(self, width=20, height=20, dpi=100)

        l.addWidget(self.sc)

    def update_plotter_data(self, data, x_axis, y_axis):
        self.sc.update_plot(data, x_axis, y_axis)

    def file_quit(self):
        self.close()

    def close_event(self, ce):
        self.file_quit()
