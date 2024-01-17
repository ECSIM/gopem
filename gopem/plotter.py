# -*- coding: utf-8 -*-
"""GOPEM plotter."""
from __future__ import unicode_literals
import matplotlib
matplotlib.use('Qt5Agg')  # Make sure that we are using QT5
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import gopem.helper


class MplCanvas(FigureCanvas):
    """MplCanvas class."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        Initialize of MatPlotLib canvas for plotter.

        :param parent: the QWidget parent
        :param width: the initial width of canvas
        :param height: the initial height of canvas
        :param dpi: the dpi of the canvas
        """
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def update_plot(
            self,
            data,
            x_axis,
            y_axis,
            color,
            marker,
            style,
            x_scale,
            y_scale,
            linewidth,
            font_title,
            font_axes):
        """
        Update the data and axis range of the canvas.

        :param data: a dictionary that contains the data points
        :param x_axis: the ticks on X axis
        :param y_axis: the ticks on Y axis
        :param color: color name
        :param marker : data marker
        :param style: line style
        :param x_scale: x-axis scale
        :param y_scale: y-axis scale
        :param linewidth: plot line width
        :param font_title: title font size
        :param font_axes: axes labels font size
        :return: None
        """
        self.axes.cla()
        self.axes.grid(True, linestyle='-.', which='both')
        if x_axis in data and y_axis in data:
            x_unit = ""
            y_unit = ""
            title = ""
            self.axes.plot(
                data[x_axis],
                data[y_axis],
                color=color,
                marker=marker,
                linestyle=style,
                linewidth=linewidth)
            if y_axis in gopem.helper.UnitTable:
                title += gopem.helper.UnitTable[y_axis][0] + "~"
                if gopem.helper.UnitTable[y_axis][1] is not None:
                    y_unit = "({0})".format(gopem.helper.UnitTable[y_axis][1])
            if x_axis in gopem.helper.UnitTable:
                if title:
                    title += gopem.helper.UnitTable[x_axis][0]
                    self.axes.set_title(title, fontsize=font_title)
                if gopem.helper.UnitTable[x_axis][1] is not None:
                    x_unit = "({0})".format(gopem.helper.UnitTable[x_axis][1])
            self.axes.set_xlabel(x_axis + x_unit, fontsize=font_axes)
            self.axes.set_ylabel(y_axis + y_unit, fontsize=font_axes)
            self.axes.set_yscale(y_scale)
            self.axes.set_xscale(x_scale)
            self.axes.tick_params(labelsize=font_axes)

        self.draw()

    def save_fig(self, filename, transparent):
        """
        Save figure.

        :param filename: file name
        :param transparent: transparent flag
        :return: None
        """
        self.fig.savefig(filename, transparent=transparent)


class ApplicationWindow(QtWidgets.QWidget):
    """ApplicationWindow class."""

    def __init__(self, *args, **kwargs):
        """
        Application widget for MPLCanvas class.

        :param args: the list of arguments
        :param kwargs: the dictionary of keywords
        """
        super().__init__(*args, **kwargs)
        layout = QtWidgets.QVBoxLayout(self)
        self.canvas = MplCanvas(self, width=20, height=20, dpi=100)

        layout.addWidget(self.canvas)

    def update_plotter_data(
            self,
            data,
            x_axis,
            y_axis,
            color,
            marker,
            style,
            x_scale,
            y_scale,
            linewidth,
            font_title,
            font_axes):
        """
        Update the plotter data and axis.

        :param data: the dictionary of data
        :param x_axis: the Ticks on X axis
        :param y_axis:  the Ticks on Y axis
        :param color: color name
        :param marker : data marker
        :param style: line style
        :param x_scale: x-axis scale
        :param y_scale: y-axis scale
        :param linewidth: plot line width
        :param font_title: title font size
        :param font_axes: axes labels font size
        :return: None
        """
        if not font_title:
            font_title = gopem.helper.TitleFontDefault
        else:
            font_title = int(font_title)

        if not font_axes:
            font_axes = gopem.helper.AxesFontDefault
        else:
            font_axes = int(font_axes)

        if not linewidth:
            linewidth = 1
        else:
            linewidth = int(linewidth)

        if not marker:
            marker = ""
        else:
            marker = gopem.helper.MarkerTable[marker]
        if not color:
            color = gopem.helper.ColorList[0]
        if not x_scale:
            x_scale = gopem.helper.ScaleList[0]
        if not y_scale:
            y_scale = gopem.helper.ScaleList[0]
        if not style:
            style = gopem.helper.StyleTable["Solid"]
        else:
            style = gopem.helper.StyleTable[style]
        self.canvas.update_plot(
            data,
            x_axis,
            y_axis,
            color,
            marker,
            style,
            x_scale,
            y_scale,
            linewidth,
            font_title,
            font_axes)

    def file_quit(self):
        """
        Close the application.

        :return: None
        """
        self.close()

    def close_event(self):
        """
        Slot for close event trigger.

        :return: None
        """
        self.file_quit()

    def clear_plot(self):
        """
        Clear plot.

        :return: None
        """
        self.canvas.axes.cla()
