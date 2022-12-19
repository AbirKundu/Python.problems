------------------------------------------------------------------#### summation of index's in an Array.-----------------

n=int(input())                             # lenthe of the array  = 4
arr=list(map(int,input().split()))         # taking index's of an array as input = 7 3 2 1
sum=0


for i in range(len(arr)):                  # my loop will work between the lenth of the array (index[0] - len(array)) = 4
    sum=sum+arr[i]                         # every time index will add up with the next index
    arr[i]+=1
print(abs(sum))
    
                                   
------------------------------------------------------------------ #### Searching specific index in an array.-----------------
            
            

n=int(input())                       # # lenthe of the array  = 4
arr=list(map(int,input().split()))   ## taking index's of an array as input = 7 3 2 1
j=int(input())                       # specific index what is to find out its position. 

if n==len(arr) and j in arr :        # if my LENth of array is equal to my array " and specific index is in my array then the loop will find out j's position 
    pos=arr.index(j)                 # finding position declaerd pos variable. index() function will find position of my j
    print(pos)
else:
    print(-1)                        # if j = 5 which is not in my array it will print -1
    
    
--------------------------------------------------#### Replace index with a certain number in array####-------------------------------
# replce positive number with 1 nd replace negative number with 2

n=int(input())                       # # lenthe of the array  = 5
arr=list(map(int,input().split()))   ## taking index's of an array as input = 1 -2 0 3 4
for i in range(n):
    if arr[i]>0:
        arr[i]=1
    elif arr[i]<0:
        arr[i]=2
print(* arr)                        ## OUTPUT = 1 2 0 1 1        


----------------------------------------------##
