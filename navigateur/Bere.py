# # importations à faire pour la réalisation d'une interface graphique
# import sys
# from PyQt5.QtWidgets import *

# # Première étape : création d'une application Qt avec QApplication
# #    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
# #    on vérifie s'il existe déjà une instance de QApplication
# app = QApplication.instance() 
# if not app: # sinon on crée une instance de QApplication
#     app = QApplication(sys.argv)

# # création d'une fenêtre avec QWidget dont on place la référence dans fen
# fen = QWidget()

# # la fenêtre est rendue visible
# fen.show()

# # exécution de l'application, l'exécution permet de gérer les événements
# app.exec_()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.navigator=QWebEngineView()
        self.navigator.setUrl(QUrl('http://twitter.com'))
        self.setCentralWidget(self.navigator)
        self.showMaximized()
        # navbar
        navbar=QToolBar()
        self.addToolBar(navbar)
        retour_btn=QAction('Retour',self)
        retour_btn.triggered.connect(self.navigator.back)

        refresh_btn=QAction("refresh",self)
        refresh_btn.triggered.connect(self.navigator.reload)

        advance_btn=QAction("Avancer",self)
        advance_btn.triggered.connect(self.navigator.forward)
        navbar.addAction(retour_btn)
        navbar.addAction(advance_btn)
        navbar.addAction(refresh_btn)
app=QApplication(sys.argv)
QApplication.setApplicationName("Bere")
fenetre=MainWindow()
app.exec()