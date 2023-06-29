#!/usr/bin/env python3
# coding: utf-8


import os
import sys
import traceback
import logging


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)    

from wizards import appwizard


def SetupApp() -> None:
    global vApplicationName
    vApplicationName = os.path.splitext(os.path.basename(__file__))[0]
    basedir = os.path.dirname(__file__)
    # print("Current working folder: ", os.getcwd())
    # print("Paths are relative to: ", basedir)
    # print("Application Name: ", vApplicationName)


def Main() -> None:
    global vApplicationName
    try:
        app = QApplication(sys.argv)
        
        window = MainWindow()
        
        window.show()
        
    
    except Exception as err:
#         print(f"Unfortunately {vApplicationName} has encountered an error \
# and is unable to continue.")
#         print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception() # type: ignore

    finally:
        sys.exit(app.exec())


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Dialog 1")
        
        self.button = QPushButton("Call Next Dialog")
        
        self.setCentralWidget(self.button)
        
        self.button.clicked.connect(self.button_was_clicked) # type: ignore
        
        self.setFixedSize(300, 200)
        

        
    def button_was_clicked(self) -> None:
        # print("Button was Clicked")
        self.AppWizard = appwizard.AppWizard()
        

if __name__ == '__main__':

    vApplicationName = ""
    SetupApp()
    Main()   