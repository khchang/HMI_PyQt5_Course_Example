## appMain1.py
## 使用 ui_FormHello.py檔案中的類別Ui_FormHello建立App

import sys

from PyQt5 import QtWidgets

import ui_FormHello

app = QtWidgets.QApplication(sys.argv) 

baseWidget=QtWidgets.QWidget()      #建立視窗的基礎類別QWidget的案例

ui =ui_FormHello.Ui_FormHello()     #建立UI視窗的案例
ui.setupUi(baseWidget)              #以baseWidget作為傳遞參數

baseWidget.show()
##ui.LabHello.setText("Hello,被程式修改")    #可以修改窗體上標簽的文字

sys.exit(app.exec_()) 
