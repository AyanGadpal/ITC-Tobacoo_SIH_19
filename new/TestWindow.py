import sys
import os
from PyQt5 import *
from pprint import pprint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
 

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()      #calling constructor of init method
        self.title = 'ITC Tobacco Grade Classification'
        self.left = 700
        self.top = 900
        self.width = 1100
        self.height = 550
        self.initUI()

    def initUI(self):
        #setting the attributes of window
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('ITC_icon.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.move(250,150)

        #setting background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        #HFrame 
        hframe = QLabel("",self)
        hframe.resize(250,550)
        hframe.setStyleSheet("border: 2px solid gray")
        
        #label of folder/file path
        path=QLabel("Folder/File Path: ",self)
        path.setStyleSheet("background-color: #FFF;border-radius:10px")
        path.resize(112,30)
        path.move(270,95)
        #ITC icon
        ITCicon = QLabel("",self)
        ITCicon.resize(250,250)
        pixmap = QPixmap('/home/tanvi/GUI/ITC_icon.png')
        ITCicon.setPixmap(pixmap)
        ITCicon.setScaledContents(True)
        ITCicon.setStyleSheet("border: 2px solid gray;transparent;")

        def test(self):
            print()

        #testbutton
        testButton = QPushButton("TEST",self)
        testButton.setToolTip("Click here to test images")
        testButton.move(0,475)
        testButton.setStyleSheet("background-color: #063072; color:#FFF; font-size:24px;" )
        testButton.resize(250,75)
        testButton.clicked.connect(test)

        def Browse(self):
            filePaths = QFileDialog.getOpenFileNames(None, 'Multiple File',"/home/tanvi/GUI",'*.jpg')
            dir_name=None
            displayPath.setText(str(filePaths[0][0]))
            pixmap = QPixmap(str(filePaths[0][0]))
            displayImage.setPixmap(pixmap)

        #button to browse image files
        browseImage = QPushButton('Browse image/(s)',self)
        browseImage.setToolTip("Select a single or multiple images")
        browseImage.move(400,20)
        browseImage.setStyleSheet("background-color: #063072; color:#FFF; font-size:18px;" )
        browseImage.resize(200,50)
        browseImage.clicked.connect(Browse)

        def choose_dir(self):
            dir_name = QFileDialog.getExistingDirectory(None,'Select a folder')
            filePaths=None
            if dir_name:
                displayPath.setText(str(dir_name))
            #file list has file names of file in filepaths
            filelist=os.listdir(filePaths)
                
        #button to browse folderS
        browseFolder = QPushButton('Browse Folder',self)
        browseFolder.setToolTip("Select a folder/directory")
        browseFolder.move(750,20)
        browseFolder.setStyleSheet("background-color: #063072; color:#FFF; font-size:18px;" )
        browseFolder.resize(200,50)
        browseFolder.clicked.connect(choose_dir)

        #label to display the path of image selected by user
        displayPath = QTextEdit(' Path of image/folder will be displayed here',self)
        displayPath.setDisabled(True)
        displayPath.setStyleSheet("background-color: #666d5e;border-radius:10px")
        displayPath.move(400,95)
        displayPath.resize(675,30)

        #label to display the image
        displayImage = QLabel('Browsed image will be displayed here',self)
        displayImage.setAlignment(Qt.AlignCenter)
        displayImage.setStyleSheet("background-color: #FFF;border: 2px solid #063072")
        displayImage.move(275,150)
        displayImage.resize(450,300)
        displayImage.setScaledContents(True)

        #frame label
        frame = QLabel("",self)
        frame.resize(350,300)
        frame.setStyleSheet("background-color:transparent;border: 2px solid #063072;")
        frame.move(725,150)
        
        #label for color code
        lcolorcode=QLabel("COLOR CODE",self)
        lcolorcode.move(750,190)
        lcolorcode.setStyleSheet("color: #000")

        #label for ripeness
        lripeness=QLabel("RIPENESS",self)
        lripeness.move(750,265)
        lripeness.setStyleSheet("color: #000")
        
        #label for grade
        lgrade=QLabel("GRADE TYPE",self)
        lgrade.move(750,330)
        lgrade.setStyleSheet("color: #000")
 
        #label to display color code
        colorPath = QTextEdit('',self)
        colorPath.setDisabled(True)
        colorPath.setStyleSheet("background-color: #E8E8E8;border-radius:10px; color:#000")
        colorPath.move(750,225)
        colorPath.resize(275,30)

        #label to display ripness
        ripness = QTextEdit('',self)
        ripness.setDisabled(True)
        ripness.setStyleSheet("background-color: #E8E8E8;border-radius:10px; color:#000")
        ripness.move(750,300)
        ripness.resize(275,30)

        #label to display grade
        ripness = QTextEdit('',self)
        ripness.setDisabled(True)
        ripness.setStyleSheet("background-color: #E8E8E8;border-radius:10px; color:#000")
        ripness.setText('')
        ripness.move(750,375)
        ripness.resize(275,30)

        def classify(self):
            print()

        #download button
        downloadButton = QPushButton("DOWNLOAD",self)
        downloadButton.setToolTip("Click here to export excel file")
        downloadButton.move(550,475)
        downloadButton.setStyleSheet("background-color: #063072; color:#FFF; font-size:18px;" )
        downloadButton.resize(250,50)
        downloadButton.clicked.connect(classify)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestWindow()
    sys.exit(app.exec_())
