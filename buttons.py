import sys
from PyQt4 import QtGui, QtCore
from card import *


class Buttons(QtGui.QFrame):
    def __init__(self, parent,h,w):
        super(Buttons, self).__init__()
        self.setFixedHeight(h)
        self.setFixedWidth(w)
        self.grid = QtGui.QGridLayout()
        self.okBtn = QtGui.QPushButton('Ok', self)
        self.okBtn.clicked.connect(self.accept)
        self.grid.addWidget(self.okBtn,0,0)
        self.putBox = QtGui.QCheckBox('Put a card.', self)
        self.raiseBox = QtGui.QCheckBox('Raise cards.', self)
        self.putBox.setCheckState(QtCore.Qt.Checked)
        self.putBox.stateChanged.connect(self.putC)
        self.raiseBox.stateChanged.connect(self.raiseC)
        self.grid.addWidget(self.putBox,0,1)
        self.grid.addWidget(self.raiseBox,1,1)
        self.setLayout(self.grid)
        self.parent=parent
        self.setStyleSheet("Buttons {background-image: url(pics/textureButb.png);}")
        self.initNew=False
        
    def initForNew(self):
        self.initNew=True
        self.raiseBox.setCheckState(QtCore.Qt.Unchecked)
        self.putBox.setCheckState(QtCore.Qt.Checked)
        self.initNew=False
            
    def putC(self,state):
        if self.initNew:
            return
        elif state == QtCore.Qt.Checked:
            self.raiseBox.setCheckState(QtCore.Qt.Unchecked)
            self.parent.stateChanged(True)
        else:
            self.raiseBox.setCheckState(QtCore.Qt.Checked)
            self.parent.stateChanged(False)
        
    def raiseC(self,state):
        if self.initNew:
            return
        elif state == QtCore.Qt.Checked:
            self.putBox.setCheckState(QtCore.Qt.Unchecked)
            self.parent.stateChanged(False)
        else:
            self.putBox.setCheckState(QtCore.Qt.Checked)
            self.parent.stateChanged(True)
    
    def accept(self):
        self.parent.accept()
    
    
    
