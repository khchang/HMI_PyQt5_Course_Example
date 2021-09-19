# -*- coding: utf-8 -*-

"""
Module implementing LCD_Counter_with_Two_Button.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_LCD_Counter_with_Two_Button import Ui_Form
# 將 from .Ui_LCD_Counter_with_Two_Button import Ui_Form 的.去掉

import sys

class LCD_Counter_with_Two_Button(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(LCD_Counter_with_Two_Button, self).__init__(parent)
        self.setupUi(self)
        self.__count = 0                # 新增類別內的變數__count
    
    @pyqtSlot()
    def on_QPB_1_clicked(self):         # 按下QPB_1時，會執行的副程式(slot)
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.__count = self.__count + 1
        self.QLCD_Num_1.display(self.__count)

    @pyqtSlot()
    def on_QPB_2_clicked(self):         # 按下QPB_2時，會執行的副程式(slot)
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.__count = self.__count - 1
        self.QLCD_Num_1.display(self.__count)

if __name__ == "__main__":              # 程式進入點
    app = QApplication(sys.argv)
    Main_Window = LCD_Counter_with_Two_Button()
    Main_Window.show()
    sys.exit(app.exec_())
    