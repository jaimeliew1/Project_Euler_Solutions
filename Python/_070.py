import time

def totient(N):
    #returns list of totient function values for n in  2 < n < N
    tots = list(range(N))
    tots[1] = 0
    for i, tot in enumerate(tots):
        if i == 0:
            continue
        if i == tot: #if i is prime
            for n in range(i, N, i):
                tots[n] *= (i-1)
                tots[n] /=  i
    tots[1] = 1
    return tots[1:]


def isPerm(a,b):
    aa = str(a)
    bb = str(b)
    if len(aa) != len(bb):
        return False

    return sorted(aa) == sorted(bb)




start = time.time()


N = 10**7
ans = [999,0]
tots = totient(N)

for i, tot in enumerate(tots):
    if i == 0: continue
    if isPerm(i+1,tot) and float(i+1)/tot < ans[0]:
        ans = [float(i+1)/tot, i+1, tot]



print('n = {} such that n/phi(n) is minimum. {:0.5f}s'.format(ans[2],time.time()-start))