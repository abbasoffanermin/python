import sys
from PyQt5.QtWidgets import QApplication, QLabel

def main():
    app = QApplication(sys.argv)

    label = QLabel("Hello, PyQt5!")
    label.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
