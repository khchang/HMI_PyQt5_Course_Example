## demo2_1Hello.py
## 使用PyQt5，純程式碼建立一個簡單的GUI程式

import sys

from PyQt5 import QtCore, QtGui, QtWidgets  # 匯入PyQt5套件中的幾個模組

app = QtWidgets.QApplication(sys.argv)      # 建立App，用QApplication類別

widgetHello = QtWidgets.QWidget()           # 建立一個窗體widgetHello，用QWidget類別
widgetHello.resize(280,150)                 # 設定交談視窗的寬度和高度
widgetHello.setWindowTitle("Demo2_1")       # 設定交談視窗的標題文字

LabHello = QtWidgets.QLabel(widgetHello)    # 建立一個標簽LabHello，父容器為widgetHello
LabHello.setText("Hello World, PyQt5")      # 設定標籤文字

font = QtGui.QFont()                        # 建立字型物件font，用QFont類別
font.setFamily("微軟正黑體")                 # 設定字型
# font.setFamily("Arial")                     # 設定字型
font.setPointSize(14)                       # 設定字型大小
font.setBold(True)                          # 設定為粗體
LabHello.setFont(font)                      # 將設定為標簽LabHello的字型

size = LabHello.sizeHint()                  # 取得LabHello的合適大小，傳回值aLabSize是QSize類別物件

LabHello.setGeometry(50, 60, size.width(), size.height())
##設定LabHello的位置和大小，位置x=50,y=60， 寬度和高度由aLabSize的值確定

widgetHello.show()                          # 顯示交談視窗

sys.exit(app.exec_())                       # 套用程式執行
