import sys
from PySide import QtGui, QtCore
from card import *

class CardContainer:
    def __init__(self):
        self.back=QtGui.QPixmap("pics/taka.png").scaled(100,130)
        
        '''
        clubs
        '''
        self.cA=QtGui.QPixmap("pics/cA.png").scaled(100,130)
        self.c2=QtGui.QPixmap("pics/c2.png").scaled(100,130)
        self.c3=QtGui.QPixmap("pics/c3.png").scaled(100,130)
        self.c4=QtGui.QPixmap("pics/c4.png").scaled(100,130)
        self.c5=QtGui.QPixmap("pics/c5.png").scaled(100,130)
        self.c6=QtGui.QPixmap("pics/c6.png").scaled(100,130)
        self.c7=QtGui.QPixmap("pics/c7.png").scaled(100,130)
        self.c8=QtGui.QPixmap("pics/c8.png").scaled(100,130)
        self.c9=QtGui.QPixmap("pics/c9.png").scaled(100,130)
        self.c10=QtGui.QPixmap("pics/c10.png").scaled(100,130)
        self.cJ=QtGui.QPixmap("pics/cJ.png").scaled(100,130)
        self.cQ=QtGui.QPixmap("pics/cQ.png").scaled(100,130)
        self.cK=QtGui.QPixmap("pics/cK.png").scaled(100,130)
        
        '''
        diamonds
        '''
        self.dA=QtGui.QPixmap("pics/dA.png").scaled(100,130)
        self.d2=QtGui.QPixmap("pics/d2.png").scaled(100,130)
        self.d3=QtGui.QPixmap("pics/d3.png").scaled(100,130)
        self.d4=QtGui.QPixmap("pics/d4.png").scaled(100,130)
        self.d5=QtGui.QPixmap("pics/d5.png").scaled(100,130)
        self.d6=QtGui.QPixmap("pics/d6.png").scaled(100,130)
        self.d7=QtGui.QPixmap("pics/d7.png").scaled(100,130)
        self.d8=QtGui.QPixmap("pics/d8.png").scaled(100,130)
        self.d9=QtGui.QPixmap("pics/d9.png").scaled(100,130)
        self.d10=QtGui.QPixmap("pics/d10.png").scaled(100,130)
        self.dJ=QtGui.QPixmap("pics/dJ.png").scaled(100,130)
        self.dQ=QtGui.QPixmap("pics/dQ.png").scaled(100,130)
        self.dK=QtGui.QPixmap("pics/dK.png").scaled(100,130)
        
        '''
        spades
        '''
        self.sA=QtGui.QPixmap("pics/sA.png").scaled(100,130)
        self.s2=QtGui.QPixmap("pics/s2.png").scaled(100,130)
        self.s3=QtGui.QPixmap("pics/s3.png").scaled(100,130)
        self.s4=QtGui.QPixmap("pics/s4.png").scaled(100,130)
        self.s5=QtGui.QPixmap("pics/s5.png").scaled(100,130)
        self.s6=QtGui.QPixmap("pics/s6.png").scaled(100,130)
        self.s7=QtGui.QPixmap("pics/s7.png").scaled(100,130)
        self.s8=QtGui.QPixmap("pics/s8.png").scaled(100,130)
        self.s9=QtGui.QPixmap("pics/s9.png").scaled(100,130)
        self.s10=QtGui.QPixmap("pics/s10.png").scaled(100,130)
        self.sJ=QtGui.QPixmap("pics/sJ.png").scaled(100,130)
        self.sQ=QtGui.QPixmap("pics/sQ.png").scaled(100,130)
        self.sK=QtGui.QPixmap("pics/sK.png").scaled(100,130)
        
        '''
        heart
        '''
        self.hA=QtGui.QPixmap("pics/hA.png").scaled(100,130)
        self.h2=QtGui.QPixmap("pics/h2.png").scaled(100,130)
        self.h3=QtGui.QPixmap("pics/h3.png").scaled(100,130)
        self.h4=QtGui.QPixmap("pics/h4.png").scaled(100,130)
        self.h5=QtGui.QPixmap("pics/h5.png").scaled(100,130)
        self.h6=QtGui.QPixmap("pics/h6.png").scaled(100,130)
        self.h7=QtGui.QPixmap("pics/h7.png").scaled(100,130)
        self.h8=QtGui.QPixmap("pics/h8.png").scaled(100,130)
        self.h9=QtGui.QPixmap("pics/h9.png").scaled(100,130)
        self.h10=QtGui.QPixmap("pics/h10.png").scaled(100,130)
        self.hJ=QtGui.QPixmap("pics/hJ.png").scaled(100,130)
        self.hQ=QtGui.QPixmap("pics/hQ.png").scaled(100,130)
        self.hK=QtGui.QPixmap("pics/hK.png").scaled(100,130)
        
        
        '''
        chosenCards
        '''
        
        '''
        clubsChosen
        '''
        self.cAb=QtGui.QPixmap("pics/cAb.png").scaled(100,130)
        self.c2b=QtGui.QPixmap("pics/c2b.png").scaled(100,130)
        self.c3b=QtGui.QPixmap("pics/c3b.png").scaled(100,130)
        self.c4b=QtGui.QPixmap("pics/c4b.png").scaled(100,130)
        self.c5b=QtGui.QPixmap("pics/c5b.png").scaled(100,130)
        self.c6b=QtGui.QPixmap("pics/c6b.png").scaled(100,130)
        self.c7b=QtGui.QPixmap("pics/c7b.png").scaled(100,130)
        self.c8b=QtGui.QPixmap("pics/c8b.png").scaled(100,130)
        self.c9b=QtGui.QPixmap("pics/c9b.png").scaled(100,130)
        self.c10b=QtGui.QPixmap("pics/c10b.png").scaled(100,130)
        self.cJb=QtGui.QPixmap("pics/cJb.png").scaled(100,130)
        self.cQb=QtGui.QPixmap("pics/cQb.png").scaled(100,130)
        self.cKb=QtGui.QPixmap("pics/cKb.png").scaled(100,130)
        
        '''
        diamondsChosen
        '''
        self.dAb=QtGui.QPixmap("pics/dAb.png").scaled(100,130)
        self.d2b=QtGui.QPixmap("pics/d2b.png").scaled(100,130)
        self.d3b=QtGui.QPixmap("pics/d3b.png").scaled(100,130)
        self.d4b=QtGui.QPixmap("pics/d4b.png").scaled(100,130)
        self.d5b=QtGui.QPixmap("pics/d5b.png").scaled(100,130)
        self.d6b=QtGui.QPixmap("pics/d6b.png").scaled(100,130)
        self.d7b=QtGui.QPixmap("pics/d7b.png").scaled(100,130)
        self.d8b=QtGui.QPixmap("pics/d8b.png").scaled(100,130)
        self.d9b=QtGui.QPixmap("pics/d9b.png").scaled(100,130)
        self.d10b=QtGui.QPixmap("pics/d10b.png").scaled(100,130)
        self.dJb=QtGui.QPixmap("pics/dJb.png").scaled(100,130)
        self.dQb=QtGui.QPixmap("pics/dQb.png").scaled(100,130)
        self.dKb=QtGui.QPixmap("pics/dKb.png").scaled(100,130)
        
        '''
        spadesChosen
        '''
        self.sAb=QtGui.QPixmap("pics/sAb.png").scaled(100,130)
        self.s2b=QtGui.QPixmap("pics/s2b.png").scaled(100,130)
        self.s3b=QtGui.QPixmap("pics/s3b.png").scaled(100,130)
        self.s4b=QtGui.QPixmap("pics/s4b.png").scaled(100,130)
        self.s5b=QtGui.QPixmap("pics/s5b.png").scaled(100,130)
        self.s6b=QtGui.QPixmap("pics/s6b.png").scaled(100,130)
        self.s7b=QtGui.QPixmap("pics/s7b.png").scaled(100,130)
        self.s8b=QtGui.QPixmap("pics/s8b.png").scaled(100,130)
        self.s9b=QtGui.QPixmap("pics/s9b.png").scaled(100,130)
        self.s10b=QtGui.QPixmap("pics/s10b.png").scaled(100,130)
        self.sJb=QtGui.QPixmap("pics/sJb.png").scaled(100,130)
        self.sQb=QtGui.QPixmap("pics/sQb.png").scaled(100,130)
        self.sKb=QtGui.QPixmap("pics/sKb.png").scaled(100,130)
        
        '''
        heartChosen
        '''
        self.hAb=QtGui.QPixmap("pics/hAb.png").scaled(100,130)
        self.h2b=QtGui.QPixmap("pics/h2b.png").scaled(100,130)
        self.h3b=QtGui.QPixmap("pics/h3b.png").scaled(100,130)
        self.h4b=QtGui.QPixmap("pics/h4b.png").scaled(100,130)
        self.h5b=QtGui.QPixmap("pics/h5b.png").scaled(100,130)
        self.h6b=QtGui.QPixmap("pics/h6b.png").scaled(100,130)
        self.h7b=QtGui.QPixmap("pics/h7b.png").scaled(100,130)
        self.h8b=QtGui.QPixmap("pics/h8b.png").scaled(100,130)
        self.h9b=QtGui.QPixmap("pics/h9b.png").scaled(100,130)
        self.h10b=QtGui.QPixmap("pics/h10b.png").scaled(100,130)
        self.hJb=QtGui.QPixmap("pics/hJb.png").scaled(100,130)
        self.hQb=QtGui.QPixmap("pics/hQb.png").scaled(100,130)
        self.hKb=QtGui.QPixmap("pics/hKb.png").scaled(100,130)
        
        
    def getCard(self,suit,num):
        if suit==Card.SPADES:
            if num==1:
                return self.sA
            elif num==2:
                return self.s2
            elif num==3:
                return self.s3
            elif num==4:
                return self.s4
            elif num==5:
                return self.s5
            elif num==6:
                return self.s6
            elif num==7:
                return self.s7
            elif num==8:
                return self.s8
            elif num==9:
                return self.s9
            elif num==10:
                return self.s10
            elif num==11:
                return self.sJ
            elif num==12:
                return self.sQ
            elif num==13:
                return self.sK
            
        if suit==Card.HEARTS:
            if num==1:
                return self.hA
            elif num==2:
                return self.h2
            elif num==3:
                return self.h3
            elif num==4:
                return self.h4
            elif num==5:
                return self.h5
            elif num==6:
                return self.h6
            elif num==7:
                return self.h7
            elif num==8:
                return self.h8
            elif num==9:
                return self.h9
            elif num==10:
                return self.h10
            elif num==11:
                return self.hJ
            elif num==12:
                return self.hQ
            elif num==13:
                return self.hK
        
        if suit==Card.DIAMONDS:
            if num==1:
                return self.dA
            elif num==2:
                return self.d2
            elif num==3:
                return self.d3
            elif num==4:
                return self.d4
            elif num==5:
                return self.d5
            elif num==6:
                return self.d6
            elif num==7:
                return self.d7
            elif num==8:
                return self.d8
            elif num==9:
                return self.d9
            elif num==10:
                return self.d10
            elif num==11:
                return self.dJ
            elif num==12:
                return self.dQ
            elif num==13:
                return self.dK
        
        if suit==Card.CLUBS:
            if num==1:
                return self.cA
            elif num==2:
                return self.c2
            elif num==3:
                return self.c3
            elif num==4:
                return self.c4
            elif num==5:
                return self.c5
            elif num==6:
                return self.c6
            elif num==7:
                return self.c7
            elif num==8:
                return self.c8
            elif num==9:
                return self.c9
            elif num==10:
                return self.c10
            elif num==11:
                return self.cJ
            elif num==12:
                return self.cQ
            elif num==13:
                return self.cK
            
            
            
    def getCardChosen(self,suit,num):
        if suit==Card.SPADES:
            if num==1:
                return self.sAb
            elif num==2:
                return self.s2b
            elif num==3:
                return self.s3b
            elif num==4:
                return self.s4b
            elif num==5:
                return self.s5b
            elif num==6:
                return self.s6b
            elif num==7:
                return self.s7b
            elif num==8:
                return self.s8b
            elif num==9:
                return self.s9b
            elif num==10:
                return self.s10b
            elif num==11:
                return self.sJb
            elif num==12:
                return self.sQb
            elif num==13:
                return self.sKb
            
        if suit==Card.HEARTS:
            if num==1:
                return self.hAb
            elif num==2:
                return self.h2b
            elif num==3:
                return self.h3b
            elif num==4:
                return self.h4b
            elif num==5:
                return self.h5b
            elif num==6:
                return self.h6b
            elif num==7:
                return self.h7b
            elif num==8:
                return self.h8b
            elif num==9:
                return self.h9b
            elif num==10:
                return self.h10b
            elif num==11:
                return self.hJb
            elif num==12:
                return self.hQb
            elif num==13:
                return self.hKb
        
        if suit==Card.DIAMONDS:
            if num==1:
                return self.dAb
            elif num==2:
                return self.d2b
            elif num==3:
                return self.d3b
            elif num==4:
                return self.d4b
            elif num==5:
                return self.d5b
            elif num==6:
                return self.d6b
            elif num==7:
                return self.d7b
            elif num==8:
                return self.d8b
            elif num==9:
                return self.d9b
            elif num==10:
                return self.d10b
            elif num==11:
                return self.dJb
            elif num==12:
                return self.dQb
            elif num==13:
                return self.dKb
        
        if suit==Card.CLUBS:
            if num==1:
                return self.cAb
            elif num==2:
                return self.c2b
            elif num==3:
                return self.c3b
            elif num==4:
                return self.c4b
            elif num==5:
                return self.c5b
            elif num==6:
                return self.c6b
            elif num==7:
                return self.c7b
            elif num==8:
                return self.c8b
            elif num==9:
                return self.c9b
            elif num==10:
                return self.c10b
            elif num==11:
                return self.cJb
            elif num==12:
                return self.cQb
            elif num==13:
                return self.cKb
            
    def getBack(self):
        return self.back
            