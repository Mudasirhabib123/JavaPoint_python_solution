arr=[34,54,32,12,34,56,67,78]

for i in range(len(arr)):
        for j in range(len(arr)-1):
                if(arr[i]<arr[j+1]):
                        temp=arr[i]
                        arr[i]=arr[j]
                        arr[j]=temp
print(arr)





