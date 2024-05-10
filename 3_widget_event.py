import sys
from PyQt5.QtWidgets import *
import py.btn_actions as action

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Quit", self)
        btn.move(20, 20)
        btn.clicked.connect(lambda :action.quit(self))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()