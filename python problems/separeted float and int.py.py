n=float(input())
if n==int(n):
    print("int",int(n))
else:
    print("float",int(n),n-int(n)) 

               ### factorial problem:::::::
import math
t=int(input())
for i in range(t):
    n=map(int,input().split())
    for j in n:
        print(math.factorial(j))
        
        
        ### GCD problem::::::::
        import math
        a,b=map(int,input().split())
        res=math.gcd(a,b)
        print(res)
    
