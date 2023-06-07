# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appwizard.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import buttonsGlassRound_rc

class Ui_dialogAppWizard(object):
    def setupUi(self, dialogAppWizard):
        if not dialogAppWizard.objectName():
            dialogAppWizard.setObjectName(u"dialogAppWizard")
        dialogAppWizard.setWindowModality(Qt.ApplicationModal)
        dialogAppWizard.resize(520, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogAppWizard.sizePolicy().hasHeightForWidth())
        dialogAppWizard.setSizePolicy(sizePolicy)
        dialogAppWizard.setMinimumSize(QSize(520, 500))
        dialogAppWizard.setMaximumSize(QSize(520, 500))
        icon = QIcon()
        icon.addFile(u"../resources/buttons/glassRound/glassButtonWizard.png", QSize(), QIcon.Normal, QIcon.Off)
        dialogAppWizard.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(dialogAppWizard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, -1)
        self.labelWizardPixmap = QLabel(dialogAppWizard)
        self.labelWizardPixmap.setObjectName(u"labelWizardPixmap")
        self.labelWizardPixmap.setMaximumSize(QSize(96, 96))
        self.labelWizardPixmap.setPixmap(QPixmap(u":/glassRound/glassButtonWizard.png"))
        self.labelWizardPixmap.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.labelWizardPixmap)

        self.labelApplicationsInfo = QLabel(dialogAppWizard)
        self.labelApplicationsInfo.setObjectName(u"labelApplicationsInfo")
        self.labelApplicationsInfo.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.labelApplicationsInfo)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBoxCurrent = QGroupBox(dialogAppWizard)
        self.groupBoxCurrent.setObjectName(u"groupBoxCurrent")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBoxCurrent)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayoutCurrent = QHBoxLayout()
        self.horizontalLayoutCurrent.setObjectName(u"horizontalLayoutCurrent")
        self.labelCurrentDate = QLabel(self.groupBoxCurrent)
        self.labelCurrentDate.setObjectName(u"labelCurrentDate")

        self.horizontalLayoutCurrent.addWidget(self.labelCurrentDate)

        self.labelCurrentVersion = QLabel(self.groupBoxCurrent)
        self.labelCurrentVersion.setObjectName(u"labelCurrentVersion")

        self.horizontalLayoutCurrent.addWidget(self.labelCurrentVersion)

        self.labelCurrentQuantity = QLabel(self.groupBoxCurrent)
        self.labelCurrentQuantity.setObjectName(u"labelCurrentQuantity")

        self.horizontalLayoutCurrent.addWidget(self.labelCurrentQuantity)


        self.horizontalLayout_6.addLayout(self.horizontalLayoutCurrent)


        self.horizontalLayout.addWidget(self.groupBoxCurrent)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.groupBoxCurrent1 = QGroupBox(dialogAppWizard)
        self.groupBoxCurrent1.setObjectName(u"groupBoxCurrent1")
        self.horizontalLayout_16 = QHBoxLayout(self.groupBoxCurrent1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayoutNew = QHBoxLayout()
        self.horizontalLayoutNew.setObjectName(u"horizontalLayoutNew")
        self.labelNewDate = QLabel(self.groupBoxCurrent1)
        self.labelNewDate.setObjectName(u"labelNewDate")

        self.horizontalLayoutNew.addWidget(self.labelNewDate)

        self.labelNewVersion = QLabel(self.groupBoxCurrent1)
        self.labelNewVersion.setObjectName(u"labelNewVersion")

        self.horizontalLayoutNew.addWidget(self.labelNewVersion)

        self.labelNewQuantity = QLabel(self.groupBoxCurrent1)
        self.labelNewQuantity.setObjectName(u"labelNewQuantity")

        self.horizontalLayoutNew.addWidget(self.labelNewQuantity)


        self.horizontalLayout_16.addLayout(self.horizontalLayoutNew)


        self.horizontalLayout_1.addWidget(self.groupBoxCurrent1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(dialogAppWizard)
        self.groupBox.setObjectName(u"groupBox")
        self.progressBarApplications = QProgressBar(self.groupBox)
        self.progressBarApplications.setObjectName(u"progressBarApplications")
        self.progressBarApplications.setGeometry(QRect(10, 20, 492, 25))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBarApplications.sizePolicy().hasHeightForWidth())
        self.progressBarApplications.setSizePolicy(sizePolicy1)
        self.progressBarApplications.setCursor(QCursor(Qt.WaitCursor))
        self.progressBarApplications.setValue(0)
        self.progressBarApplications.setInvertedAppearance(False)

        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButtonClose = QPushButton(dialogAppWizard)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        icon1 = QIcon()
        icon1.addFile(u":/glassRound/glassButtonClose.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonClose.setIcon(icon1)
        self.pushButtonClose.setIconSize(QSize(28, 28))
        self.pushButtonClose.setAutoDefault(False)

        self.horizontalLayout_5.addWidget(self.pushButtonClose)

        self.pushButtonStart = QPushButton(dialogAppWizard)
        self.pushButtonStart.setObjectName(u"pushButtonStart")
        icon2 = QIcon()
        icon2.addFile(u":/glassRound/glassButtonStart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonStart.setIcon(icon2)
        self.pushButtonStart.setIconSize(QSize(28, 28))
        self.pushButtonStart.setAutoDefault(False)

        self.horizontalLayout_5.addWidget(self.pushButtonStart)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBoxStatus = QGroupBox(dialogAppWizard)
        self.groupBoxStatus.setObjectName(u"groupBoxStatus")
        self.horizontalLayout_26 = QHBoxLayout(self.groupBoxStatus)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayoutStatus = QHBoxLayout()
        self.horizontalLayoutStatus.setObjectName(u"horizontalLayoutStatus")
        self.labelStatus = QLabel(self.groupBoxStatus)
        self.labelStatus.setObjectName(u"labelStatus")

        self.horizontalLayoutStatus.addWidget(self.labelStatus)


        self.horizontalLayout_26.addLayout(self.horizontalLayoutStatus)


        self.horizontalLayout_7.addWidget(self.groupBoxStatus)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)

        self.retranslateUi(dialogAppWizard)

        QMetaObject.connectSlotsByName(dialogAppWizard)
    # setupUi

    def retranslateUi(self, dialogAppWizard):
        dialogAppWizard.setWindowTitle(QCoreApplication.translate("dialogAppWizard", u"Applications Wizard", None))
        self.labelWizardPixmap.setText("")
        self.labelApplicationsInfo.setText(QCoreApplication.translate("dialogAppWizard", u"<html><head/><body><p>When you are ready, please press the <span style=\" font-weight:700;\">Start Button</span>, which will then open a dialog box to select the needed file. It will then check to ensure that it is the correct file and then automatically attempt to find the applications neccessary for Projectionist to run properly.</p></body></html>", None))
        self.groupBoxCurrent.setTitle(QCoreApplication.translate("dialogAppWizard", u"Current", None))
        self.labelCurrentDate.setText(QCoreApplication.translate("dialogAppWizard", u"Date: 26/05/2023", None))
        self.labelCurrentVersion.setText(QCoreApplication.translate("dialogAppWizard", u"Version: 0.0.0", None))
        self.labelCurrentQuantity.setText(QCoreApplication.translate("dialogAppWizard", u"Quantity: 0", None))
        self.groupBoxCurrent1.setTitle(QCoreApplication.translate("dialogAppWizard", u"New", None))
        self.labelNewDate.setText(QCoreApplication.translate("dialogAppWizard", u"Date: 26/05/2023", None))
        self.labelNewVersion.setText(QCoreApplication.translate("dialogAppWizard", u"Version: 0.0.0", None))
        self.labelNewQuantity.setText(QCoreApplication.translate("dialogAppWizard", u"Quantity: 0", None))
        self.groupBox.setTitle(QCoreApplication.translate("dialogAppWizard", u"Progress", None))
        self.pushButtonClose.setText(QCoreApplication.translate("dialogAppWizard", u"Close", None))
        self.pushButtonStart.setText(QCoreApplication.translate("dialogAppWizard", u"Start", None))
        self.groupBoxStatus.setTitle(QCoreApplication.translate("dialogAppWizard", u"Status", None))
        self.labelStatus.setText(QCoreApplication.translate("dialogAppWizard", u"Waiting...", None))
    # retranslateUi

