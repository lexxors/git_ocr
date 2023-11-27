import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import random


class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        loadUi('design.ui', self)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Circle Drawer')
        layout = QVBoxLayout()
        self.pushButton.clicked.connect(self.add_circle)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def add_circle(self):
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        radius = random.randint(10, 50)
        color = QColor(Qt.yellow)

        self.circles.append(Circle(x, y, radius, color))
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setPen(circle.color)
            painter.drawEllipse(circle.x - circle.radius, circle.y - circle.radius,
                                2 * circle.radius, 2 * circle.radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())
