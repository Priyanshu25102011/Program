L = [4,5,1,2,9,7,10,8]
print("Original List: ",L)
count = 0
for i in L:
    count += 1
avg = count/len(L)
print("sum =",count)
print("Average =",avg)
L.sort()
print("Smallest Element is:",L[0])
print("Largest Element is:",L[-1])