list=[1,2,3,4,5,6,7,8,9]
list2=[None]*len(list)
'''for i in range(len(list)):
	list[i],list[i-i-(i-1)]=list[i-i-(i-1)],list[i]

print(list)
'''
v=len(list)
v=v-v-v
for i in range(len(list)):
	list2[i]=list[0-(i+1)]


print(list2)
