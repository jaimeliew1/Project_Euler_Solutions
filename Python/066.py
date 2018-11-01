import math


def sqrtContFracGen(S):
    #x=[m,d,a]
    x=[[0,1,int(math.floor(math.sqrt(S)))]]
    #if S is square, there is no continued fraction. return zeros
    if x[0][2]**2 == S:
        while True:
            yield 0

    while True:
        temp = [(x[-1][1]*x[-1][2]-x[-1][0])]
        temp.append((S-temp[0]**2)/x[-1][1])
        if temp[1] == 0:
            return 0,0
        temp.append(int(math.floor((x[0][2]+temp[0])/temp[1])))

        if temp not in x:
            x.append(temp)

        else: #if the sequence is about to repeat
            a = []
            for i in x:
                a.append(i[2])
            period = len(x)-x.index(temp)

            #split the non-repeating and repeating part of sequence
            a = [a[:len(a)-period],a[len(a)-period:]]
            break

    #generate the sequence
    for i in a[0]:
        yield i

    i = 0
    while True:
        yield a[1][i]
        i =(i+1)%period


def run():
    limit = 1000

    #Find the smallest integer solution (x,y) for a range of d's in x^2-d*y^2 = 1
    maxX = 0

    for i in range(2,limit+1):
        if math.sqrt(i).is_integer():
            continue

        #generate an increasingly accurate continued fraction. the solution is
        #in this space
        gen = sqrtContFracGen(i)
        cur = next(gen)
        A0 = 1
        A1 = cur #numerator

        B0 = 0
        B1 = 1 #denominator
        while A1*A1 - i*B1*B1 != 1:
            cur = next(gen)
            A1,A0 = cur*A1+A0,A1
            B1,B0 = cur*B1+B0,B1

        if A1 > maxX:
            maxX = A1
            ans = i
            #print(i,maxX,B1)
    return ans

if __name__ == '__main__':
    print(run())




