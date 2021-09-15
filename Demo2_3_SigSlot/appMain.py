##  GUI套用程式主程式

import sys

from PyQt5.QtWidgets import  QApplication

from myDialog import QmyDialog
    
app = QApplication(sys.argv)     #建立GUI套用程式

mainform=QmyDialog()             #建立主窗體

mainform.show()                  #顯示主窗體

sys.exit(app.exec_()) 
