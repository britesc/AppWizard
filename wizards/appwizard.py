#!/usr/bin/env python3
# coding: utf-8


# TODO Move all .qrc files to resources folder adjusting as necessary

import subprocess
import atexit
import logging

import time
import datetime

from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QApplication
)


from PySide6.QtCore import (
    QFileInfo,
    QDate
)

from PySide6.QtGui import (
    QPixmap
)

from sqlitedict import (
    SqliteDict
)

from classes import (
    j2_settings
)

from wizards.appwizard_ui import (
    Ui_dialogAppWizard
)

import readfiles_rc  # type: ignore


class AppWizard(QDialog, Ui_dialogAppWizard):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # type: ignore

        self.setWindowTitle("Applications Wizard")
        self.pushButtonClose.setEnabled(True)
        self.pushButtonStart.setEnabled(True)

        self.pushButtonClose.clicked.connect(self.closeApp)  # type: ignore
        self.pushButtonStart.clicked.connect(self.startApp)  # type: ignore
 
        self.key1 = 'applications'
        self.key2 = 'apps'
        self.fileName = ()       
        
        """ 
            Setup The Logging Process
        """
        self.setupLogging()

        """ 
            Setup The SqliteDict Process
        """
        self.setupDatabase()

        """ 
            Setup The Initial Wizard Display
        """
        self.setupWizardDisplay(False)

        self.setModal(True)
        self.exec()

    def closeApp(self) -> None:
        self.labelStatus.setText("Waiting...")
        self.reject()

    def startApp(self) -> None:
        self.progressBarApplications.setMinimum(0)
        self.labelStatus.setText("Processing...")
        logging.debug('Processing...')

        adapterList = [
            self.adapterNone,
            self.adapterToml,
            self.adapterYaml,
            self.adapterJson
        ]
        # pz  = QFileDialog.getOpenFileName(
        self.fileName = QFileDialog.getOpenFileName(     # type: ignore
            self,
            "Open File",
            "/home",
            "TOML Files (*.toml);; \
            YAML Files (*.yml *.yaml);; \
            JSON Files (*.jsn  *.json)"
            )  # noqa: E999

        self.filename = QFileInfo(str(self.fileName[0]))  # type: ignore
        self.filebase = self.filename.fileName()
        self.extension = self.filename.completeSuffix().lower()

        self.labelStatus.setText(str(self.filebase))

        QApplication.processEvents()
        adapter = 0
        match self.extension:
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
                adapter = 0

        adapterList[adapter]()  # type: ignore
        if not self.ActivityResult:
            return
        self.checkLoadedConfig()
        if not self.ActivityResult:
            return
        self.parseConfig()

    def adapterNone(self) -> None:
        logging.debug('AdapterNone Called')

    def adapterToml(self) -> bool:
        import tomli

        # Set status to Using TOML Adapter
        logging.debug('AdapterToml Called')
        self.ActivityResult = False

        try:
            with open(self.fileName[0], mode="rb") as self.fp:  # type: ignore
                self.loadedConfig = tomli.load(self.fp)
            # self.fp.close()
            self.labelFileType.setPixmap(
                QPixmap(u":/resources/Images/png/toml.png"))
            self.labelFileType.setScaledContents(True)

            QApplication.processEvents()
            self.ActivityResult = True

        except Exception as err:
            logging.debug(f'adapterToml Failed: Exception: {str(err)}')
            logging.error("Exception occurred", exc_info=True)
            self.ActivityResult = False

        finally:
            logging.debug(f"adapterToml = {self.ActivityResult}")
            self.fp.close()
#            time.sleep(1)
            return self.ActivityResult
            # We now have the TOML File Loaded

    def adapterYaml(self) -> None:
        logging.debug("AdapterYaml Called")

    def adapterJson(self) -> None:
        logging.debug("AdapterJson Called")

    def checkLoadedConfig(self) -> bool:  # type: ignore
        # sourcery skip: class-extract-method
        # We need to check it is our file not some other file
        # First we check the length of the dictionary
        # If it is 2 OK else INVALID
        logging.debug("checkLoadedConfig Called")
        self.ActivityResult = False
        try:
            if len(self.loadedConfig) != 2:  # type: ignore
                # logging.info status message File Invalid and wait for reselection or close option
                self.labelStatus.setText("Incorrect File Format")
                logging.warning('Incorrect File Format')
                self.t1 = []
                self.t2 = []
                self.loadedConfig.clear()
                logging.debug("Length |= 2 so stop")
                self.AdapterErrorCode = 4001
                self.ActivityResult = False
            else:
                self.t1 = self.loadedConfig[self.key1]
                self.t2 = self.loadedConfig[self.key2]
                self.ActivityResult = True

        except Exception as err:
            logging.error(f'checkLoadedConfig: Exception: {str(err)}')
            logging.error("Exception occurred", exc_info=True)
            self.ActivityResult = False

        finally:
            QApplication.processEvents()
            logging.debug(f"checkLoadedConfig 1 = {self.ActivityResult}")
