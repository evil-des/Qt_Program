import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import random


class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(lambda x: self.btnClicked(1))
        self.myFlag = -1

    def btnClicked(self, i):
        self.myFlag = i
        self.update()

    def paintEvent(self, e):
        super().paintEvent(e)
        qp = QPainter()
        qp.begin(self)
        self.draw_shape(qp)
        qp.end()

    def draw_shape(self, qp):
        if self.myFlag != 1:
            return

        if self.myFlag == 1:
            qp.setBrush(QColor(255, 255, 0))
            size = random.randint(30, 100)
            position = [random.randint(20, 50) for _ in range(2)]
            qp.drawEllipse(*position, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())
