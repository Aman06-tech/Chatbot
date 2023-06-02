from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from GAMAUI import Ui_MainWindow
import sys
import main


class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        main.TaskExe()

startFunctions = MainThread() 

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.GAMA_ui = Ui_MainWindow()
        
        self.GAMA_ui.setupUi(self)

        self.GAMA_ui.pushButton.clicked.connect(self.startFunc)

        self.GAMA_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.GAMA_ui.movies = QtGui.QMovie("../../../../2 - Python/3 -  Materials/G.U.I Material/B.G/1.gif")

        self.GAMA_ui.GIF.setMovie(self.GAMA_ui.movies)

        self.GAMA_ui.movies.start()



        self.GAMA_ui.movies_2 = QtGui.QMovie("../../../../2 - Python/3 -  Materials/G.U.I Material/VoiceReg/gui (4).gif")

        self.GAMA_ui.GIF2.setMovie(self.GAMA_ui.movies_2)

        self.GAMA_ui.movies_2.start()

        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

        startFunctions.start()

    def showtime(self):
        
        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")

        labbel = " Time :  " + label_time 

        self.GAMA_ui.textBrowser.setText(labbel)

Gui_App = QApplication(sys.argv)

Gui_GAMA = Gui_Start()

Gui_GAMA.show()

exit(Gui_App.exec_())