##與UI窗體類別對應的業務邏輯類別

import sys

from PyQt5.QtWidgets import  QApplication, QDialog

from PyQt5.QtGui import  QPalette

from PyQt5.QtCore import Qt, pyqtSlot

from ui_Dialog import Ui_Dialog

class QmyDialog(QDialog): 
   def __init__(self, parent=None):
      super().__init__(parent)   #呼叫父類別建構函數，建立窗體
      self.ui=Ui_Dialog()        #建立UI物件
      self.ui.setupUi(self)      #建構UI界面

      self.ui.radioBlack.clicked.connect(self.do_setTextColor)
      self.ui.radioRed.clicked.connect(self.do_setTextColor)
      self.ui.radioBlue.clicked.connect(self.do_setTextColor)

## 由connectSlotsByName() 自動與元件的訊號連線的槽函數
##    @pyqtSlot()
   def on_btnClear_clicked(self):  #"清理"按鈕
      self.ui.textEdit.clear()

##    @pyqtSlot()
   def on_chkBoxBold_toggled(self,checked):  #"Bold"復選框
      font=self.ui.textEdit.font()
      font.setBold(checked)         #函數參數checked表示了選取狀態
      self.ui.textEdit.setFont(font)

##    @pyqtSlot()
   def on_chkBoxUnder_clicked(self):   #"Underline"復選框
      checked=self.ui.chkBoxUnder.isChecked()   #讀取選取狀態
      font=self.ui.textEdit.font()
      font.setUnderline(checked)
      self.ui.textEdit.setFont(font)

   @pyqtSlot(bool)     #修飾符號指定參數型態，用於overload型的訊號
   def on_chkBoxItalic_clicked(self,checked):   #"Italic"復選框
      font=self.ui.textEdit.font()
      font.setItalic(checked)
      self.ui.textEdit.setFont(font)
        

## 自訂槽函數
   def do_setTextColor(self):
      plet=self.ui.textEdit.palette()     #取得 palette

      if (self.ui.radioBlack.isChecked()):    
         plet.setColor(QPalette.Text, Qt.black)  #black
      elif (self.ui.radioRed.isChecked()):
         plet.setColor(QPalette.Text, Qt.red)    #red
      elif (self.ui.radioBlue.isChecked()):
         plet.setColor(QPalette.Text, Qt.blue)   #blue

      self.ui.textEdit.setPalette(plet)   #設定palette
   
if  __name__ == "__main__":         #用於目前窗體測試
   app = QApplication(sys.argv)     #建立GUI套用程式

   form=QmyDialog()                 #建立窗體

   form.show()

   sys.exit(app.exec_()) 
