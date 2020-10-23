from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from helpers import CountWords, PlotWordHistogram
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt


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

        # File Selection Buttons
        self.FilePickerButton = QPushButton("&Choose file", self)
        self.FilePickerButton.clicked.connect(self.FilePicker)

        self.RefreshFileButton = QPushButton("&Refresh File", self)
        self.RefreshFileButton.clicked.connect(self.RefreshFile)

        # Buttons Arranged Horizontally
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.addWidget(self.FilePickerButton)
        self.ButtonLayout.addWidget(self.RefreshFileButton)

        # File Content Display
        self.FileTextViewBox = QTextEdit()
        self.FileTextViewBox.setReadOnly(True)

        # Extra Feature Buttons
        self.DisplayDetailsButton = QPushButton("&Show Text Details")
        self.DisplayDetailsButton.clicked.connect(self.DisplayTextDetails)
        
        self.PlotWordHistogramButton = QPushButton("&Display Word Frequencies")
        self.PlotWordHistogramButton.clicked.connect(self.DisplayWordHistogram)

        self.KeywordCheckButton = QPushButton("Check &Keywords")
        # self.KeywordCheckButton.clicked.connect(self.CheckKeywords)

        self.CreateWordCloudButton = QPushButton("Create &WordCloud")
        self.CreateWordCloudButton.clicked.connect(self.CreateWordCloud)

        # Extra Buttons Arranged in a grid
        self.FeatureButtonsLayout = QGridLayout()
        self.FeatureButtonsLayout.addWidget(self.DisplayDetailsButton, 0, 0, 1, 1)
        self.FeatureButtonsLayout.addWidget(self.PlotWordHistogramButton, 0, 1, 1, 1)
        self.FeatureButtonsLayout.addWidget(self.KeywordCheckButton, 1, 0, 1, 1)
        self.FeatureButtonsLayout.addWidget(self.CreateWordCloudButton, 1, 1, 1, 1)

        # Main Vertical Layout
        self.CentralLayout.addLayout(self.ButtonLayout)
        self.CentralLayout.addWidget(self.FileTextViewBox)
        self.CentralLayout.addLayout(self.FeatureButtonsLayout)

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

    def DisplayTextDetails(self):
        counts = CountWords(self.FileTextViewBox.toPlainText())

        Details = {
            'Total Words' : sum([len(sentence.split(' ')) for sentence in self.FileTextViewBox.toPlainText().strip().split('\n')]),
            'Total Words Under Consideration' : sum(counts.values()),
            'Total Different Words' : len(list(counts)),
            'Most Frequently occuring Word' : counts.most_common()[0],
            'Least Frequently occuring Word' : counts.most_common()[-1]
        }

        dlg = QDialog(self)
        dlg.setWindowTitle("Text Details")
        dlg.setFixedSize(400, 200)
        
        dlgLayout = QGridLayout(dlg)
        
        c = 0
        for key, val in Details.items():
            dlgLayout.addWidget(QLabel(key), c, 0, 1, 1)
            dlgLayout.addWidget(QLabel(str(val)), c, 1, 1, 1)
            c += 1

        dlg.setLayout(dlgLayout)

        if dlg.exec_():
            pass

    def CreateWordCloud(self):
        counts = CountWords(self.FileTextViewBox.toPlainText())

        cloud = WordCloud(background_color='white').fit_words(counts)
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def DisplayWordHistogram(self):
        plot = PlotWordHistogram(self.FileTextViewBox.toPlainText())

        plt.show()
