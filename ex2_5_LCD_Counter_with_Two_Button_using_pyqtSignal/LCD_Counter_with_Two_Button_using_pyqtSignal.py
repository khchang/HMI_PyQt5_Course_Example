# -*- coding: utf-8 -*-

"""
Module implementing LCD_Counter_with_Two_Button.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication

from Ui_LCD_Counter_with_Two_Button import Ui_Form
# 將 from .Ui_LCD_Counter_with_Two_Button import Ui_Form 的.去掉

import sys

class LCD_Counter_with_Two_Button(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    Count_Value_Changed = pyqtSignal(int)       # 定義Count_Value_Changed為傳遞整數的訊號

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
        # self.QLCD_Num_1.display(self.__count)
        self.Count_Value_Changed.emit(self.__count)

    @pyqtSlot()
    def on_QPB_2_clicked(self):             # 按下QPB_2時，會執行的副程式(slot)
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.__count = self.__count - 1
        # self.QLCD_Num_1.display(self.__count)
        self.Count_Value_Changed.emit(self.__count)

    def Set_QLCD_Num_1_Value(self, value):  # 設定QLCD_Num_1顯示數值的副程式
        self.QLCD_Num_1.display(value)

if __name__ == "__main__":                  # 程式進入點
    app = QApplication(sys.argv)
    Main_Window = LCD_Counter_with_Two_Button()
    Main_Window.Count_Value_Changed.connect(Main_Window.Set_QLCD_Num_1_Value)
    # 將Main_Window.Count_Value_Changed的signal連接到Main_Window.Set_QLCD_Num_1_Value的slot

    Main_Window.show()
    sys.exit(app.exec_())
    