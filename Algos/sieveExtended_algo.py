import math 
prime = [] 

def simpleSieve(limit): 
	
	mark = [True for i in range(limit + 1)] 
	p = 2
	while (p * p <= limit): 
		
		if (mark[p] == True): 
			
			for i in range(p * p, limit + 1, p): 
				mark[i] = False
		p += 1
		
	for p in range(2, limit): 
		if mark[p]: 
			prime.append(p) 
			print(p,end = " ") 
			
def segmentedSieve(n): 
	
	limit = int(math.floor(math.sqrt(n)) + 1) 
	simpleSieve(limit) 
	
	low = limit 
	high = limit * 2
	
	while low < n: 
		if high >= n: 
			high = n 
			
		mark = [True for i in range(limit + 1)] 
		
		for i in range(len(prime)): 
			
			loLim = int(math.floor(low / prime[i]) *
										prime[i]) 
			if loLim < low: 
				loLim += prime[i] 
				
			for j in range(loLim, high, prime[i]): 
				mark[j - low] = False
				
		for i in range(low, high): 
			if mark[i - low]: 
				print(i, end = " ") 
				
		low = low + limit 
		high = high + limit 
def main():
    n = int(input())
    print("Primes smaller than", n, ":") 
    segmentedSieve(100) 

if __name__ == "__main__":
    main()
