from game import Game
from gameLogic import *
from computerPlayerIO import *
from cardContainer import *
from infoBox import *
from boardGui import *
from handGui import *
from plrList import *
from buttons import *
import sys
from PySide import QtGui, QtCore
from card import *
import time

class Window(QtGui.QFrame):
    BREAKTIME=2
    
    def __init__(self,parent):
        super(Window, self).__init__()
        self.game = Game()
        self.dic={}
        self.parent=parent
        self.timer = QtCore.QBasicTimer()
        self.roundOn = False
        self.gameOn = False
        self.turnOn = False
        self.firstInit=True
        self.hRaise=False
        self.playNext2=False
        self.playNext3=False
        self.hPut=False
        self.pauseGame=False
        self.cardsToBeRaised=None
        self.raiseCard=None
        self.putBoxChecked=True
        self.startHumanTurn=False
        self.player=None
        self.errorClose=False  
        self.showHiddenCards=False  
        self.waitForNewRoundStart=False        
        self.setStyleSheet("Window {background-image: url(pics/concrete.png);background-repeat: no-repeat;}")
        self.container=CardContainer()
        self.updateGui()
        self.setGeometry(300, 300, 1300,800)
    
    '''
    updates the GUI
    if self.firstInit: --> goes here in the beginning and initializes the gui components.
    elif show: --> if self.player is computer, players hand is shown so that the backside of the cards is up,
                   if self.player is human, all cards are shown normally
    else: -->    shows the hand cards as if the player was computer.  This is used to hide human players cards before "show cards"-button
                 has been pressed
    '''
    
    def updateGui(self,show=True):
        if self.firstInit:
            self.grid = QtGui.QGridLayout()
            self.board = Board(self,400,900,self.container)
            self.grid.addWidget(self.board,0,0)
            self.plrList = ListPlr(self,400,300)
            self.grid.addWidget(self.plrList,0,1)
            self.infoBox = Info(self,100,900)
            self.grid.addWidget(self.infoBox,1,0)
            self.showBtn = QtGui.QPushButton('Show cards', self)
            self.showBtn.clicked.connect(self.showC)
            self.grid.addWidget(self.showBtn,1,1)
            self.grid.itemAtPosition(1,1).widget().hide()
            self.hand = HandPlr(self,200,900,self.container)
            self.grid.addWidget(self.hand,2,0)
            self.buttons=Buttons(self,100,300)
            self.grid.addWidget(self.buttons,2,1)
            self.grid.itemAtPosition(2,1).widget().hide()
            self.setLayout(self.grid)
            self.firstInit=False
            
        elif show:
            nimi=''
            if self.player!=None:
                nimi=self.player.getName()
            kortit=[]
            if self.player!=None:
                kortit=self.player.getHand().getCards()
            tyyppi=Player.COMPUTER
            if self.player!=None:
                tyyppi=self.player.getType()
                
            self.board.update(self.game.getBoard().getCards())
            self.plrList.update(self.dic,nimi)
            self.hand.update(kortit,tyyppi)
            
        else:
            nimi=''
            if self.player!=None:
                nimi=self.player.getName()
            kortit=[]
            if self.player!=None:
                kortit=self.player.getHand().getCards()
                
            self.board.update(self.game.getBoard().getCards())
            self.plrList.update(self.dic,nimi)
            self.hand.update(kortit,Player.COMPUTER)
    
    '''
    initializes a new game, if a game is already running, player 
    has to confirm that he wants to quit the existing game and start a new one
    '''
    def initGame(self):
        startIt= not self.gameOn
        
        if not startIt:
            self.pauseGame=True
            valinta = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure you wish to start a new game", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if valinta == QtGui.QMessageBox.Yes:
                startIt=True
            else:
                self.pauseGame=False
   
        if startIt:
            lkm = self.getPlayerAmount()
            if lkm == -1:
                return
            
            
            self.roundOn = False
            self.gameOn = False
            self.turnOn = False
            self.hRaise=False
            self.playNext2=False
            self.playNext3=False
            self.hPut=False
            self.pauseGame=False
            self.cardsToBeRaised=None
            self.raiseCard=None
            self.putBoxChecked=True
            self.startHumanTurn=False
            self.player=None
            self.errorClose=False
            
            #uudet
            self.showHiddenCards=False  
            self.waitForNewRoundStart=False  
            
            self.infoBox.clear()
            self.game=Game()
            
            for i in range(lkm):
                self.addPlayer(i+1)
            self.dic={}
            for plr in self.game.getPlayers():
                self.dic[plr.getName()]=plr.getPoints()
            self.pauseGame=False
            self.gameOn = True
            if not self.timer.isActive():
                self.timer.start(Game.SPEED, self)
            
    '''
    returns a boolean that is used in timerEvent to determine whether a new round should be started or not
    '''
    def startNewRound(self):
        return self.gameOn and not self.roundOn  and not self.turnOn
    
    '''
    returns a boolean that is used in timerEvent to determine whether a new turn should be started or not
    '''
    def startNewTurn(self):
        return self.gameOn and self.roundOn  and not self.turnOn

    '''
    timerEvent is triggered by the QtCore.QBasicTimer(), it handles the game loop
    '''
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            
            #error occured while loading a game.  The whole programm needs to be shut down
            if self.errorClose:
                time.sleep(3)
                print "The program was closed due to an error."
                self.close()
                self.parent.close()
                return
            
            #game is over, print the winner
            elif self.startNewRound() and self.game.gameOver() and not self.pauseGame:
                self.gameOn=False
                
                #find the winner(s)
                paras=[]
                parasp=-1
                for plr in self.game.getPlayers():
                    if parasp<plr.getPoints():
                        parasp=plr.getPoints()
                        paras=[]
                        paras.append(plr)
                    elif parasp==plr.getPoints():
                        paras.append(plr)
                        
                txt=''
                if len(paras)==1:
                    txt="Game over. Winner was "+paras[0].getName()+ " with "+str(paras[0].getPoints())+" points."
                else:
                    txt="Game over. The following players won the game with "+str(paras[0].getPoints())+" points:\n"
                    for i in paras:
                        txt+=i.getName()
                        txt+="\n"
                self.infoBox.update(txt)
                
            #start a new round
            elif self.startNewRound() and not self.pauseGame:
                self.grid.itemAtPosition(2,1).widget().hide()
                self.grid.itemAtPosition(1,1).widget().setText("Start a new round")
                self.grid.itemAtPosition(1,1).widget().show()
                self.updateGui(False)
                self.waitForNewRoundStart=True
                
                
            #start a new turn, if player is comp, show cards
            elif self.startNewTurn() and not self.pauseGame:
                self.grid.itemAtPosition(1,1).widget().hide()
                self.grid.itemAtPosition(1,1).widget().setText("Show Cards")
                self.turnOn=True
                self.player = self.game.getNextInTurn()
                if self.player.getType()==Player.COMPUTER:
                    self.updateGui()
                self.playNext2=True
                
            #if player is human, show cards backside up, if comp, play turn
            elif self.playNext2 and not self.pauseGame:
                self.playNext2=False
                if not self.player.hasCards():
                    self.playNext3=True
                elif self.player.getType()==Player.HUMAN:
                    self.grid.itemAtPosition(1,1).widget().show()
                    self.updateGui(False)
                    self.showHiddenCards=True
                else:
                    self.playComputerTurn()
                    self.playNext3=True
                    
            #start human turn
            elif self.startHumanTurn and not self.pauseGame:
                self.startHumanTurn=False
                self.cardsToBeRaised=[]
                self.raiseCard=None
                self.hPut=True
                self.grid.itemAtPosition(2,1).widget().initForNew()
                self.grid.itemAtPosition(2,1).widget().show()
                

            #check if round is over
            elif self.playNext3 and not self.pauseGame:
                self.playNext3=False
                self.grid.itemAtPosition(2,1).widget().hide()
                
                #if round is over, calculate points
                if not self.game.continueRound():
                    self.game.dealBoardToLatest()            
                    self.game.extraCardPoints, self.game.extraSpadesPoints,utxt\
                     = calculatePoints(self.game.getPlayers(),self.game.extraCardPoints,self.game.extraSpadesPoints)
                    for plr in self.game.getPlayers():
                        self.dic[plr.getName()]=plr.getPoints()
                    
                    self.updateGui()
                    self.roundOn=False
                    self.infoBox.update(utxt)
                self.turnOn=False
        else:
            #nain oli jossain mallissa joten laitoin tahankin :---d
            QtGui.QFrame.timerEvent(self, event)

    def playComputerTurn(self):
        pickCards,raiseCard,cards = playComputerTurn(self.player,self.game)
        text=''
        #raiseCards
        if pickCards:
            moveCardsToStack(raiseCard,cards,self.game,self.player)            
            self.game.lastRaise=self.player
            mj=""
            for card in cards:
                mj+=str(card)
                mj+=" "
            text+= self.player.getName()+" raisecard:"+str(raiseCard)+"  cards:"+mj
        
        #put card to board     
        else:
            putCardToBoard(raiseCard,self.game,self.player)
            text+=self.player.getName()+" put:"+str(raiseCard)
        
        newCard = self.game.deal(1)
        self.player.addCardsToHand(newCard)
        
        if len(self.game.getBoard().getCards())==0 and len(newCard)!=0:
            self.player.raiseCottages(1)
            text+= " and got a cottage!"
        self.infoBox.update(text)
        
        for plr in self.game.getPlayers():
            self.dic[plr.getName()]=plr.getPoints()
            
    def addPlayer(self,num):
        txt='th'
        if num==1:
            txt='st'
        elif num==2:
            txt='nd'
        elif num==3:
            txt='rd'
        name=''  
        ok = False
        while not ok:
            text='Name of the %d%s player:              '%(num,txt)
            text1='Name of the %d%s player'%(num,txt)
            name, ok = QtGui.QInputDialog.getText(self, text1, text)
            for plr in self.game.getPlayers():
                if plr.getName()==name:
                    ok=False
        ok = False
        type1=''
        if len(name)>20:
            name=name[0:20]
        while not ok:
            text='c=computer, h=human                     '
            text1="Type of the %d%s player"%(num,txt)
            type1, ok = QtGui.QInputDialog.getText(self, text1, text)
            if type1.lower()!='c' and type1.lower()!='h':
                ok=False
        type = Player.COMPUTER
        if type1.lower()=='h':
            type = Player.HUMAN
        self.game.addPlayer(name,type)
        
    def getPlayerAmount(self):
        ok = False
        am=-1
        while not(1<am<9):
            text, ok = QtGui.QInputDialog.getText(self, 'Amount of players (2-8)', 'Enter amount:                                 ')
            if not ok:
                return -1
            try:
                am=int(text)
            except ValueError:
                am=-1
        return am
    
    '''
    this methdod is called if a card on the board is clicked
    '''
    def chosenBoard(self,card):
        if self.hRaise:
            if card not in self.cardsToBeRaised:
                self.cardsToBeRaised.append(card)
            else:
                self.cardsToBeRaised.remove(card)
            self.board.choose(card)
    
    '''
    this method is called if a card on players hand is clicked
    '''
    def chosenHand(self,card):
        if self.hPut or self.hRaise:
            self.raiseCard=card
            self.hand.choose(card)
         
    '''
    this method is called if "raise Cards"-box is chosen and "put cards"-box unchosen or vice versa
    '''
    def stateChanged(self,put):
        self.putBoxChecked=put
        self.raiseCard=None
        self.cardsToBeRaised=[]
        self.hand.unchoose()
        self.board.unchoose()
        if put:
            self.hRaise=False
            self.hPut=True
        else:
            self.hRaise=True
            self.hPut=False
    
    '''
    this method is called if the "show cards"-button is pressed
    '''
    def showC(self):
        if self.showHiddenCards:
            self.showHiddenCards=False
            self.grid.itemAtPosition(1,1).widget().hide()
            self.updateGui()
            self.startHumanTurn=True
            
        elif self.waitForNewRoundStart:
            self.waitForNewRoundStart=False
            self.game.initForNewRound()
            self.roundOn=True          
      
    '''
    this method is called if "ok"-button is pressed
    '''
    def accept(self):
        #if ok is pressed and put-box checked
        if self.hPut:
            self.hPut=False
            if self.raiseCard==None:
                self.infoBox.update("Invalid put!")
                self.hPut=True
                return
            text=''
            putCardToBoard(self.raiseCard,self.game,self.player)
            text+=self.player.getName()+" put:"+str(self.raiseCard)
  
            #draw a new card if possible
            newCard = self.game.deal(1) #TASSA H1
            self.player.addCardsToHand(newCard)
            
            self.infoBox.update(text)
            
            for plr in self.game.getPlayers():
                self.dic[plr.getName()]=plr.getPoints()
            self.playNext3=True
            
        #if ok is pressed and raise-box checked
        elif self.hRaise:
            self.hRaise=False
            if self.raiseCard==None:
                self.infoBox.update("raise was not valid")
                self.hRaise=True
                return
            validR = validRaise(self.raiseCard, self.cardsToBeRaised)
            if not validR:
                self.infoBox.update("raise was not valid")
                self.hRaise=True
            else:
                self.game.lastRaise=self.player
                moveCardsToStack(self.raiseCard,self.cardsToBeRaised,self.game,self.player)
                text=""
                mj=""
                for card in self.cardsToBeRaised:
                    mj+=str(card)
                    mj+=" "
                text+= self.player.getName()+" raisecard:"+str(self.raiseCard)+"  cards:"+mj
                
                newCard = self.game.deal(1) #TASSA H2
                self.player.addCardsToHand(newCard)
                
                if len(self.game.getBoard().getCards())==0 and len(newCard)!=0:
                    self.player.raiseCottages(1)
                    text+= " and got a cottage!"

                self.infoBox.update(text)
                for plr in self.game.getPlayers():
                    self.dic[plr.getName()]=plr.getPoints()
                self.playNext3=True
                
                
    '''
    loads a game.
    Error handling:     if file is not name.txt , the file is dismissed
                        if the file doesnt start with GAM11, the file is dismissed
                        if reading the file takes too long, it probably means no "END000" is found, the file is dismissed and game closed.
    '''
    def loadGame(self):
        try:
            
            self.pauseGame=True
            fname, ok = QtGui.QFileDialog.getOpenFileName(self, 'Open file','savedGames')
            if not ok:
                self.pauseGame=False
                return
            paate=fname.split(".")
            if len(paate)!=2 or paate[1]!="txt":
                self.infoBox.update("Error: Invalid file.")
                self.pauseGame=False
                return
            
            file=open(fname,'r')
            
            
            line=file.read(6)
            if line!='GAM111':
                self.infoBox.update("Error: Invalid file.")
                file.close()
                self.pauseGame=False
                return
            
            self.game=Game()
            line=file.read(6)
            tic = time.clock()
            toc=0
            
            while line!='END000':
                if (toc-tic)>Window.BREAKTIME:
                    break
                
                cmd=line[0:3]
                lkm=line[3:6].strip('0')
                if len(lkm)==0:
                    lkm='0'
                    
                #from game
                if cmd=='PLR':
                    line=file.read(6)
                    nimi=None
                    cot=None
                    poi=None
                    han=None
                    typ=None
                    sta=None
                    
                    while line!='END001':
                        if (toc-tic)>Window.BREAKTIME:
                            break
                        
                        cmd1=line[0:3]
                        lkm1=line[3:6]
                        lkm1=line[3:6].strip('0')
                        if len(lkm1)==0:
                            lkm1='0'
                        
                        if cmd1=='NAM':
                            line=file.read(int(lkm1))
                            nimi=line
                        
                        elif cmd1=='COT':
                            line=file.read(int(lkm1))
                            cot=int(line)
                            
                        elif cmd1=='POI':
                            line=file.read(int(lkm1))
                            poi=int(line)
                            
                        elif cmd1=='HAN':
                            han=[]
                            for i in range(int(lkm1)):
                                line=file.read(2)
                                card=makeCard(line)
                                #print card
                                han.append(card)
                            #raw_input("sfsad\n")
                                
                        elif cmd1 =='TYP':
                            line=file.read(int(lkm1))
                            typ=int(line)
                            
                        elif cmd1 == 'STA':
                            sta=[]
                            for i in range(int(lkm1)):
                                line=file.read(2)
                                card=makeCard(line)
                                sta.append(card)
                        line=file.read(6)
                        toc = time.clock()
                                
                    nplayer=Player(nimi,typ)
                    nplayer.setCottages(cot)
                    nplayer.setPoints(poi)
                    nplayer.getHand().setCards(han)
                    nplayer.setStack(sta)
                    self.game.addPlayer2(nplayer)
                    
                elif cmd=='BOA':    #board
                    cards=[]
                    for i in range(int(lkm)):
                        line=file.read(2)
                        card=makeCard(line)
                        cards.append(card)
                    self.game.getBoard().setCards(cards)
                    
                elif cmd=='DEC':    #deck
                    cards=[]
                    for i in range(int(lkm)):
                        line=file.read(2)
                        card=makeCard(line)
                        cards.append(card)
                    self.game.getDeck().setCards(cards)
                    
                elif cmd=='NTU': #nextInTurn
                    line=file.read(int(lkm))
                    self.game.nextInTurn=int(line)
                    
                elif cmd=='NDE':    #nexdealer
                    line=file.read(int(lkm))
                    self.game.nextDealer=int(line)
                    
                elif cmd=='ECP':    #extraCardPoints
                    line=file.read(int(lkm))
                    self.game.extraCardPoints=int(line)
                    
                elif cmd=='ESP': #extraSpadesPoints
                    line=file.read(int(lkm))
                    self.game.extraSpadesPoints=int(line)
                    
                elif cmd=='LRA': #lastRaise
                    line=file.read(int(lkm))
                    if line=='9':
                        self.game.lastRaise=None
                    else:
                        self.game.lastRaise=self.game.getPlayers()[int(line)]
                #/GAME
    
                elif cmd=='RON':#bool roundOn
                    line=file.read(int(lkm))
                    self.roundOn=bool(int(line))
                    
                elif cmd=='GON':#bool gameOn
                    line=file.read(int(lkm))
                    self.gameOn=bool(int(line))
    
                elif cmd=='TON': #bool turnOn
                    line=file.read(int(lkm))
                    self.turnOn=bool(int(line))
                    
                elif cmd=='FIN': #bool firstInit
                    line=file.read(int(lkm))
                    self.firstInit=bool(int(line))
                    
                elif cmd=='HRA': #bool hRaise
                    line=file.read(int(lkm))
                    self.hRaise=bool(int(line))
                    
                elif cmd=='PN2': #bool playNext2
                    line=file.read(int(lkm))
                    self.playNext2=bool(int(line))
                    
                elif cmd=='PN3': #bool playNext3
                    line=file.read(int(lkm))
                    self.playNext3=bool(int(line))
                    
                elif cmd=='HPU': #bool hPut
                    line=file.read(int(lkm))
                    self.hPut=bool(int(line))
                    
                elif cmd=='PBC': #bool putBoxChecked
                    line=file.read(int(lkm))
                    self.putBoxChecked=bool(int(line))
                    
                elif cmd=='PGA': #pauseGame
                    line=file.read(int(lkm))
                    self.pauseGame=bool(int(line))
                
                elif cmd=='SHT':#bool startHumanTurn
                    line=file.read(int(lkm))
                    self.startHumanTurn=bool(int(line))
                    
                elif cmd=='SPL': #self.player
                    line=file.read(int(lkm))
                    if line=='9':
                        self.player=None
                    else:
                        self.player = self.game.getPlayers()[int(line)]
                    
                elif cmd=='SHC':
                    line=file.read(int(lkm))
                    self.showHiddenCards=bool(int(line))
                    
                elif cmd=='SNR':
                    line=file.read(int(lkm))
                    self.waitForNewRoundStart=bool(int(line))
                    
                line=file.read(6)
                toc = time.clock()
    
            file.close()
            
            if (toc-tic)>Window.BREAKTIME:
                self.infoBox.update("ERROR: Invalid file, closing the programm...")
                self.errorClose=True
                if not self.timer.isActive():
                    self.timer.start(Game.SPEED, self)
                return
            
            #updating snr-button txt
            if self.waitForNewRoundStart:
                self.grid.itemAtPosition(1,1).widget().setText("Start a new round")
            else:
                self.grid.itemAtPosition(1,1).widget().setText("Show Cards")
                
            
            self.infoBox.clear()
            self.dic={}
            for plr in self.game.getPlayers():
                self.dic[plr.getName()]=plr.getPoints()
            
            self.updateGui()
            if self.hRaise or self.hPut:
                self.stateChanged(True)
                self.grid.itemAtPosition(2,1).widget().initForNew()
                self.grid.itemAtPosition(2,1).widget().show()
            else:
                self.grid.itemAtPosition(2,1).widget().hide()
                
            if self.showHiddenCards or self.waitForNewRoundStart:
                self.grid.itemAtPosition(1,1).widget().show()
                self.updateGui(False)
            else:
                self.grid.itemAtPosition(1,1).widget().hide()
            
            if not self.timer.isActive():
                    self.timer.start(Game.SPEED, self)
            
            name=fname.split("/")
            if len(name)==0:
                name=fname
            else:
                name=name[len(name)-1]
            txt="Game loaded successfully from "+name+"."
            self.infoBox.update(txt)
            self.pauseGame=False
        
        except IOError:
            self.infoBox.update("ERROR: Invalid file, closing the programm...")
            self.errorClose=True
            if not self.timer.isActive():
                self.timer.start(Game.SPEED, self)
            return
    
    
    def saveGame(self):
        if not self.gameOn:
            self.infoBox.update("ERROR: Cannot save a game that is not running. Start a game first.")
            return
        self.pauseGame=True
        fname,ok = QtGui.QFileDialog.getSaveFileName(self,'save file','savedGames')
        paate = fname.split(".")
        if not ok or len(paate)!=2 or paate[1]!="txt":
            self.infoBox.update("ERROR: Invalid file name.")
            self.pauseGame=False
            return
        final_text='GAM111'
        
        gameTxt=self.game.saveGame()
        final_text+=gameTxt
        
        roundOn=str(int(self.roundOn))
        txt='RON001'+roundOn
        final_text+=txt
        
        gameOn=str(int(self.gameOn))
        txt='GON001'+gameOn
        final_text+=txt
        
        turnOn=str(int(self.turnOn))
        txt='TON001'+turnOn
        final_text+=txt
        
        firstInit=str(int(self.firstInit))
        txt='FIN001'+firstInit
        final_text+=txt
        
        hRaise=str(int(self.hRaise))
        txt='HRA001'+hRaise
        final_text+=txt
        
        playNext2=str(int(self.playNext2))
        txt='PN2001'+playNext2
        final_text+=txt
        
        playNext3=str(int(self.playNext3))
        txt='PN3001'+playNext3
        final_text+=txt
        
        hPut=str(int(self.hPut))
        txt='HPU001'+hPut
        final_text+=txt
        
        pauseGame=str(int(True))
        txt='PGA001'+pauseGame
        final_text+=txt
        
        putBoxChecked = str(int(self.putBoxChecked))
        txt='PBC001'+putBoxChecked
        final_text+=txt
        
        startHumanTurn = str(int(self.startHumanTurn))
        txt='SHT001'+startHumanTurn
        final_text+=txt
        
        player=''
        if self.player==None:
            player='9'
        else:
            player = str(int(self.game.getPlayers().index(self.player)))
        txt='SPL001'+player
        final_text+=txt
        
        
        sH = str(int(self.showHiddenCards))
        txt='SHC001'+sH
        final_text+=txt
        
        snr=str(int(self.waitForNewRoundStart))
        txt='SNR001'+snr
        final_text+=txt
        
        final_text+='END000'

        try:
            file=open(fname,'w')
            file.write(final_text)
            file.close()
        
            name=fname.split("/")
            if len(name)==0:
                name=fname
            else:
                name=name[len(name)-1]
            txt="Game saved successfully to "+name+"."
            self.infoBox.update(txt)
            self.pauseGame=False
            
        except IOError:
            txt="Error occured while saving the game."
            self.infoBox.update(txt)
            self.pauseGame=False
        
        
        