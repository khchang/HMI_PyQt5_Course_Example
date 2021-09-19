# -*- coding: utf-8 -*-

"""
Module implementing LCD_Counter_with_Two_Button.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from .Ui_LCD_Counter_with_Two_Button import Ui_Form


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
    
    @pyqtSlot()
    def on_QPB_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_QPB_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
