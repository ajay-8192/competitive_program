import random
def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y>>1 # y = y/2
        x = (x * x) % p
    return res
def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False
def isPrime( n, k):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1; 
    while (d % 2 == 0):
        d //= 2

    for i in range(k):
        if (miillerTest(d, n) == False):
            return False

    return True

##bool isPrime(int n, int k)
##1) Handle base cases for n < 3
##2) If n is even, return false.
##3) Find an odd number d such that n-1 can be written as d*2r. 
##   Note that since n is odd, (n-1) must be even and r must be 
##   greater than 0.
##4) Do following k times
##     if (millerTest(n, d) == false)
##          return false
##5) Return true.
##
##// This function is called for all k trials. It returns 
##// false if n is composite and returns true if n is probably
##// prime.  
##// d is an odd number such that  d*2r = n-1 for some r >= 1
##bool millerTest(int n, int d)
##1) Pick a random number 'a' in range [2, n-2]
##2) Compute: x = pow(a, d) % n
##3) If x == 1 or x == n-1, return true.
##
##// Below loop mainly runs 'r-1' times.
##4) Do following while d doesn't become n-1.
##     a) x = (x*x) % n.
##     b) If (x == 1) return false.
##     c) If (x == n-1) return true. 






k = 4; 
def main():
    print("All primes smaller than 100: "); 
    for n in range(1,100):
        if (isPrime(n, k)):
            print(n , end=" ") 
if __name__ == "__main__":
    main()
