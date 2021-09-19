## 單繼承方法，能更好的進行介面與程式邏輯的分離

import sys

from PyQt5.QtWidgets import  QWidget, QApplication

from ui_FormHello import Ui_FormHello

class QmyWidget(QWidget):                    # 建立QmyWidget類別，只有一個基礎類別QWidget 
	def __init__(self, parent=None):
		super().__init__(parent)               # 呼叫父類別建構函數，建立QWidget視窗

		self.__ui = Ui_FormHello()             # 建立UI物件
		self.__ui.setupUi(self)                # 建構UI介面
		self.Lab = "單繼承的QmyWidget"          # 建立字串變數            
		self.__ui.LabHello.setText(self.Lab)   # 將剛建立的字串變數設定到UI介面的LabHello物件的文字屬性

	def setBtnText(self, aText):
		self.__ui.btnClose.setText(aText)
        
    
if __name__ == "__main__":
	app = QApplication(sys.argv)              # 建立App，用QApplication類別

	myWidget = QmyWidget()
	myWidget.show()
	myWidget.setBtnText("間接設定")
	sys.exit(app.exec_())
	