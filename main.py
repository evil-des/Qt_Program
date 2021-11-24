import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random
from UI import Ui_MainWindow


class Program(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
            size = random.randint(30, 100)
            position = [random.randint(20, 50) for _ in range(2)]
            color = [random.randint(0, 256) for _ in range(3)]
            qp.setBrush(QColor(*color))
            qp.drawEllipse(*position, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())
