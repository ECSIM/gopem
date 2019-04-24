from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox, QComboBox, QDoubleSpinBox
from PyQt5.QtWidgets import QWidget, QFrame, QHBoxLayout, QVBoxLayout, QScrollArea, QSizePolicy
from PyQt5.QtWidgets import QLabel, QPushButton

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


def get_name_widget():
    name = QLabel('OPEM (v' + str(Version) + ')')
    name.setAlignment(Qt.AlignCenter)
    return name


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.plotter = gopem.plotter.ApplicationWindow(parent=self)
        self.mode = []
        self.layout = []
        self.attributes = {}
        self.selectedMode = 0

        self.output = {}

        self.x_ax = QComboBox(self)
        self.y_ax = QComboBox(self)
        self.x_ax.currentTextChanged.connect(self.axis_changed)
        self.y_ax.currentTextChanged.connect(self.axis_changed)

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
        self.super = QHBoxLayout(self)
        self.main = QVBoxLayout(self)

        self.initialModes(self.menu.keys())
        for mode in self.mode:
            mode.setVisible(False)
        self.mode[0].setVisible(True)

        self.main.addWidget(get_name_widget())
        self.main.addWidget(self.HLine())
        lay_0 = QHBoxLayout()
        lay_0.addWidget(self.getComboWidget(self.menuKey))
        lay_0.addWidget(self.getTestCheckBox())
        self.main.addLayout(lay_0)
        for mode in self.mode:
            self.main.addWidget(mode)
        self.main.addWidget(self.getButtonWidget())
        self.main.addWidget(self.HLine())
        self.main.addWidget(QLabel("Description:"))
        self.description.setText(Description_Menu[self.menuKey[0]])
        self.des_link.setText('<a href="' + Description_Links[self.menuKey[0]] + '">Web Link</a>')
        self.main.addWidget(self.description)
        self.main.addWidget(self.des_link)
        self.setLayout(self.super)
        self.super.addLayout(self.main)
        self.super.addWidget(self.VLine())
        self.super.addWidget(self.getPlotterArea())

    def initialModes(self, menu):
        for i, _ in enumerate(menu):
            self.mode.append(QScrollArea(self))
            w = QWidget(self.mode[i])
            self.layout.append(QVBoxLayout(self.mode[i]))
            for f in self.get_attr_fields(i):
                self.layout[i].addLayout(f)
            w.setLayout(self.layout[i])
            self.mode[i].setWidget(w)
            self.mode[i].setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def getPlotterArea(self):
        w = QWidget(self)
        l = QVBoxLayout()
        w.setLayout(l)
        x_label = QLabel("X-Axis:")
        y_label = QLabel("Y-Axis:")
        ll = QHBoxLayout()
        ll.addWidget(x_label)
        ll.addWidget(self.x_ax)
        ll.addWidget(y_label)
        ll.addWidget(self.y_ax)
        ll.setAlignment(Qt.AlignLeft)
        l.addLayout(ll)
        l.addWidget(self.HLine())
        l.addWidget(self.plotter)
        return w

    def getButtonWidget(self):
        w = QWidget(self)
        resetBtn = QPushButton('Reset')
        analyseBtn = QPushButton('Analyse')
        layout = QHBoxLayout(self)
        layout.addWidget(resetBtn)
        layout.addWidget(analyseBtn)
        resetBtn.clicked.connect(self.reset_slt)
        analyseBtn.clicked.connect(self.analyse_slt)
        w.setLayout(layout)
        return w

    def getComboWidget(self, combo_list):
        combo = QComboBox(self)
        combo.currentIndexChanged.connect(self.mode_changed_slt)
        for k in combo_list:
            combo.addItem(k)
        combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        return combo

    def getTestCheckBox(self):
        self.test_checkbox = QCheckBox("Use Test Data")
        self.test_checkbox.stateChanged.connect(self.test_slt)
        return self.test_checkbox

    def get_attr_fields(self, mode):
        fields = []
        input_param = gopem.helper.InputParam[self.menuKey[mode]]
        name = self.menuKey[mode]
        self.attributes[name] = {}
        for item in sorted(list(input_param.keys())):
            field = QHBoxLayout(self)
            label = QLabel(item + ' ( ' + input_param[item] + ' ) : ')
            field.addWidget(label, alignment=Qt.AlignLeft)
            self.attributes[name][item] = QDoubleSpinBox(self)
            self.attributes[name][item].setRange(0, 100000)
            self.attributes[name][item].setMinimumSize(200, 20)
            self.attributes[name][item].setDecimals(10)
            field.addWidget(self.attributes[name][item], alignment=Qt.AlignRight)
            fields.append(field)
        return fields

    def reset_slt(self):
        for k in self.attributes[self.menuKey[self.selectedMode]].keys():
            self.attributes[self.menuKey[self.selectedMode]][k].setValue(0.0)
        print('reset')

    def analyze(self, menu, attributes):
        temp = {}
        for key, value in attributes.items():
            temp[key] = value.value()

        name = self.menuKey[self.selectedMode]
        input_attr = {"Name": name}
        for k in self.attributes[name].keys():
            input_attr[k] = self.attributes[name][k].value()
        print(input_attr)
        output = menu(input_attr, True, False, True)
        self.output = output
        print(output.keys())
        self.x_ax.clear()
        self.y_ax.clear()
        for k in output.keys():
            if isinstance(output[k], list):
                self.x_ax.addItem(str(k))
                self.y_ax.addItem(str(k))
        print(output)
        self.plotter.update_plotter_data(output, self.x_ax.currentText(), self.y_ax.currentText())

    def analyse_slt(self):
        print('analyse ... ')
        self.analyze(self.menu[self.menuKey[self.selectedMode]], self.attributes[self.menuKey[self.selectedMode]])
        print('analysed')

    def HLine(self):
        toto = QFrame(parent=self)
        toto.setFrameShape(QFrame.HLine)
        toto.setFrameShadow(QFrame.Sunken)
        return toto

    def VLine(self):
        toto = QFrame(parent=self)
        toto.setFrameShape(QFrame.VLine)
        toto.setFrameShadow(QFrame.Sunken)
        return toto

    def mode_changed_slt(self, index):
        for m in self.mode:
            m.setVisible(False)
        self.mode[index].setVisible(True)
        self.description.setText(Description_Menu[self.menuKey[index]])
        self.des_link.setText('<a href="' + Description_Links[self.menuKey[index]] + '">Web Link</a>')
        self.selectedMode = index
        self.test_checkbox.setChecked(False)

    def test_slt(self, state):
        if state == 2:
            name = self.menuKey[self.selectedMode]
            for k in self.attributes[name].keys():
                if k in Vectors[name].keys():
                    self.attributes[name][k].setValue(Vectors[name][k])

    def axis_changed(self):
        self.plotter.update_plotter_data(self.output, self.x_ax.currentText(), self.y_ax.currentText())
