from card import Card
from gameLogic import *
from player import Player
from game import Game
from deck import Deck

'''
checks if combined groups have unique cards
param: combination of cardGroups
return: True, if cards are not unique, False otherwise
[d2 d3][d2 s3]->true
[d2 d3][s2 s3]->false
'''
def hasSameCards(cardGroupComb):                #[s1 s2 r1][s3 b1][s4]
    
    for i in range(len(cardGroupComb)):         #[s1 s2 e1]
        if i+1>=len(cardGroupComb):
            return False
        for j in range(i+1,len(cardGroupComb)):   #[s3 b1][s4]
            for card in cardGroupComb[i]:       #s1 s2 r1
                if card in cardGroupComb[j]:    #s1 vs s3 b1
                    return True
    return False

'''
makes combinations of groups of cards. All cards in a combination are unique.
param: list of card groups, that are possible to pick from board
return: list of combined card groups. 
Each group of cards in the combination have unique cards
example:
groups: [s1 s5] [s6] [s1 d5]

poss:   [(s1 s5)(s6)] 
        [(s1 d5)(s6)]
        [(s1 s5)]
        [(s6)]
        [(s1 d5)]
'''
def combineGroups(groups):
    poss = []
    for i in range(1,len(groups)+1):
        comb=combinations(groups,i)
        
        for j in comb: #comb: ([s2 s3][s5]) ([s2 s3])([s5])
            if not hasSameCards(j):
                poss.append(j)
                
    return poss

'''
param: cards in players hand, cards on the board
return: dictionary, cards in players hand as key, and a list of possible groups of cards as value
for example:
    cards on board s1 s5 s6 d5 d11 d12
    raise Card d6
    key: d6
    value:  [(s1 s5)(s6)] 
            [(s1 d5)(s6)]
            [(s1 s5)]
            [(s6)]
            [(s1 d5)]
'''

def getPossibleCombos(cardsInHand,cardsOnBoard):
    possibilities = {}
    
    for raiseCard in cardsInHand:
        groups = getValidGroups1(raiseCard.getHandValue(),cardsOnBoard)
        groupCombos = combineGroups(groups)
        gclist=[]      
            
        for gr in groupCombos:
            comboAsList=[]
            for gr1 in gr:  #[(s1 s5)(s6)]
                for card in gr1:    #(s1 s5)
                    comboAsList.append(card)    #s1,s5,s6
            gclist.append(comboAsList)  #[[s1 s5 s6]]
        possibilities[raiseCard]=gclist
    
    return possibilities

'''
returns value used to rate possible raiseHands for computer player
'''
def getValue(group,raiseCard):
    value=0.0
    for card in group:
        value+=card.getCompValue()
    value+=raiseCard.getCompValue()
    return value

'''
This function is used to determine the card to put on the table for computer player
putCard has 2 criterias:
1. the first thing that is checked is the compValue of the card
2. if the two cards have the same compValue,  the card that makes the board harder to raise as once is put to board
'''
def chooseCardToTable(cards,board,game):
    val=-1
    rcard=-1
    boardVal=0
    for c in board:
        boardVal+=c.getBoardValue()
    posC=[]
    for card in cards:
        if val==-1 or card.getCompValue()<val:
            val=card.getCompValue()
            rcard=card
        
        elif card.getCompValue()==val:
            oldCards=[]
            newCards=[]
            oldCards.extend(board)
            newCards.extend(board)
            oldCards.append(rcard)
            newCards.append(card)
            
            testDeck=Deck()
            stackedCards=game.getAllStackCardsFromPlayers()
            availableCards=testDeck.getCards()
            
            for card1 in stackedCards:
                if card1 in availableCards:
                    availableCards.remove(card1)
            
            #number of cards left in deck/players hands that can raise the whole board at once
            validRaiseLkmOld=0
            validRaiseLkmNew=0
            for card1 in availableCards:
                if validRaise(card1,oldCards):
                    validRaiseLkmOld+=1
                if validRaise(card1,newCards):
                    validRaiseLkmNew+=1
                
            if validRaiseLkmOld > validRaiseLkmNew:
                rcard=card

    return rcard
    
'''
returns the best raiseCombo for computer player
cardsToRaise has 3 criterias:
1. the first thing that is checked is the compValue of the cards (the bigger the better)
2. if the two groups have the same compValue,  the group that makes the remaining board harder to raise as once is chosen
3. if there are no possible groups to raise, a card from players hand is put to board (function above)
'''
def getBestPick(comb,board,game):
    groupsFound=False
    rcard=-1
    points=0.0
    cards=[]
    cardsOnHand=[]
    for raiseCard in comb:
        cardsOnHand.append(raiseCard)
        for group in comb[raiseCard]:
            if getValue(group,raiseCard)>points:
                groupsFound=True
                rcard=raiseCard
                cards=group
                points=getValue(group,raiseCard)
                
            elif getValue(group,raiseCard)==points:
                oldCards=[]
                newCards=[]
                for c in board:
                    if c not in cards:
                        oldCards.append(c)
                for c in board:
                    if c not in group:
                        newCards.append(c)
                
                testDeck=Deck()
                stackedCards=game.getAllStackCardsFromPlayers()
                availableCards=testDeck.getCards()
                for card1 in stackedCards:
                    if card1 in availableCards:
                        availableCards.remove(card1)
                
                
                #number of cards left in deck/players hands that can raise the whole board at once
                validRaiseLkmOld=0
                validRaiseLkmNew=0
                for card1 in availableCards:
                    if validRaise(card1,oldCards):
                        validRaiseLkmOld+=1
                    if validRaise(card1,newCards):
                        validRaiseLkmNew+=1
                
                if validRaiseLkmOld > validRaiseLkmNew:
                    groupsFound=True
                    rcard=raiseCard
                    cards=group
                    points=getValue(group,raiseCard)

    if groupsFound==False:
        rcard=chooseCardToTable(cardsOnHand,board,game)
    return groupsFound,rcard,cards

def playComputerTurn(player,game):
    cardsInHand = player.getHand().getCards()
    cardsOnBoard = game.getBoard().getCards()
    comb = getPossibleCombos(cardsInHand,cardsOnBoard)
    found,rcard,cards = getBestPick(comb,cardsOnBoard,game)
    if found:
        return True,rcard,cards
    else:
        return False,rcard,cards


    
    