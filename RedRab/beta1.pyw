import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor, QLinearGradient
from PyQt5.QtCore import Qt, QSize
from random import randint

n_words = [
    'zzz... \u2764\uFE0F',
    'Hər şeyim mənim \u2764\uFE0F',
    'Səni hər şeydən çox sevirəm \u2764\uFE0F',
    'Səni hər şeydən çox sevirəm dovşanım \u2764\uFE0F',
    'Dovşanım mənim \u2764\uFE0F',
    'Varlığım mənim \u2764\uFE0F',
    'Ulduz Tozum \u2764\uFE0F',
    'Nərminim \u2764\uFE0F',
    'Dünyam mənim \u2764\uFE0F',
    'Can parçam mənim \u2764\uFE0F',
    'Mələyim mənim \u2764\uFE0F',
    'Pııt \u2764\uFE0F',
]

RanNum = randint(0, len(n_words) - 1)

class GradientWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
        gradient.setColorAt(0, QColor(123, 251, 240))  # pink
        gradient.setColorAt(1, QColor(109, 250, 81))  # white
        painter.fillRect(self.rect(), gradient)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Narminator Beta v3.0 Special For Narmin")
        self.setGeometry(100, 100, 1400, 800)
        self.setStyleSheet("background-color: transparent;")

        icon_heart = QIcon("C:/Program Files (x86)/Narminator Beta v2.0/icon.png")
        self.setWindowIcon(icon_heart)

        central_widget = GradientWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.label = QLabel()
        self.label.setText(n_words[RanNum])
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white;")
        self.label.setFont(QFont("Helvetica", 25))
        layout.addWidget(self.label)
        layout.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()