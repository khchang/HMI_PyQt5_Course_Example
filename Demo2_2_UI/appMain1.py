## appMain1.py
## 使用 ui_FormHello.py檔案中的類別Ui_FormHello建立App

import sys
from PyQt5 import QtWidgets
import ui_FormHello                     # 匯入剛剛由pyuic5轉出的ui_FormHello類別

app = QtWidgets.QApplication(sys.argv) 

baseWidget = QtWidgets.QWidget()        # 建立視窗的基礎類別QWidget的案例

ui = ui_FormHello.Ui_FormHello()        # 建立UI視窗的案例
ui.setupUi(baseWidget)                  # 以baseWidget作為傳遞參數

baseWidget.show()                       # 顯示表單
# ui.LabHello.setText("Hello,被程式修改")  # 可以修改LabHello上文字

sys.exit(app.exec_()) 
