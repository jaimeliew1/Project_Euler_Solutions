# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
def isTri(n):
    return ((math.sqrt(1+8*n)-1)/2).is_integer()

def isSqr(n):
    return (math.sqrt(n)).is_integer()

def isPent(n):
    return ((1+math.sqrt(1+24*n))/6).is_integer()

def isHex(n):
    return ((1+math.sqrt(1+8*n))/4).is_integer()

def isHept(n):
    return ((3+math.sqrt(9+40*n))/10).is_integer()

def isOct(n):
    return ((2+math.sqrt(4+12*n))/6).is_integer()

isPoly = [isTri, isSqr, isPent, isHex,isHept,isOct]


class Jnum:
    id = 0 #each nth bit is 1 if it is an nGon number
    n = 0
    isMultiPoly = False
    def __init__(self, num):
        self.n = num
        for i in (f(num) for f in isPoly):
            self.id = (self.id << 1) | i
        if bin(self.id).count('1') > 1:
            self.isMultiPoly = True

    def __eq__(self,other):
        return self.n == other.n

    def __ne__(self,other):
        return self.n != other.n

def checkThisSet(thisSet,depth,maxDepth):
    for q in (q for q in numSet if q  not in thisSet):
        workingBit = 0
        qIsCandidate = True
        if str(thisSet[-1].n)[2:] == str(q.n)[:2]: #if cyclical
            workingBit = 0
            for i in (thisSet + [q]):
                if workingBit & (i.id) == 0:
                    workingBit |= (i.id)
                else:
                    qIsCandidate = False

                    break
        else:
            qIsCandidate = False

        if qIsCandidate:
            if depth == maxDepth-1:
                if str(thisSet[0].n)[:2] == str(q.n)[2:]: #if cyclical back to start

                    return list(thisSet + [q])
                else:
                    return [Jnum(0)]
            furtherTesting = checkThisSet(list(thisSet + [q]),depth +1, maxDepth)
            if furtherTesting != [Jnum(0)]:
                return furtherTesting

    return [Jnum(0)]

def run():
    ### generate set of possible candidates
    numSet = []
    for i in range(1000, 10000):
        a = Jnum(i)
        if a.id != 0:
            if a.isMultiPoly:
                temp = a
                for k, bit in enumerate(bin(a.id)[2:].zfill(6)[::-1]):
                    if bit == '1':
                        temp.id = 1<<k
                        numSet.append(Jnum(a.n))
                        numSet[-1].id = 1<<k


            else:
                numSet.append(a)

    #print("there are ",len(numSet)," candidate numbers.\n")

    ### Recursive search loop
    for i in numSet:
        currentSet = checkThisSet(list([i]), 1, 6)
        if currentSet != [Jnum(0)]:
            break

    Sum = 0
    for i in currentSet:
        #print(i.n, bin(i.id)[2:].zfill(6))
        Sum += i.n

    return Sum


if __name__ == "__main__":
    print(run())

