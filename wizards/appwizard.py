#!/usr/bin/env python3
# coding: utf-8


from PySide6.QtWidgets import (
    QDialog,
    QFileDialog
)

from PySide6.QtCore import (
    QFileInfo
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
                                                      "TOML Files (*.toml);; \
                                                      YAML Files (*.yml *.yaml);; \
                                                      JSON Files (*.jsn  *.json)")    
        print(str(fileName))
        print(f"Location {str(fileName[0])}")
        print(f"Option {str(fileName[1])}")
        fi = QFileInfo(str(fileName[0]))
        ext = fi.completeSuffix().lower()
        print(f"Extension {ext}")
        self.adapter = 0
        match ext:
            case "toml":
                self.adapter = 1
            case "yml":
                self.adapter = 2
            case "yaml":
                self.adapter = 2
            case "jsn":
                self.adapter = 3
            case "json":
                self.adapter = 3                
            case _:
                self.adapter = 0    
        print(f"Adapter {self.adapter}")
        