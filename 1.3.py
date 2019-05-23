while (1):
    print('Enter a number:')
    n = int(input())
    if n == 0:
        break
    #finding a massive of multipliers
    i = 2
    primes = []
    while i * i <= n:
        while n % i == 0:
            primes.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primes.append(n)
    #out
    out = []
    for i in range(len(primes)):
        if (primes[i] in out) == False:
            out.append(primes[i])
    if len(primes) <= 1: print(1, '*', n) #if number is prime
    else:
        for i in range(len(out)):
            if primes.count(out[i]) == 1:
                print(int(out[i]), end=' ')
                if (i != (len(out) - 1)): print('*', end=' ')
            else:
                print(int(out[i]), '^', primes.count(out[i]), sep='', end=' ')
                if (i != (len(out) - 1)): print('*', end=' ')
    print()
