import sys
from PyQt4 import QtGui, QtCore

class Info(QtGui.QFrame):
    def __init__(self, parent,h,w):
        super(Info, self).__init__()
        self.setFixedHeight(h)
        self.setFixedWidth(w)
        self.grid = QtGui.QGridLayout()
        self.txtBox=QtGui.QTextBrowser()
        self.grid.addWidget(self.txtBox)
        self.setLayout(self.grid)
        self.txtBox.setStyleSheet("QTextBrowser {background-image: url(pics/textureInfo2.png);}")
        self.setStyleSheet("Info {background-image: url(pics/textureInfob.png);}")
        
    def update(self,text):
        self.txtBox.append(text)
        
    def clear(self):
        self.txtBox.clear()
