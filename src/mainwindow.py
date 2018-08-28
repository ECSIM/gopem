from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from opem.Params import Amphlett_InputParams as A_Input
from opem.Params import Chamberline_InputParams as C_Input
from opem.Params import Larminiee_InputParams as L_Input
from opem.Params import Padulles_InputParams as P_Input
import src.plotter


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.plotter = src.plotter.ApplicationWindow(parent=self)
        self.mode = []
        self.layout = []
        self.attributes = {}
        self.selectedMode = 0
        self.menu = menu
        self.menuKey = list(menu.keys())
        self.menuKey.sort()
        self.super = QHBoxLayout(self)
        self.main = QVBoxLayout(self)

        self.initialModes(menu.keys())
        for mode in self.mode:
            mode.setVisible(False)
        self.mode[0].setVisible(True)

        self.main.addWidget(self.getNameWidget())
        self.main.addWidget(self.HLine())
        self.main.addWidget(self.getComboWidget(self.menuKey))
        for mode in self.mode:
            self.main.addWidget(mode)
        self.main.addWidget(self.getButtonWidget())
        self.setLayout(self.super)
        self.super.addLayout(self.main)
        self.super.addWidget(self.VLine())
        self.super.addWidget(self.plotter)

    def initialModes(self, menu):
        for i, k in enumerate(menu):
            self.mode.append(QWidget(self))
            self.layout.append(QVBoxLayout(self.mode[i]))
            for f in self.get_attr_fields(i):
                self.layout[i].addLayout(f)
            self.mode[i].setLayout(self.layout[i])

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
        combo.currentIndexChanged.connect(self.mode_changed_slt);
        for k in list:
            combo.addItem(k)
        return combo

    def getNameWidget(self):
        name = QLabel('OPEM')
        name.setAlignment(Qt.AlignCenter)
        return name

    def get_attr_fields(self, mode):
        fields = []
        Input = {}
        if mode == 0:
            Input = A_Input
        elif mode == 1:
            Input = C_Input
        elif mode == 2:
            Input = L_Input
        elif mode == 3:
            Input = P_Input
        else:
            return fields

        for item in sorted(list(Input.keys())):
            field = QHBoxLayout(self)
            label = QLabel(item + ' ( ' + Input[item] + ' ) : ')
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
        self.selectedMode = index
