from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    # Initializes Window Geometry and Important Variables
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.setWindowTitle("File Processor")
        self.FilePath = ""
        self.resize(600, 400)
        self.setupUi()

    def setupUi(self):
        self.CentralWidget = QWidget(self)
        self.setCentralWidget(self.CentralWidget)

        self.CentralLayout = QVBoxLayout()
        self.CentralWidget.setLayout(self.CentralLayout)

        self.FilePickerButton = QPushButton("&Choose file", self)
        self.FilePickerButton.clicked.connect(self.FilePicker)
        self.FilePickerButton.move(10, 10)

        self.RefreshFileButton = QPushButton("&Refresh File", self)
        self.RefreshFileButton.clicked.connect(self.RefreshFile)
        self.RefreshFileButton.move(120, 10)

        # Buttons Arranged Horizontally
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.addWidget(self.FilePickerButton)
        self.ButtonLayout.addWidget(self.RefreshFileButton)

        self.FileTextViewBox = QTextEdit()
        self.FileTextViewBox.setReadOnly(True)

        # Main Vertical Layout
        self.CentralLayout.addLayout(self.ButtonLayout)
        self.CentralLayout.addWidget(self.FileTextViewBox)

    # Refreshes Currently open file for any outside changes made to it
    def RefreshFile(self):
        with open(self.FilePath[0], "r") as File:
            text = File.read()
            self.FileTextViewBox.setText(text)

    # Choose File to perform Operations on
    def FilePicker(self):
        OldFilePath = self.FilePath
        self.FilePath = QFileDialog.getOpenFileName(self, "Open File")

        # Reverts Changes if No file is Selected or Operation is Cancelled
        if self.FilePath[0] == "":
            self.FilePath = OldFilePath
            return

        # Updates FileTextViewBox with new text
        with open(self.FilePath[0], "r") as File:
            text = File.read()
            self.FileTextViewBox.setText(text)
