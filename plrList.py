import sys
from PyQt4 import QtGui, QtCore
from card import *

class ListPlr(QtGui.QFrame):
    def __init__(self, parent,h,w):
        super(ListPlr, self).__init__()
        self.setFixedHeight(h)
        self.setFixedWidth(w)
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)
        
        for i in range(10):
            lbl = QtGui.QLabel(self)
            self.grid.addWidget(lbl,i,1) 
            lbl1 = QtGui.QLabel(self)
            self.grid.addWidget(lbl1,i,2)
            lbl2 = QtGui.QLabel(self)
            self.grid.addWidget(lbl2,i,0)
        self.setStyleSheet("ListPlr {background-image: url(pics/textureListb.png);}")
        
    '''
    updates the plrlist
    '''
    def update(self,dic,nimi):        
        i=1
        txt="Player name"
        self.grid.itemAtPosition(0,1).widget().setText(txt)
        txt="Score"
        self.grid.itemAtPosition(0,2).widget().setText(txt)
        for name in dic:
            plrname=name
            score=dic[name]
            if len(plrname)>20:
                plrname=plrname[0:20]
            self.grid.itemAtPosition(i,1).widget().setText(plrname)
            txt=str(score)
            if nimi==name:
                self.grid.itemAtPosition(i,0).widget().setPixmap(QtGui.QPixmap("pics/hippo.png").scaled(20,20))
                self.grid.itemAtPosition(i,0).widget().show()
            else:
                self.grid.itemAtPosition(i,0).widget().hide()
            self.grid.itemAtPosition(i,2).widget().setText(txt)
            i+=1
        while i < 10:
            self.grid.itemAtPosition(i,0).widget().hide()
            self.grid.itemAtPosition(i,1).widget().setText('')
            self.grid.itemAtPosition(i,2).widget().setText('')
            i+=1
            
            
            