#            time.sleep(1)
            if not self.ActivityResult:
                return self.ActivityResult

        try:
            if len(self.loadedConfig[self.key1]) != 1:
                self.loadedConfig.clear()
                self.labelStatus.setText("Incorrect Header Format")
                self.AdapterErrorCode = 4002
                self.ActivityResult = False

        except Exception as err:
            logging.error(f'checkLoadedConfig: Exception: {str(err)}')
            logging.error("Exception occurred", exc_info=True)
            self.ActivityResult = False

        finally:
            QApplication.processEvents()
            logging.debug(f"checkLoadedConfig 2 = {self.ActivityResult}")
#            time.sleep(1)
            if not self.ActivityResult:
                return self.ActivityResult

        try:
            if (self.loadedConfig[self.key1][0]['application'] != 'Projectionist'):
                logging.warning("Wrong File")
                self.loadedConfig.clear()
                self.labelStatus.setText("Wrong File Selected")
                self.AdapterErrorCode = 4003
                self.ActivityResult = False

            else:
                self.NewDate = QDate.fromJulianDay(self.loadedConfig[self.key1][0]['date']).toString()  # noqa: E501
                self.NewJulianDate = (self.loadedConfig[self.key1][0]['date'])
                self.labelNewDate.setText(f"Date: {self.NewDate}")
                self.NewVersion = self.loadedConfig[self.key1][0]['version']
                self.labelNewVersion.setText(f"Version: {self.NewVersion}")
                self.NewQuantity = len(self.loadedConfig[self.key2])
                self.labelNewQuantity.setText(f"Quantity: {self.NewQuantity}")
                self.progressBarApplications.setMinimum(0)
                self.progressBarCounter = 0
                self.progressBarApplications.setMaximum(self.NewQuantity)
                self.ActivityResult = True

        except Exception as err:
            logging.error(f'checkLoadedConfig: Exception: {str(err)}')
            logging.error("Exception occurred", exc_info=True)
            self.ActivityResult = False

        finally:
            QApplication.processEvents()
            logging.debug(f"checkLoadedConfig 3 = {self.ActivityResult}")
#            time.sleep(1)
            return self.ActivityResult

    def parseConfig(self) -> bool:
        logging.debug("parseConfig Called")
        self.progressBarApplications.setMinimum(0)
        self.progressBarCounter = 0
        self.progressBarApplications.setMaximum(
            self.NewQuantity)  # type: ignore

        self.ActivityResult = False
        self.pushButtonClose.setEnabled(False)
        self.pushButtonStart.setEnabled(False)

        try:
            logging.debug("Trying Dict Item")
            for dict_item in self.loadedConfig[self.key2]:
                vAppAlias = dict_item['AppAlias']  # type: ignore
                vAppReal = dict_item['AppReal']
                vAppVerGet = dict_item['AppVerGet']
                vRegexStart = dict_item['RegexStart']
                vRegexEnd = dict_item['RegexEnd']
                vType = dict_item['Type']

                request = f"which {vAppReal}"
                process = subprocess.run(
                    request,
                    shell=True,
                    check=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True,
                    timeout=10
                )

                vLocation = process.stdout
                vLocation = vLocation.rstrip('\n')
                self.labelStatus.setText(f"Processing... {vLocation}")
                logging.info(f"Processing... {vLocation}")
                QApplication.processEvents()

                process.stdout = ""
                process.stderr = ""

                vRequest = f"{vLocation} {vAppVerGet}"
                process = subprocess.run(
                    vRequest,
                    shell=True,
                    check=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True,
                    timeout=10
                )
