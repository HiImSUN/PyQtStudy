
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

main_ui = uic.loadUiType(resource_path("./MainWindow.ui"))[0] # main ui 불러오고
widget_btns_ui = uic.loadUiType(resource_path("./widget_btns.ui"))[0] # widget ui 불러와서
widget_count_ui = uic.loadUiType(resource_path("./widget_count.ui"))[0] # widget ui 불러와서
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# main_ui = uic.loadUiType("main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainWindowClass(QMainWindow, main_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #self.button_process.clicked.connect(lambda :print_hello(self))
        self.upper_count_widget = widgetCountClass()
        self.lower_count_widget = widgetCountClass()
        self.btns_widget = widgetBtnsClass()
        # self.centralwidget.addWidget(self.new_widget)
        #####self.layout1 = 

class widgetCountClass(QWidget, widget_count_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

class widgetBtnsClass(QWidget, widget_btns_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    #WindowClass의 인스턴스 생성
    myWindow = MainWindowClass() 
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()