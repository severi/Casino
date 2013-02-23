from deck import Deck
from hand import Hand
from player import Player
from card import Card

class Game(object):
    MAXPOINTS = 16
    SPEED = 100
    
    def __init__(self):
        self.__players = []
        self.__board = Hand()
        self.__deck = Deck()
        self.nextInTurn = 0
        self.nextDealer = -1
        self.extraCardPoints=0
        self.extraSpadesPoints=0
        self.lastRaise=None
        
    def initForNewRound(self):
        self.__deck = Deck()
        for pl in self.__players:
            pl.setHand(self.deal(4))
            pl.clearStack()
            pl.clearCottages()
        self.lastRaise=None
        self.nextDealer += 1
        self.nextInTurn = self.nextDealer+1
        self.initBoard()
        
    def addPlayer(self,playerName, tyyppi):
        player = Player(playerName,tyyppi)
        self.__players.append(player)
    
    def addPlayer2(self,player):
        self.__players.append(player)
    
    def getPlayers(self):
        return self.__players
    
    def getNextInTurn(self):
        pl = self.__players[self.nextInTurn%len(self.__players)]
        self.nextInTurn+=1
        return pl
    
    def initBoard(self):
        cards = self.__deck.deal(4)
        self.__board.addCards(cards)
        
    def getBoard(self):
        return self.__board
        
    
    '''
    Checks if game is over/ someone has 16 or more points
    '''
    def gameOver(self):
        for player in self.__players:
            if player.getPoints()>=Game.MAXPOINTS:
                return True
        return False
        
    def deal(self,amount):
        return self.__deck.deal(amount)
    
    def nextInTurnType(self):
        return self.__players[self.nextInTurn%len(self.__players)].getType()
    
    def getDeck(self):
        return self.__deck
    
    '''
    returns boolean value determining if round should be continued i.e.  if cards are left on deck or on players hands
    '''
    def continueRound(self):
        if self.getDeck().cardsLeft()>0:
            return True
        for pl in self.getPlayers():
            if pl.hasCards():
                return True
        return False
    
    '''
    This function deals the card on board to the player who was the last one to raise cards
    '''
    def dealBoardToLatest(self):
        if len(self.getBoard().getCards())>0:
            try:
                self.lastRaise.addCardsToStack(self.getBoard().getCards())
                self.getBoard().clear()
            except AttributeError:
                self.getBoard().clear()
        
    '''
    THIS FUNCTION IS NOT USED ANYMORE FOR ANYTHING
    This function returns the minimum limit used in computerPlayerIO's chooseCardToTable function to determine the MIVALUE-limit
    '''            
    def getMinLimit(self):
        cards=[]
        c10=Card(10,Card.DIAMONDS)
        s2=Card(2,Card.SPADES)
        for pl in self.__players:
            cards.extend(pl.getStack().getCards())
        #cards.sort()
        am=[0]*13
        for c in cards:
            num=c.getHandValue()-2
            if c==c10:
                num=8 #10-2
            elif c==s2:
                num=0 #2-2
            am[num]+=1
            
        if c10 not in cards:
            return 16
        if s2 not in cards:
            return 15   
        for i in range(12,-1,-1):
            if am[i]!=4:
                return i+2
        return 16
    
    def getAllStackCardsFromPlayers(self):
        cards=[]
        for pl in self.__players:
            cards.extend(pl.getStack().getCards())
        return cards
    
    '''
    Window's saveGame method uses this method for saving the game
    '''
    def saveGame(self):
        final_text=''
        #players
        plrs=''
        for i in self.getPlayers():
            text=''
            text+='NAM'
            name=i.getName()
            pit=len(name)
            if pit<10:
                text+='00'
            elif pit<100:
                text+='0'
            text+=str(pit)
            text+=name
            
            text+='COT'
            cot=i.getCottages()
            if cot<10:
                text+='001'
            elif cot<100:
                text+='002'
            elif cot>100:
                text+='003'
            text+=str(cot)
            
            points=i.getPoints()
            text+='POI'
            if points<10:
                text+='001'
            elif points<100:
                text+='002'
            elif points>100:
                text+='003'
            text+=str(points)
            
            hand=i.getHand().getCards()
            am=len(hand)
            text+='HAN'
            text+='00'
            text+=str(am)
            for card in hand:
                text+=card.cardSave()
            
            text+='TYP'
            text+='001'
            typ=i.getType()
            text+=str(typ)
            
            stack=i.getStack().getCards()
            text+='STA'
            if len(stack)<10:
                text+='00'
            elif len(stack)<100:
                text+='0'
            text+=str(len(stack))
            for card in stack:
                text+=card.cardSave()
            text+='END001'
            
            text2='PLR'
            if len(text)<10:
                text2+='00'
            elif len(text)<100:
                text2+='0'
                
            text2+=str(len(text))
            text2+=text
            
            plrs+=text2
        final_text=plrs
        
        #board
        board=self.getBoard().getCards()
        txt='BOA'
        if len(board)<10:
            txt+='00'
        elif len(board)<100:
            txt+='0'
        txt+=str(len(board))
        for card in board:
            txt+=card.cardSave()
        
        final_text+=txt
        
        #deck
        deck=self.getDeck().getCards()
        txt='DEC'
        if len(deck)<10:
            txt+='00'
        elif len(deck)<100:
            txt+='0'
        txt+=str(len(deck))
        for card in deck:
            txt+=card.cardSave()
        
        final_text+=txt
        
        #nextInTurn
        txt='NTU001'+str(self.nextInTurn%len(self.__players))
        
        final_text+=txt
        
        #nextDealer
        txt='NDE001'+str(self.nextDealer%len(self.__players)%len(self.__players))
        
        final_text+=txt
        
        #extraCardPoints
        extraCardPoints=self.extraCardPoints
        txt='ECP'
        if extraCardPoints<10:
            txt+='001'
        elif extraCardPoints<100:
            txt+='002'
        else:
            txt+='003'
        txt+=str(extraCardPoints)
        
        final_text+=txt
        
        #extraSpadesPoints
        extraSpadesPoints=self.extraSpadesPoints
        txt='ESP'
        if extraSpadesPoints<10:
            txt+='001'
        elif extraSpadesPoints<100:
            txt+='002'
        else:
            txt+='003'
        txt+=str(extraSpadesPoints)
        final_text+=txt
        
        #lastRaise
        lastRaise=9
        txt='LRA001'
        if self.lastRaise!=None:
            lastRaise=self.__players.index(self.lastRaise)
            txt+=str(lastRaise%len(self.__players))
        else:
            txt+=str(lastRaise)
        final_text+=txt
        return final_text



