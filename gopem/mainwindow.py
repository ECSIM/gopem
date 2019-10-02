"""GOPEM mainwindow."""
import requests
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox, QComboBox, QDoubleSpinBox, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QWidget, QFrame, QHBoxLayout, QVBoxLayout, QScrollArea, QSizePolicy
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont
from opem.Static.Amphlett import Static_Analysis as Amphlett_Analysis
from opem.Static.Larminie_Dicks import Static_Analysis as Larminiee_Analysis
from opem.Static.Chamberline_Kim import Static_Analysis as Chamberline_Kim_Analysis
from opem.Dynamic.Padulles1 import Dynamic_Analysis as Padulles1_Analysis
from opem.Dynamic.Padulles2 import Dynamic_Analysis as Padulles2_Analysis
from opem.Dynamic.Padulles_Hauer import Dynamic_Analysis as Padulles_Hauer_Analysis
from opem.Dynamic.Padulles_Amphlett import Dynamic_Analysis as Padulles_Amphlett_Analysis
from opem.Params import Version, Description_Menu, Description_Links, Vectors
import gopem.helper
import gopem.plotter


class MainWindow(QWidget):
    """MainWindow class."""

    def __init__(self):
        """Initialize of GUI window."""
        super(MainWindow, self).__init__()
        self.plotter = gopem.plotter.ApplicationWindow(parent=self)
        self.mode = []
        self.setWindowIcon(QIcon(gopem.helper.IconPath))
        self.layout = []
        self.attributes = {}
        self.selectedMode = 0

        self.output = {}

        self.x_ax = QComboBox(self)
        self.y_ax = QComboBox(self)
        self.color_bar = QComboBox(self)
        self.marker_bar = QComboBox(self)
        self.style_bar = QComboBox(self)
        self.x_scale = QComboBox(self)
        self.y_scale = QComboBox(self)
        self.line_width = QComboBox(self)
        self.config_plot_bar(min_width=130)

        self.test_checkbox = QCheckBox()

        self.description = QLabel()
        self.des_link = QLabel()
        self.des_link.setTextFormat(Qt.RichText)
        self.des_link.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.des_link.setOpenExternalLinks(True)
        self.menu = {
            "Amphlett_Analysis (Static)": Amphlett_Analysis,
            "Larminiee_Analysis (Static)": Larminiee_Analysis,
            "Chamberline_Kim_Analysis (Static)": Chamberline_Kim_Analysis,
            "Padulles_Analysis I (Dynamic)": Padulles1_Analysis,
            "Padulles_Analysis II (Dynamic)": Padulles2_Analysis,
            "Padulles_Hauer Analysis (Dynamic)": Padulles_Hauer_Analysis,
            "Padulles_Amphlett Analysis (Dynamic)": Padulles_Amphlett_Analysis}
        self.menuKey = list(self.menu.keys())
        self.menuKey.sort()
        self.super = QHBoxLayout()
        self.main = QVBoxLayout()

        self.initial_modes(self.menu.keys())
        for mode in self.mode:
            mode.setVisible(False)
        self.mode[0].setVisible(True)
        self.name_version = self.get_name_widget()
        self.main.addWidget(self.name_version)
        self.main.addWidget(self.h_line())
        lay_0 = QHBoxLayout()
        lay_0.addWidget(self.get_combo_widget(self.menuKey))
        lay_0.addWidget(self.get_test_check_box())
        self.main.addLayout(lay_0)
        for mode in self.mode:
            self.main.addWidget(mode)

        self.reportChkBox = QCheckBox()
        self.printChkBox = QCheckBox()
        self.main.addWidget(self.get_button_widget())
        self.main.addWidget(self.h_line())
        self.main.addWidget(QLabel("Description:"))
        self.description.setText(Description_Menu[self.menuKey[0]])
        self.des_link.setText('<a href="' +
                              Description_Links[self.menuKey[0]] +
                              '">Web Link</a>')
        self.main.addWidget(self.description)
        self.main.addWidget(self.des_link)
        self.setLayout(self.super)
        self.super.addLayout(self.main)
        self.super.addWidget(self.v_line())
        self.super.addWidget(self.get_plotter_area())

    def config_plot_bar(self, min_width=140):
        """
        Set config for plot setting bar.

        :param min_width: minimum width
        :return: None
        """
        self.x_ax.setMinimumWidth(min_width)
        self.y_ax.setMinimumWidth(min_width)
        self.color_bar.setMinimumWidth(min_width)
        self.marker_bar.setMinimumWidth(min_width)
        self.style_bar.setMinimumWidth(min_width)
        self.x_scale.setMinimumWidth(min_width)
        self.y_scale.setMinimumWidth(min_width)
        self.line_width.setMinimumWidth(min_width)
        self.x_ax.currentTextChanged.connect(self.axis_changed)
        self.y_ax.currentTextChanged.connect(self.axis_changed)
        self.color_bar.currentTextChanged.connect(self.axis_changed)
        self.marker_bar.currentTextChanged.connect(self.axis_changed)
        self.style_bar.currentTextChanged.connect(self.axis_changed)
        self.x_scale.currentTextChanged.connect(self.axis_changed)
        self.y_scale.currentTextChanged.connect(self.axis_changed)
        self.line_width.currentTextChanged.connect(self.axis_changed)

    def location_on_screen(self, x=0, y=0):
        """
        Set window location.

        :param x: x-axis
        :param y: y-axis
        :return: None
        """
        self.move(x, y)

    def message_box(self, title, message):
        """
        Show message box.

        :param title: title of window
        :param message: message text
        :return: None
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setTextFormat(Qt.RichText)
        msg.setWindowTitle(title)
        msg.setText(message)
        try:
            msg.setWindowIcon(QIcon(gopem.helper.IconPath))
        except Exception as e:
            print(str(e))
        msg.exec_()

    def get_name_widget(self):
        """
        Top widget that shows the names and versions of OPEM/GOPEM.

        :return: containing the names and versions of the OPEM/GOPEM
        """
        name = QLabel(gopem.helper.VersionText, self)
        name.setAlignment(Qt.AlignCenter)
        name.setFont(QFont("Times", 12, QFont.Bold))
        return name

    def edit_name_widget(self, analyse=True):
        """
        Edit name_version widget in different mode.

        :param analyse: analyse mode flag
        :return: None
        """
        if analyse:
            self.name_version.setText(gopem.helper.AnalyzingMessage)
            self.name_version.setStyleSheet("color:red;")
            self.repaint()
        else:
            self.name_version.setText(gopem.helper.VersionText)
            self.name_version.setStyleSheet("color:black;")
            self.repaint()

    def initial_modes(self, menu):
        """
        Generate a page for each model in OPEM and put them on each other.

        :param menu: the dictionary of OPEM models
        :return: None
        """
        for i, _ in enumerate(menu):
            self.mode.append(QScrollArea(self))
            w = QWidget(self.mode[i])
            self.layout.append(QVBoxLayout(self.mode[i]))
            for f in self.get_attr_fields(i):
                self.layout[i].addLayout(f)
            w.setLayout(self.layout[i])
            self.mode[i].setWidget(w)
            self.mode[i].setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def get_plotter_area(self):
        """
        Initialize the plotter widget.

        :return: QWidget for plotter layer
        """
        w = QWidget(self)
        l = QVBoxLayout()
        w.setLayout(l)
        x_label = QLabel("X-Axis:")
        y_label = QLabel("Y-Axis:")
        color_label = QLabel("Color:")
        marker_label = QLabel("Marker:")
        style_label = QLabel("Style:")
        x_scale_label = QLabel("X-Scale:")
        y_scale_label = QLabel("Y-Scale:")
        line_width_label = QLabel("Line Width:")
        saveBtn = QPushButton('Save Plot')
        checkBtn = QPushButton('Check Update')
        saveBtn.clicked.connect(self.save_slt)
        checkBtn.clicked.connect(self.check_update)
        ll = QHBoxLayout()
        ll.addWidget(x_label)
        ll.addWidget(self.x_ax)
        ll.addWidget(y_label)
        ll.addWidget(self.y_ax)
        ll.addWidget(x_scale_label)
        ll.addWidget(self.x_scale)
        ll.addWidget(y_scale_label)
        ll.addWidget(self.y_scale)
        ll.addWidget(color_label)
        ll.addWidget(self.color_bar)
        ll.addWidget(marker_label)
        ll.addWidget(self.marker_bar)
        ll.addWidget(style_label)
        ll.addWidget(self.style_bar)
        ll.addWidget(line_width_label)
        ll.addWidget(self.line_width)
        ll.setAlignment(Qt.AlignLeft)
        l.addLayout(ll)
        l.addWidget(self.h_line())
        l.addWidget(self.plotter)
        l.addWidget(self.h_line())
        lll = QHBoxLayout()
        lll.addWidget(checkBtn)
        lll.addWidget(saveBtn)
        l.addLayout(lll)
        return w

    def get_button_widget(self):
        """
        Initialize and construct reset, analyse buttons and connection.

        :return: QWidget of buttons Layer
        """
        w = QWidget(self)
        resetBtn = QPushButton('Reset')
        analyseBtn = QPushButton('Analyse')
        self.reportChkBox = QCheckBox(gopem.helper.ReportTitle)
        self.printChkBox = QCheckBox(gopem.helper.PrintTitle)
        self.printChkBox.setDisabled(True)
        layout_v = QVBoxLayout(self)
        layout = QHBoxLayout()
        layout.addWidget(resetBtn)
        layout.addWidget(analyseBtn)
        resetBtn.clicked.connect(self.reset_slt)
        analyseBtn.clicked.connect(self.analyse_slt)
        self.reportChkBox.stateChanged.connect(self.report_slt)
        layout_v.addLayout(layout)
        layout_v.addWidget(self.reportChkBox)
        layout_v.addWidget(self.printChkBox)
        w.setLayout(layout_v)
        return w

    def get_combo_widget(self, combo_list):
        """
        Construct the combo box of models.

        :param combo_list: the list of models
        :return: QComboBox of models
        """
        combo = QComboBox(self)
        combo.currentIndexChanged.connect(self.mode_changed_slt)
        for k in combo_list:
            combo.addItem(k)
        combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        return combo

    def get_test_check_box(self):
        """
        Construct and initialize of the check box for test data and its connections.

        :return: QCheckBox for test data
        """
        self.test_checkbox = QCheckBox(gopem.helper.TestTitle)
        self.test_checkbox.stateChanged.connect(self.test_slt)
        return self.test_checkbox

    def get_attr_fields(self, mode):
        """
        Return the list of attributes for the given model.

        :param mode: the model to get its attributes
        :return: the list of attributes for the given model
        """
        fields = []
        input_param = gopem.helper.InputParam[self.menuKey[mode]]
        name = self.menuKey[mode]
        self.attributes[name] = {}
        for item in sorted(list(input_param.keys())):
            field = QHBoxLayout()
            label = QLabel(item + ' ( ' + input_param[item] + ' ) : ')
            field.addWidget(label, alignment=Qt.AlignLeft)
            self.attributes[name][item] = QDoubleSpinBox(self)
            self.attributes[name][item].setRange(0, 100000)
            self.attributes[name][item].setMinimumSize(200, 20)
            self.attributes[name][item].setDecimals(10)
            field.addWidget(
                self.attributes[name][item],
                alignment=Qt.AlignRight)
            fields.append(field)
        return fields

    def reset_slt(self):
        """
        Slot function for the reset button, it will set all the attributes value to 0.0, clear plot and reset checkbox.

        :return: None
        """
        for k in self.attributes[self.menuKey[self.selectedMode]].keys():
            self.attributes[self.menuKey[self.selectedMode]][k].setValue(0.0)
        self.reportChkBox.setChecked(False)
        self.test_checkbox.setChecked(False)
        self.printChkBox.setChecked(False)
        self.printChkBox.setDisabled(True)
        self.x_ax.clear()
        self.y_ax.clear()
        self.color_bar.clear()
        self.marker_bar.clear()
        self.style_bar.clear()
        self.x_scale.clear()
        self.y_scale.clear()
        self.plotter.clear_plot()

    def analyze(self, menu, attributes):
        """
        Start an analysis by the selected model and given attributes values.

        :param menu: the model that analysis is based on
        :param attributes: the value of each parameter of model
        :return: None
        """
        temp = {}
        report_flag = self.reportChkBox.isChecked()
        print_flag = self.printChkBox.isChecked()
        for key, value in attributes.items():
            temp[key] = value.value()

        name = self.menuKey[self.selectedMode]
        input_attr = {"Name": name}
        for k in self.attributes[name].keys():
            input_attr[k] = self.attributes[name][k].value()
        self.edit_name_widget(True)
        output = menu(
            input_attr,
            True,
            print_flag,
            report_flag)  # Test Print Report
        self.edit_name_widget(False)
        self.output = output
        self.color_bar.clear()
        for color in gopem.helper.ColorList:
            self.color_bar.addItem(color)
        self.marker_bar.clear()
        for marker in gopem.helper.MarkerList:
            self.marker_bar.addItem(marker)
        self.style_bar.clear()
        for style in gopem.helper.StyleList:
            self.style_bar.addItem(style)
        self.x_scale.clear()
        self.y_scale.clear()
        for scale in gopem.helper.ScaleList:
            self.x_scale.addItem(scale)
            self.y_scale.addItem(scale)
        self.line_width.clear()
        for width in gopem.helper.WidthList:
            self.line_width.addItem(str(width))
        self.x_ax.clear()
        self.y_ax.clear()
        for k in output.keys():
            if isinstance(output[k], list):
                self.x_ax.addItem(str(k))
                self.y_ax.addItem(str(k))
        self.plotter.update_plotter_data(
            output,
            self.x_ax.currentText(),
            self.y_ax.currentText(),
            self.color_bar.currentText(),
            self.marker_bar.currentText(),
            self.style_bar.currentText(),
            self.x_scale.currentText(),
            self.y_scale.currentText(),
            self.line_width.currentText())
        if report_flag:
            self.message_box("Report", gopem.helper.ReportMessage)

    def analyse_slt(self):
        """
        Slot function for the analyse button.

        :return: None
        """
        self.analyze(self.menu[self.menuKey[self.selectedMode]],
                     self.attributes[self.menuKey[self.selectedMode]])

    def report_slt(self):
        """
        Slot function for the report checkbox.

        :return: None
        """
        if self.reportChkBox.isChecked():
            self.printChkBox.setEnabled(True)
        else:
            self.printChkBox.setEnabled(False)

    def h_line(self):
        """
        Generate a horizontal line with QFrame.

        :return: QFrame looks like a horizontal separator line
        """
        toto = QFrame(parent=self)
        toto.setFrameShape(QFrame.HLine)
        toto.setFrameShadow(QFrame.Sunken)
        return toto

    def v_line(self):
        """
        Generate a vertical line with QFrame.

        :return: QFrame looks like a vertical separator line
        """
        toto = QFrame(parent=self)
        toto.setFrameShape(QFrame.VLine)
        toto.setFrameShadow(QFrame.Sunken)
        return toto

    def mode_changed_slt(self, index):
        """
        Slot function for mode selector ComboBox.

        :param index: the index of the model that has been selected
        :return: None
        """
        for m in self.mode:
            m.setVisible(False)
        self.mode[index].setVisible(True)
        self.description.setText(Description_Menu[self.menuKey[index]])
        self.des_link.setText('<a href="' +
                              Description_Links[self.menuKey[index]] +
                              '">Web Link</a>')
        self.selectedMode = index
        self.test_checkbox.setChecked(False)

    def test_slt(self, state):
        """
        The slot function for test CheckBox.

        :param state: the state of the check box
        :return: None
        """
        if state == 2:
            name = self.menuKey[self.selectedMode]
            for k in self.attributes[name].keys():
                if k in Vectors[name].keys():
                    self.attributes[name][k].setValue(Vectors[name][k])

    def axis_changed(self):
        """
        Slot function for the axis selector comboBox.

        :return: None
        """
        self.plotter.update_plotter_data(
            self.output,
            self.x_ax.currentText(),
            self.y_ax.currentText(),
            self.color_bar.currentText(),
            self.marker_bar.currentText(),
            self.style_bar.currentText(),
            self.x_scale.currentText(),
            self.y_scale.currentText(),
            self.line_width.currentText())

    def save_slt(self):
        """
        Save slot.

        :return: None
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Plot", "", "PNG (*.png)", options=options)
        if filename:
            self.plotter.sc.save_fig(filename)
            self.message_box("Save Plot", gopem.helper.PlotMessage)

    def check_update(self):
        """
        Check for new gopem version in website.

        :return: None
        """
        try:
            update_obj = requests.get(gopem.helper.UpdateUrl)
            update_data = update_obj.text
            if float(update_data) > float(gopem.helper.Version):
                self.message_box("Check Update", gopem.helper.UpdateMessage2.format(
                    str(gopem.helper.Version), update_data))
            else:
                self.message_box("Check Update", gopem.helper.UpdateMessage1.format(
                    str(gopem.helper.Version), update_data))
        except Exception:
            self.message_box("Check Update", gopem.helper.UpdateMessage3.format(
                str(gopem.helper.Version), "??"))
