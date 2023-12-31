# Form implementation generated from reading ui file 'main_interface.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 615)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(930, 615))
        MainWindow.setMaximumSize(QtCore.QSize(930, 615))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Kclery_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"QMainWindow {\n"
"     background-image: url(:/Background/Untitled design.png);\n"
"    background-repeat: no-repeat; /* Optional: Prevent image from repeating */\n"
"    background-position: center; /* Optional: Center the image */\n"
"}\n"
"")
        MainWindow.setIconSize(QtCore.QSize(50, 30))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mic_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mic_button.setGeometry(QtCore.QRect(799, 476, 51, 51))
        self.mic_button.setStyleSheet("QPushButton {\n"
"    border-radius: 25px; \n"
"    background-color:rgb(170, 255, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Hover background color */\n"
"}")
        self.mic_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/mic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.mic_button.setIcon(icon1)
        self.mic_button.setIconSize(QtCore.QSize(50, 50))
        self.mic_button.setCheckable(False)
        self.mic_button.setFlat(False)
        self.mic_button.setObjectName("mic_button")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(90, 20, 711, 421))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px; /* Adjust the width of the scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: lightblue; /* Scrollbar handle color */\n"
"    border-radius: 5px;/* Rounded corners */\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #505050; /* Hovered color */\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #303030; /* Pressed color */\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    width: 0;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    background: transparent;\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 711, 421))
        self.scrollAreaWidgetContents.setStyleSheet("QWidget#scrollAreaWidgetContents {\n"
"    background-image: url(:/Background/Untitled design.png);\n"
"    /*background-repeat: no-repeat; /* Optional: Prevent image from repeating */\n"
"   background-position: center; /* Optional: Center the image */\n"
"}\n"
"")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 460, 701, 81))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    background-color: rgb(166, 166, 166);\n"
"   \n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"   border: 1px solid; \n"
"   border-radius:30px;\n"
"   background-color:rgb(147, 147, 147);\n"
"  \n"
"   margin: 5px; /* Sets the margin around the QTextEdit */\n"
"   padding: 5px; /* Sets the padding inside the QTextEdit */\n"
"\n"
"    \n"
"   \n"
"}\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px; /* Adjust the width of the scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: grey; /* Scrollbar handle color */\n"
"    border-radius: 5px;/* Rounded corners */\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #505050; /* Hovered color */\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #303030; /* Pressed color */\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    width: 0;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.enter_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(856, 476, 51, 51))
        self.enter_button.setStyleSheet("QPushButton {\n"
"    border-radius: 25px; \n"
"    background-color:rgb(170, 255, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Hover background color */\n"
"}")
        self.enter_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.enter_button.setIcon(icon2)
        self.enter_button.setIconSize(QtCore.QSize(55, 55))
        self.enter_button.setCheckable(False)
        self.enter_button.setFlat(False)
        self.enter_button.setObjectName("enter_button")
        self.music_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.music_button.setGeometry(QtCore.QRect(32, 476, 51, 51))
        self.music_button.setStyleSheet("QPushButton {\n"
"    border-radius: 25px; \n"
"    background-color:rgb(170, 255, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Hover background color */\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/music.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.music_button.setIcon(icon3)
        self.music_button.setIconSize(QtCore.QSize(50, 50))
        self.music_button.setObjectName("music_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KCLERY"))
        self.enter_button.setShortcut(_translate("MainWindow", "Ctrl+Return"))
import UI_elements_rc