import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *

class Ui(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        year_label = QLabel("Year:", self)
        start_label = QLabel("Start week:", self)
        end_label = QLabel("End week:", self)
        qb_label = QLabel("# QB:", self)
        rb_label = QLabel("# RB:", self)
        te_label = QLabel("# TE:", self)
        wr_label = QLabel("# WR:", self)
        flex_label = QLabel("# Flex:", self)
        

        start_week = QComboBox(self)
        end_week = QComboBox(self)
        year = QComboBox(self)
        num_QB = QComboBox(self)
        num_RB = QComboBox(self)
        num_WR = QComboBox(self)
        num_TE = QComboBox(self)
        num_flex = QComboBox(self)

        labels = [year_label, start_label, end_label, qb_label, rb_label, te_label, wr_label, flex_label]
        dropdowns = [year, start_week, end_week, num_QB, num_RB, num_TE, num_WR, num_flex]

        for i in range(1, 18):
            i = str(i)
            start_week.addItem(i)
            end_week.addItem(i)
            if int(i) < 5:
                num_QB.addItem(i)
                num_RB.addItem(i)
                num_WR.addItem(i)
                num_TE.addItem(i)
                num_flex.addItem(i)

        for i in range(1970, 2019):
            i = str(i)
            year.addItem(i)

        year.activated[str].connect(self.onActivated)
        start_week.activated[str].connect(self.onActivated)
        end_week.activated[str].connect(self.onActivated)
        num_QB.activated[str].connect(self.onActivated)
        num_RB.activated[str].connect(self.onActivated)
        num_WR.activated[str].connect(self.onActivated)
        num_TE.activated[str].connect(self.onActivated)
        num_flex.activated[str].connect(self.onActivated)

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.setAlignment(Qt.AlignTop)
        # vbox.addStretch(0)
        # hbox.addStretch(0)
        for label in labels:
            hbox.addWidget(label)

        # vbox.addLayout(hbox)


        # year_label.move(10, 10)
        # start_label.move(50, 10)
        # end_label.move(90, 10)
        # qb_label.move(130, 10)
        # rb_label.move(170, 10)
        # wr_label.move(210, 10)
        # te_label.move(250, 10)
        # flex_label.move(290, 10)

        year.move(100, 50)
        start_week.move(75, 75)
        end_week.move(75, 100)
        num_QB.move(75, 125)
        num_RB.move(75, 150)
        num_WR.move(75, 175)
        num_TE.move(75, 200)
        num_flex.move(75, 225)

        self.setLayout(hbox)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Fantasy Football Lineup Generator')
        self.show()

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui()
    sys.exit(app.exec_())



