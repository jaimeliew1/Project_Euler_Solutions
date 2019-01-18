from EulerFunctions import factors, timeit


@timeit
def run():
    Nmax = int(1e6)
    factsum = {n:sum(factors(n))-n for n in range(2, Nmax + 1)}

    best_L, best_chain = 0, []
    for n in range(2, Nmax + 1):
        chain = [n]
        i = n
        while 1 < i <= Nmax:

            i = factsum[i]
            if i in chain:
                if factsum[chain[-1]] == chain[0]:
                    if len(chain) > best_L:
                        best_L, best_chain = len(chain), chain
                break
            chain.append(i)

    print(best_chain)
    print(min(best_chain))




if __name__ == '__main__':
    run()
