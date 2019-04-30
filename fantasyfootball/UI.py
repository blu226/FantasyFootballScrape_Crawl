import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel, QFormLayout, QSpinBox, QVBoxLayout, QMainWindow
from PyQt5.QtCore import *
import time

class UIWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("UIWindow")
        self.centralwidget = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        year_label = QLabel("Season: " + str(MainWindow.season), MainWindow)
        start_label = QLabel("Start week: " + str(MainWindow.start), MainWindow)
        end_label = QLabel("End week: " + str(MainWindow.end), MainWindow)
        qb_label = QLabel("# QB: " + str(MainWindow.qb), MainWindow)
        rb_label = QLabel("# RB: " + str(MainWindow.rb), MainWindow)
        te_label = QLabel("# TE: " + str(MainWindow.te), MainWindow)
        wr_label = QLabel("# WR: " + str(MainWindow.wr), MainWindow)
        flex_label = QLabel("# Flex: " + str(MainWindow.flex), MainWindow)
        def_label = QLabel("# Def: " + str(MainWindow.defense), MainWindow)
        k_label = QLabel("# Kicker: " + str(MainWindow.k), MainWindow)
        self.ToolsBTN = QPushButton('edit', self.centralwidget)
        self.SubmitBTN = QPushButton('generate', self.centralwidget) #Brad

        labels = [year_label, start_label, end_label, qb_label, rb_label, wr_label, te_label,  flex_label, k_label, def_label, self.ToolsBTN, self.SubmitBTN] #~Brad

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignLeft)

        for label in labels:
            vbox.addWidget(label)

        self.centralwidget.setLayout(vbox)
        # self.ToolsBTN.move(50, 350)
        MainWindow.setCentralWidget(self.centralwidget)


