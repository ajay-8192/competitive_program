def gcd(a,b):
    if a == 0:
        return b,0,1
    g,x1,y1 = gcd(b%a,a)
    x = y1 - (b//a)*x1
    y = x1
    return g,x,y
def main():
    a,b = map(int,input().split())
    g,x,y = gcd(a,b)
    print(g,x,y)
if __name__ == "__main__":
    main()
