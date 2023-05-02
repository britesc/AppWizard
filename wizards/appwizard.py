#!/usr/bin/env python3
# coding: utf-8


from PySide6.QtWidgets import (
    QDialog,
    QFileDialog
)

from wizards.appwizard_ui import Ui_dialogAppWizard

class AppWizard(QDialog, Ui_dialogAppWizard):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self) # type: ignore
        
        self.setWindowTitle("Applications Wizard")
        
        self.pushButtonClose.clicked.connect(self.closeApp) # type: ignore
        self.pushButtonStart.clicked.connect(self.startApp) # type: ignore
        
        self.exec()

    def closeApp(self) -> None:
        self.reject()
        
    def startApp(self) -> None:
        print("In startApp")
        fileName = QFileDialog.getOpenFileName(self, "Open File",
                                                      "/home",
                                                      "YAML Files (*.yml *.yaml);; \
                                                      TOML Files (*.toml);; \
                                                      JSON Files (*.jsn  *.json)")    
        print(str(fileName))
        print(f"Location {str(fileName[0])}")
        print(f"Extension {str(fileName[1])}")
     