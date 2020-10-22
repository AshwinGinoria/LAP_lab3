from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.setWindowTitle("SG Transport")
        self.resize(800, 800)
        self.setupUi()

    def setupUi(self):
        self.filePickerButton = QPushButton("Choose file", self)
        self.filePickerButton.clicked.connect(self.filePicker)
        self.filePickerButton.setObjectName("filePickerButton")
        self.filePickerButton.move(10, 10)
        
        self.refreshFileButton = QPushButton("Refresh File", self)
        self.refreshFileButton.clicked.connect(self.refreshFile)
        self.refreshFileButton.setObjectName("refreshFileButton")
        self.refreshFileButton.move(120, 10)

        self.wid = QWidget(self)

        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.layout.addWidget(self.filePickerButton, 0, 0, 1, 1)
        self.layout.addWidget(self.refreshFileButton, 0, 1, 1, 1)
        self.wid.setLayout(self.layout)

    def refreshFile(self):
        file = open(self.filePath[0], "r")
        self.layout.removeWidget(self.textEdit)
        self.displayText()
        with file:
            text = file.read()
            self.textEdit.setText(text)

    def filePicker(self):
        self.filePath = QFileDialog.getOpenFileName(self, "Open File")
        file = open(self.filePath[0], "r")
        self.displayText()
        with file:
            text = file.read()
            self.textEdit.setText(text)

    def displayText(self):
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.layout.addWidget(self.textEdit, 1, 0, 2, 5)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())