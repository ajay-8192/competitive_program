def sieve(m, n):
    if m <= 1:
        m = 2
    prime = [True for i in range(n+1)]
    p = 2
    while( p*p <= n ):
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return [i for i in range(m,n+1) if prime[i]]
def main():
    m, n = map(int,input("Enter range: ").split())
    l = sieve(m, n)
    print(l)
if __name__ == "__main__":
    main()
