import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from PyQt5.QtCore import QCoreApplication

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyQt5 Pencere Ornegi')
        self.setGeometry(100, 100, 400, 300)

        btn_quit = QPushButton('Kapat', self)
        btn_quit.clicked.connect(QCoreApplication.instance().quit)
        btn_quit.setGeometry(150, 150, 100, 50)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
