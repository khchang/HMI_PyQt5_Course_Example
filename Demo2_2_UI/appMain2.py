﻿## 多重繼承，界面元件物件容易與新類別定義的變數混淆

import sys

from PyQt5.QtWidgets import  QWidget, QApplication

from ui_FormHello import Ui_FormHello

class QmyWidget(QWidget,Ui_FormHello): 
   def __init__(self, parent=None):
      super().__init__(parent)   #呼叫父類別建構函數，建立QWidget視窗

      self.Lab="多重繼承的QmyWidget"     #新定義的一個變數
      self.setupUi(self)               #self就是QWidget窗體，可以作為參數傳給setupUi()
      self.LabHello.setText(self.Lab)  #窗體上的LabHello
    
if  __name__ == "__main__":
   app = QApplication(sys.argv)        #建立App
   myWidget=QmyWidget()
   myWidget.show()
   myWidget.btnClose.setText("不關閉了")
   sys.exit(app.exec_()) 
