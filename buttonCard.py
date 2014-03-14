import sys
from PyQt4 import QtGui, QtCore
from card import *

class ButtonCard(QtGui.QAbstractButton):
    def __init__(self, parent,pixmap,gparent,type):
        super(ButtonCard, self).__init__(parent)
        self.pixmap = pixmap
        self.card=None
        self.type=type
        self.gparent=gparent

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)
         
    def setPic(self,p,card):
        self.pixmap=p
        self.card=card

    def sizeHint(self):
        return self.pixmap.size()
    def mousePressEvent(self,event):
        if self.isVisible():    
            if self.type==1:    #Board.TYPE
                self.gparent.chosenBoard(self.card)
            elif self.type==0:  #HandPlr.TYPE
                self.gparent.chosenHand(self.card)