# sourcery skip: extract-duplicate-method, extract-method, use-or-for-fallback
                responseVersion = process.stdout
                if not responseVersion:
                    responseVersion = process.stderr
                responseVersion = responseVersion.rstrip('\n')
                vVersion = responseVersion[vRegexStart:vRegexEnd]

                self.database[f"{vAppReal}"] = {
                    'app': vAppReal,
                    'alias': vAppAlias,
                    'location': vLocation,
                    'version': vVersion,
                    'type': vType
                }
                self.database.commit()  # type: ignore

                self.databaseSize = str(len(self.database))

                # print("")
                # for key, item in self.database.items():
                #     print("%s=%s" % (key, item))

                self.progressBarCounter += 1
                self.progressBarApplications.setValue(self.progressBarCounter)
                QApplication.processEvents()
                process.stdout = ""
                process.stderr = ""
                self.ActivityResult = True

        except subprocess.CalledProcessError as err:
            vRequest = f"killall {vAppReal}"  # type: ignore
            logging.error(f"parseConfig: Exception: {vRequest}")
            logging.error(f'parseConfig: Exception: {str(err)}')
            logging.error(f'parseConfig: Exception: {str(err.returncode)} - {err.returncode}')            
            logging.error("Exception occurred", exc_info=True)

            process = subprocess.run(
                vRequest,
                shell=True,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                timeout=10
            )
            subprocess.CalledProcessError.discard()  # type: ignore

        except Exception as err:
            logging.error(f'parseConfig: Exception: {str(err)}')
            logging.error("Exception occurred", exc_info=True)
            vRequest = f"killall {vAppReal}"  # type: ignore
            logging.debug(f"{vRequest}")
            err.discard()            # type: ignore

            process = subprocess.run(
                vRequest,
                shell=True,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                timeout=10
            )
            self.ActivityResult = True

        finally:
            QApplication.processEvents()
            logging.debug(f"parseConfig = {self.ActivityResult}")

            self.setupWizardDisplay(True)

            return self.ActivityResult

    def setupLogging(self) -> None:
        self.debugstatus = logging.NOTSET
        self.logdate = datetime.date.today()
        self.logfilename = f"appwizard.{self.logdate}.log"
        self.logging = logging.basicConfig(
            filename=self.logfilename,
            encoding='utf-8',
            level=self.debugstatus,
            format='%(asctime)s %(name)s %(levelname)s: %(module)s %(funcName)s: %(lineno)s %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S'
        )

        self.j2_settings = j2_settings.J2_Settings()
        self.debugstatus = self.j2_settings.getDebugStatus()
        logging.getLogger().setLevel(self.debugstatus)
        logging.debug("Logging Enabled")
        logging.debug(f"Logging Status: {self.debugstatus}")
        
    def setupDatabase(self) -> None:
        self.databaseName = 'projectionist.db'
        self.AdapterErrorCode = 0
        self.tablename = "Apps"
        self.database = SqliteDict(
            self.databaseName,
            tablename=self.tablename,
            autocommit=True
        )
        self.databaseRecords = len(self.databaseName)
        logging.debug(f"SqliteDict Database Enabled - {self.debugstatus}")

    def setupWizardDisplay(self, displaystatus: bool) -> None:
        self.displaystatus = displaystatus
        self.progressBarApplications.setMinimum(0)
        self.progressBarCounter = 0
        self.labelStatus.setText("Waiting...")

        # Date        
        try:
            self.currentDate = f"Date: {self.j2_settings.getHeaderDate()}"
            self.labelCurrentDate.setText(self.currentDate)
            if self.displaystatus:
                self.j2_settings.setHeaderDate(self.NewJulianDate)
                self.currentDate = self.NewDate
                self.labelCurrentDate.setText(f"Date: {self.currentDate}")
                self.NewDate = ""
                self.labelNewDate.setText("Date: None")        
        except Exception as err:
            logging.error(f'Exception: {str(err)}')
            logging.error("Exception:", exc_info=True)            
            err.discard()            # type: ignore
        finally:            
            QApplication.processEvents()


        # Version
        try:
            self.currentVersion = f"Version: {self.j2_settings.getHeaderVersion()}"
            self.labelCurrentVersion.setText(self.currentVersion)
            if self.displaystatus:
                self.j2_settings.setHeaderVersion(self.NewVersion)
                self.currentVersion = self.NewVersion
                self.labelCurrentVersion.setText(f"Version: {self.currentVersion}")
                self.NewVersion = ""
                self.labelNewVersion.setText("Version: 0.0.0")                    
        except Exception as err:
            logging.error(f'Exception: {str(err)}')
            logging.error("Exception:", exc_info=True)            
            err.discard()            # type: ignore
        finally:            
            QApplication.processEvents()



        # Quantity
        try:
            self.database.commit()  # type: ignore 
            QApplication.processEvents()  
            time.sleep(2)             
            self.databaseSize = str(len(self.database))
            self.currentQuantity = f"Quantity: {self.databaseSize}"
            self.labelCurrentQuantity.setText(self.currentQuantity)
        except Exception as err:
            logging.error(f'Exception: {str(err)}')
            logging.error("Exception:", exc_info=True)
        finally:            
            if self.displaystatus:
                self.NewQuantity = ""
                self.labelNewQuantity.setText("Quantity: 0")            
            QApplication.processEvents()

        # Other
        self.labelFileType.setPixmap(
            QPixmap(u":/resources/Images/png/blank.png"))
        self.labelFileType.setScaledContents(True)
        if self.displaystatus:
            self.labelStatus.setText("Completed")
            self.progressBarApplications.setValue(0)
            self.pushButtonClose.setEnabled(True)            
            logging.debug("Re-initialised Display Enabled")
        else:        
            logging.debug("Initial Display Enabled")

        QApplication.processEvents()



















    """

        logging.info.(self.loadedConfig)  

        logging.info("Debug Point 1 - len(self.loadedConfig)")
        logging.info(len(self.loadedConfig),end='\n\n')


        logging.info("Debug Point 2 - self.loadedConfig['applications']")
        logging.info(self.loadedConfig['applications'],end='\n\n') 


        logging.info("Debug Point 3 - t1 = self.loadedConfig['applications']")
        t1 = self.loadedConfig['applications']
        logging.info(len(t1))
        plogging.info.plogging.info(t1)
        logging.info("")


        logging.info("Debug Point 4 - x = self.loadedConfig.keys()")
        x = self.loadedConfig.keys()
        logging.info(x,end='\n\n')    


        logging.info("Debug Point 5 - key1 = list(self.loadedConfig.keys())[0]")
        key1 = self._extracted_from_adapterToml_58(
            0, "Debug Point 6 - key2 = list(self.loadedConfig.keys())[1]"
        )
        key2 = self._extracted_from_adapterToml_58(
            1, "Debug Point 2b - self.loadedConfig[key1]"
        )
        logging.info(self.loadedConfig[key1],end='\n\n')  


        logging.info("Debug Point 3b - t2 = len(self.loadedConfig[key1]")
        t2 = len(self.loadedConfig[key1])
        logging.info(t2,end='\n\n')          

        logging.info("Debug Point 7 - td1 = self.loadedConfig[key1]")
        td1 = self.loadedConfig[key1]
        plogging.info.plogging.info(td1)
        logging.info("")

        logging.info("Debug Point 8 - t3 = len(td1)")
        t3 = len(td1)
        logging.info(t3,end='\n\n')

        self._extracted_from_adapterToml_84(
            "Debug Point 9 - td1[0]['date']", td1, 'date', 'version'
        )
        logging.info("")

        logging.info("Debug Point 3c - t2 = len(self.loadedConfig[key2]")
        t2 = len(self.loadedConfig[key2])
        logging.info(t2,end='\n\n')           

        logging.info("Debug Point 7a - td1 = self.loadedConfig[key2]")
        td1 = self.loadedConfig[key2]
        plogging.info.plogging.info(td1)
        logging.info("")

        logging.info("Debug Point 8a - t3 = len(td1)")
        logging.info(len(td1), end='\n\n')   

        self._extracted_from_adapterToml_84(
            "Debug Point 9a - td1[0]['AppAlias']", td1, 'AppAlias', 'AppReal'
        )
        logging.info(td1[0]['AppVerGet'])
        logging.info(td1[0]['RegexEnd'])
        logging.info(td1[0]['RegexStart'])
        logging.info(td1[0]['Type'])
        logging.info("")             

    # TODO Rename this here and in `adapterToml`
    def _extracted_from_adapterToml_84(self, arg0, td1, arg2, arg3):
        logging.info(arg0)
        logging.info(td1[0][arg2])
        logging.info(td1[0][arg3])             

    # TODO Rename this here and in `adapterToml`
    def _extracted_from_adapterToml_58(self, arg0, arg1):
        self.ActivityResult = list(self.loadedConfig.keys())[arg0]
        logging.info(self.ActivityResult, end='\n\n')


        logging.info(arg1)
        return self.ActivityResult             
        
        # key3 = self.loadedConfig.keys()
        
        # logging.info(key3)
        # for key in self.loadedConfig.keys():
        #     logging.info(key, '->', self.loadedConfig[key])

    """
