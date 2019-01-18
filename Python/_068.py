import itertools


def makeGons(combSet, depth=1, rem=[], x=[], finalLinks={}):
#iterative function that assembles the n-gon. Assumes all elements in
#combset have equal sums and have enough elements to complete an n-gon

    if depth == 1: #First iteration
        theAns = []
        for startLink in combSet:
            rem = set(x for x in numSet if x not in startLink)
            for a in startLink:
                ans = makeGons(combSet, depth+1, rem.union([a]),
                               [startLink],set(startLink).difference([a]))
                if ans != 0:
                    theAns.append(ans)
        return theAns
#list(set(b).intersection(a))==a
    elif 1 <= depth < n:
        for nextLink in (comb for comb in combSet if len(rem.intersection(comb))==3):
            for a in nextLink:
                currentRem = rem.difference(nextLink).union([a])
                return makeGons(combSet,depth+1,currentRem,x+[nextLink],finalLinks)

    elif depth == n:

        for final in finalLinks:

            for nextLink in (comb for comb in combSet if len(rem.union([final]).intersection(comb))==3):
                return x+[nextLink]


    return 0

def run():
    n = 5
    numSet = list(x for x in range(1,n*2+1))
    totalCombSet = list(itertools.combinations(numSet,3))
    ConcDigs = []
    #iterate through all possible sums
    for S in range(1+2+3,6*n-3+1): #min and max possible sum values

        #get set of combinations which add up to current sum S
        combSet = []
        for comb in (x for x in totalCombSet if sum(x) == S):
            combSet.append(comb)


        #discard sets with less than n members
        if len(combSet) < n:
            continue
        #print(combSet)
        ans = makeGons(combSet)
        #print(S)
        for Set in ans:
            thisSet = []
            minArm = -1
            Min = 99999
            #rearrange each arm
            #(external, middle, next)
            for i, arm in enumerate(Set):
                thisSet.append([0,0,0])
                for node in arm:
                    if node not in Set[i-1] and node not in Set[(i+1)%n]: #external
                        thisSet[i][0] = node
                    elif node in Set[i-1]:
                        thisSet[i][1] = node
                    elif node in Set[(i+1)%n]:
                        thisSet[i][2] = node

                if thisSet[i][0] < Min:
                    Min = thisSet[i][0]
                    minArm = i

            curString = ''
            #print(thisSet)
            for i in map(lambda x: (x+minArm)%n,range(0,n)):
                for node in thisSet[i]:
                    curString += str(node)
            if len(curString) == 16:
                ConcDigs.append(curString)

    maxStr = int(ConcDigs[0])
    for string in ConcDigs:
        if int(string) > maxStr:
            maxStr = int(string)
    return 'THIS IS WRONG'
    return maxStr

if __name__ == '__main__':
    print(run())




