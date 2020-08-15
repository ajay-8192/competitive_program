def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
def main():
    a,b = map(int,input().split())
    k = gcd(a,b)
    print(k)
if __name__ == "__main__":
    main()
