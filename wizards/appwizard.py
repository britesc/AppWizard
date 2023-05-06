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
        adapterList = [
            self.adapterNone,
            self.adapterToml,
            self.adapterYaml,
            self.adapterJson
        ]        
        
        fileName = QFileDialog.getOpenFileName(self, "Open File",
                                                      "/home",
                                                      "TOML Files (*.toml);; \
                                                      YAML Files (*.yml *.yaml);; \
                                                      JSON Files (*.jsn  *.json)")
        
        print(str(fileName)) # type: ignore
        print(f"Location {str(fileName[0])}") # type: ignore
        print(f"Option {str(fileName[1])}") # type: ignore
        fi = QFileInfo(str(fileName[0])) # type: ignore
        ext = fi.completeSuffix().lower()
        print(f"Extension {ext}")
        
        adapter = 0
        match ext:
            case "toml":
                adapter = 1
            case "yml":
                adapter = 2
            case "yaml":
                adapter = 2
            case "jsn":
                adapter = 3
            case "json":
                adapter = 3                
            case _:
                adapter= 0
                    
        print(f"Adapter {adapter}")
        
        print(f"Calling Adapter {adapterList[adapter]}") # type: ignore
        
        adapterList[adapter]() # type: ignore
        
        
        
    def adapterNone(self) -> None:
        print("AdapterNone Called")
    
    def adapterToml(self) -> None:
        print("AdapterToml Called")
    
    def adapterYaml(self) -> None:
        print("AdapterYaml Called")
    
    def adapterJson(self) -> None:
        print("AdapterJson Called")       
        