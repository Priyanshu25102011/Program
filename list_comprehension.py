List = [1,2,3,4,5,6,7,8,9,10]
print("The original list is : ", str(List))
even_square = [i*i for i in List if i%2==0]
print("The square of the even numbers in the list is:",str(even_square))