from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import Qt
from UI import Ui_Dialog
from random import randint
import sys


class MyWidget(Ui_Dialog, QMainWindow):
    def __init__(self):
        super().__init__()
        self.qp = QPainter(self)
        self.i = randint(1, 11)
        self.setupUi(self)
        self.qp.begin(self)
        self.qp.setBrush(QColor(255, 255, 255, 0))
        self.pushButton.clicked.connect(self.do)
        self.qp.end()

    def do(self):
        for i in range(self.i):

            x, y, a = randint(1, 951), randint(1, 751), randint(1, 476)
            self.qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
