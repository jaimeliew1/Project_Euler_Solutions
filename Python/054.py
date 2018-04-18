# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


from collections import Counter
suits = ('H','C','S','D')
values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
hands = {'HC':100,'P':200,'TP':300,'TOK':400,'ST':500,'FL':600,'FH':700,'FOK':800,'SF':900}

def playerHand(a): #first digit is hand rank. second two are rankings of hand
    asuits = Counter()
    hand = 0
    for i in {1, 4, 7, 10, 13}: # is there a flush?
        asuits[a[i]] += 1
    if asuits.most_common(1)[0][1] == 5:
        hand = hands['FL'] #Flush

    aVals = []
    for i in {0,3,6,9,12}: #is straight?
        aVals.append(values[a[i]])
    aVals.sort()
    #difference between each card in ordered hand
    diffList = list(aVals[i]-aVals[i-1] for i in range(0,5))[1:]
    if diffList == [1,1,1,1]:
        if hand == hands['FL']:
            hand = hands['SF'] + aVals[-1] #Straight flush
        else:
            hand = hands['ST'] + aVals[-1]#Straight
    if hand != 0:
        return hand
    aCnt = Counter()
    for i in aVals:
        aCnt[i] += 1
    aPair = aCnt.most_common(2)
    if aPair[1][1] == 2 and aPair[0][1] == 3:
        hand = hands['FH'] + aPair[0][0] #Full House

    elif aPair[1][1] == aPair[0][1] == 2:
        hand = hands['TP'] + aVals[3] #Two Pair

    elif aPair[0][1] == 1:
        hand = hands['HC'] + aVals[4] #high card

    elif aPair[0][1] == 2:
        hand = hands['P'] + aPair[0][0] #Pair


    elif aPair[0][1] == 3:
        hand = hands['TOK'] + aPair[0][0] #Three of Kind


    elif aPair[0][1] == 4:
        hand = hands['FOK'] + aPair[0][0] #four of Kind

    return hand


def run():

    f = open('Data/p054_poker.txt')
    wins = 0
    for i, game in enumerate(f):
        hand1 = game[:14]
        hand2 = game[15:]
        if playerHand(hand1) > playerHand(hand2):
            wins += 1
    f.close()

    return wins


if __name__ == "__main__":
    print(run())

