number = [1,2,3,4,5]
print("Original List: ",number)
for x in range(len(number)):
    squared = [x**2 for x in number]
print("List after squaring each element: ",squared)