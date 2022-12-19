#### summation of index's in an Array.-----------------

n=int(input())                             # lenthe of the array  = 4
arr=list(map(int,input().split()))         # taking index's of an array as input = 7 3 2 1
sum=0


for i in range(len(arr)):                  # my loop will work between the lenth of the array (index[0] - len(array)) = 4
    sum=sum+arr[i]                         # every time index will add up with the next index
    arr[i]+=1
print(abs(sum))
    
