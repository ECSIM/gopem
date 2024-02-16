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
        :type parent: QWidget
        :param width: the initial width of canvas
        :type width: int
        :param height: the initial height of canvas
        :type height: int
        :param dpi: the dpi of the canvas
        :type dpi: int
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
        :type data: dict
        :param x_axis: the ticks on X axis
        :type x_axis: str
        :param y_axis: the ticks on Y axis
        :type y_axis: str
        :param color: color name
        :type color: str
        :param marker : data marker
        :type marker: str
        :param style: line style
        :type style: str
        :param x_scale: x-axis scale
        :type x_scale: str
        :param y_scale: y-axis scale
        :type y_scale: str
        :param linewidth: plot line width
        :type linewidth: float
        :param font_title: title font size
        :type font_title: int
        :param font_axes: axes labels font size
        :type font_axes: int
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
        :type filename: str
        :param transparent: transparent flag
        :type transparent: bool
        :return: None
        """
        self.fig.savefig(filename, transparent=transparent)


class ApplicationWindow(QtWidgets.QWidget):
    """ApplicationWindow class."""

    def __init__(self, *args, **kwargs):
        """
        Application widget for MPLCanvas class.

        :param args: the list of arguments
        :type args: list
        :param kwargs: the dictionary of keywords
        :type kwargs: dict
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
        :type data: dict
        :param x_axis: the Ticks on X axis
        :type x_axis: str
        :param y_axis:  the Ticks on Y axis
        :type y_axis: str
        :param color: color name
        :type color: str
        :param marker : data marker
        :type marker: str
        :param style: line style
        :type style: str
        :param x_scale: x-axis scale
        :type x_scale: str
        :param y_scale: y-axis scale
        :type y_scale: str
        :param linewidth: plot line width
        :type linewidth: float
        :param font_title: title font size
        :type font_title: int
        :param font_axes: axes labels font size
        :type font_axes: int
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
