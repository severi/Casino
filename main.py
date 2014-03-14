from windowGui import *
import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):    
        startGame = QtGui.QAction(QtGui.QIcon('pics/exit.png'), '&Start', self)
        startGame.setShortcut('Ctrl+N')
        startGame.setStatusTip('New Game')
        
        saveGame = QtGui.QAction(QtGui.QIcon('pics/exit.png'), '&Save', self)
        saveGame.setShortcut('Ctrl+S')
        saveGame.setStatusTip('Save Game')
        
        loadGame = QtGui.QAction(QtGui.QIcon('pics/exit.png'), '&Load', self)
        loadGame.setShortcut('Ctrl+L')
        loadGame.setStatusTip('Load Game')
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(startGame)
        fileMenu.addAction(saveGame)
        fileMenu.addAction(loadGame)
        self.setWindowTitle('Kasino')    
        
        self.window=Window(self)
        self.setCentralWidget(self.window)
        self.move(0, 0)
        
        startGame.triggered.connect(self.window.initGame)
        loadGame.triggered.connect(self.window.loadGame)
        saveGame.triggered.connect(self.window.saveGame)
        self.show()
        
    def keyPressEvent(self,event):
        if event.key()==QtCore.Qt.Key_Return: # = enter mac:ssa
            self.window.accept()
            self.window.showC()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