class UIToolTab(object):
    def __init__(self, MainWindow):
        self.start = MainWindow.start
        self.end = MainWindow.end
        self.season = MainWindow.season
        self.qb = MainWindow.qb
        self.rb = MainWindow.rb
        self.wr = MainWindow.wr
        self.te = MainWindow.te
        self.flex = MainWindow.flex
        self.defense = MainWindow.defense
        self.k = MainWindow.k

    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("UIToolTab")
        self.centralwidget = QWidget(MainWindow)

        self.year_spinbox = QSpinBox()
        self.year_spinbox.setRange(1970, 2018)
        self.year_spinbox.setValue(self.season)
        self.year_spinbox.valueChanged.connect(self.year_valuechange)

        self.start_spinbox = QSpinBox()
        self.start_spinbox.setRange(1, 17)
        self.start_spinbox.setValue(self.start)
        self.start_spinbox.valueChanged.connect(self.start_valuechange)


        self.end_spinbox = QSpinBox()
        self.end_spinbox.setRange(self.start, 17)
        self.end_spinbox.setValue(self.end)
        self.end_spinbox.valueChanged.connect(self.end_valuechange)


        self.qb_spinbox = QSpinBox()
        self.qb_spinbox.setRange(0, 5)
        self.qb_spinbox.setValue(self.qb)
        self.qb_spinbox.valueChanged.connect(self.qb_valuechange)


        self.rb_spinbox = QSpinBox()
        self.rb_spinbox.setRange(0, 5)
        self.rb_spinbox.setValue(self.rb)
        self.rb_spinbox.valueChanged.connect(self.rb_valuechange)


        self.wr_spinbox = QSpinBox()
        self.wr_spinbox.setRange(0, 5)
        self.wr_spinbox.setValue(self.wr)
        self.wr_spinbox.valueChanged.connect(self.wr_valuechange)


        self.te_spinbox = QSpinBox()
        self.te_spinbox.setRange(0, 5)
        self.te_spinbox.setValue(self.te)
        self.te_spinbox.valueChanged.connect(self.te_valuechange)


        self.f_spinbox = QSpinBox()
        self.f_spinbox.setRange(0, 5)
        self.f_spinbox.setValue(self.flex)
        self.f_spinbox.valueChanged.connect(self.flex_valuechange)


        self.d_spinbox = QSpinBox()
        self.d_spinbox.setRange(0, 5)
        self.d_spinbox.setValue(self.defense)
        self.d_spinbox.valueChanged.connect(self.d_valuechange)


        self.k_spinbox = QSpinBox()
        self.k_spinbox.setRange(0, 5)
        self.k_spinbox.setValue(self.k)
        self.k_spinbox.valueChanged.connect(self.k_valuechange)



        layout = QFormLayout()
        layout.addRow(QLabel("Season:"), self.year_spinbox)
        layout.addRow(QLabel("Start week:"), self.start_spinbox)
        layout.addRow(QLabel("End week:"), self.end_spinbox)
        layout.addRow(QLabel("# QB:"), self.qb_spinbox)
        layout.addRow(QLabel("# RB:"), self.rb_spinbox)
        layout.addRow(QLabel("# WR:"), self.wr_spinbox)
        layout.addRow(QLabel("# TE:"), self.te_spinbox)
        layout.addRow(QLabel("# Flex:"), self.f_spinbox)
        layout.addRow(QLabel("# K:"), self.k_spinbox)
        layout.addRow(QLabel("# Def:"), self.d_spinbox)


        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignLeft)
        vbox.addLayout(layout)
        self.CPSBTN = QPushButton("save", self.centralwidget)

        vbox.addWidget(self.CPSBTN)

        self.centralwidget.setLayout(vbox)

        MainWindow.setCentralWidget(self.centralwidget)

    def setupResultsUI(self, MainWindow): #Brad
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("ResultsUIToolTab")
        self.centralwidget = QWidget(MainWindow)

        qb_label = QLabel(" QB: " + str(1), MainWindow)
        rb_label = QLabel(" RB: " + str(1), MainWindow)
        te_label = QLabel(" TE: " + str(1), MainWindow)
        wr_label = QLabel(" WR: " + str(1), MainWindow)
        flex_label = QLabel(" Flex: " + str(1), MainWindow)
        def_label = QLabel(" Def: " + str(1), MainWindow)
        k_label = QLabel(" Kicker: " + str(1), MainWindow)

        labels = [qb_label, rb_label, wr_label, te_label, flex_label, k_label, def_label]

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignLeft)

        for label in labels:
            vbox.addWidget(label)

        self.centralwidget.setLayout(vbox)
        # self.ToolsBTN.move(50, 350)
        MainWindow.setCentralWidget(self.centralwidget)

    def year_valuechange(self):
        self.season = self.year_spinbox.value()

    def start_valuechange(self):
        self.start = self.start_spinbox.value()

    def end_valuechange(self):
        self.end = self.end_spinbox.value()

    def qb_valuechange(self):
        self.qb = self.qb_spinbox.value()

    def rb_valuechange(self):
        self.rb = self.rb_spinbox.value()

    def wr_valuechange(self):
        self.wr = self.wr_spinbox.value()

    def te_valuechange(self):
        self.te = self.te_spinbox.value()

    def flex_valuechange(self):
        self.flex = self.f_spinbox.value()

    def k_valuechange(self):
        self.k = self.k_spinbox.value()

    def d_valuechange(self):
        self.defense = self.d_spinbox.value()




class MainWindow(QMainWindow):
    def __init__(self,  parent=None):
        super(MainWindow, self).__init__(parent)
        self.start = 1
        self.end = 1
        self.season = 2018
        self.qb = 1
        self.rb = 2
        self.wr = 2
        self.te = 1
        self.flex = 1
        self.defense = 1
        self.k = 1
        self.uiWindow = UIWindow()
        self.uiToolTab = UIToolTab(self)
        self.startUIWindow()

    def startUIToolTab(self):
        self.uiToolTab.setupUI(self)
        self.uiToolTab.CPSBTN.clicked.connect(self.startUIWindow)
        self.show()

    def genTeamTab(self):
        self.uiToolTab.setupResultsUI(self)
        self.uiToolTab.DBTN.clicked.connect(self.startUIWindow)
        self.show()


    def startUIWindow(self):
        self.season = self.uiToolTab.season
        self.start = self.uiToolTab.start
        self.end = self.uiToolTab.end
        self.qb = self.uiToolTab.qb
        self.rb = self.uiToolTab.rb
        self.wr = self.uiToolTab.wr
        self.te = self.uiToolTab.te
        self.flex = self.uiToolTab.flex
        self.defense = self.uiToolTab.defense
        self.k = self.uiToolTab.k
        self.uiWindow.setupUI(self)
        self.uiWindow.ToolsBTN.clicked.connect(self.startUIToolTab)
        self.uiWindow.SubmitBTN.clicked.connect(self.genTeamTab) #Brad
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
