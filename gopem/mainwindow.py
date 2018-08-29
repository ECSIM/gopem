from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from opem.Static.Amphlett import Static_Analysis as Amphlett_Analysis
from opem.Static.Larminie_Dicks import Static_Analysis as Larminiee_Analysis
from opem.Static.Chamberline_Kim import Static_Analysis as Chamberline_Kim_Analysis
from opem.Dynamic.Padulles1 import Dynamic_Analysis as Padulles1_Analysis
from opem.Dynamic.Padulles2 import Dynamic_Analysis as Padulles2_Analysis
from opem.Dynamic.Padulles_Hauer import Dynamic_Analysis as Padulles_Hauer_Analysis
from opem.Dynamic.Padulles_Amphlett import Dynamic_Analysis as Padulles_Amphlett_Analysis
from art import tprint
from opem.Params import Version, Description_Menu, Description_Links, Vectors
from opem.Functions import check_update, description_print, description_control
import gopem.helper
import gopem.plotter


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.plotter = gopem.plotter.ApplicationWindow(parent=self)
        self.mode = []
        self.layout = []
        self.attributes = {}
        self.selectedMode = 0
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

        self.main.addWidget(self.getNameWidget())
        self.main.addWidget(self.HLine())
        self.main.addWidget(self.getComboWidget(self.menuKey))
        for mode in self.mode:
            self.main.addWidget(mode)
        self.main.addWidget(self.getButtonWidget())
        self.main.addWidget(self.HLine())
        self.main.addWidget(QLabel("Description:"))
        self.description.setText(Description_Menu[self.menuKey[0]])
        self.des_link.setText('<a href="'+Description_Links[self.menuKey[0]]+'">Web Link</a>')
        self.main.addWidget(self.description)
        self.main.addWidget(self.des_link)
        self.setLayout(self.super)
        self.super.addLayout(self.main)
        self.super.addWidget(self.VLine())
        self.super.addWidget(self.plotter)

    def initialModes(self, menu):
        for i, k in enumerate(menu):
            self.mode.append(QScrollArea(self))
            w = QWidget(self.mode[i])
            self.layout.append(QVBoxLayout(self.mode[i]))
            for f in self.get_attr_fields(i):
                self.layout[i].addLayout(f)
            w.setLayout(self.layout[i])
            self.mode[i].setWidget(w)
            self.mode[i].setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            # self.mode[i].setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

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

    def getComboWidget(self, list):
        combo = QComboBox(self)
        combo.currentIndexChanged.connect(self.mode_changed_slt)
        for k in list:
            combo.addItem(k)
        return combo

    def getNameWidget(self):
        name = QLabel('OPEM')
        name.setAlignment(Qt.AlignCenter)
        return name

    def get_attr_fields(self, mode):
        fields = []
        input_param = gopem.helper.InputParam[self.menuKey[mode]]
        for item in sorted(list(input_param.keys())):
            field = QHBoxLayout(self)
            label = QLabel(item + ' ( ' + input_param[item] + ' ) : ')
            field.addWidget(label, alignment=Qt.AlignLeft)
            self.attributes[item] = QDoubleSpinBox(self)
            self.attributes[item].setRange(0, 100000)
            self.attributes[item].setMinimumSize(200, 20)
            self.attributes[item].setDecimals(10)
            field.addWidget(self.attributes[item], alignment=Qt.AlignRight)
            fields.append(field)
        return fields

    def reset_slt(self):
        for k in self.attributes.keys():
            self.attributes[k].setValue(0.0)
        print('reset')

    def analyze(self, menu, attributes):
        temp = {}
        for key, value in attributes.items():
            temp[key] = value.value()
        menu[self.menuKey[self.selectedMode]](temp, True)

    def analyse_slt(self):
        print('analyse ... ')

        self.analyze(self.menu, self.attributes)
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
        self.des_link.setText('<a href="'+Description_Links[self.menuKey[index]]+'">Web Link</a>')
        self.selectedMode = index
