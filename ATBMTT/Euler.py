def eulerPrime(n):
    a = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d not in a:
                a[d] = 1
            else:
                a[d] += 1
            n //= d
        d += 1

    res = 1
    for k, v in a.items():
        res *= pow(k, v) - pow(k, v-1)
    return res

if __name__ == '__main__':
    print(eulerPrime(220))