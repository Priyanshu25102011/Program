test_dict = {'Codingal': 2, 'is':2, 'best': 2, 'for': 2, 'coding' : 1}
print("The original dictionary is : " + str(test_dict))
K=2
res=0
for key in test_dict:
    if test_dict[key]==K:
        res = res + 1
print("Frequence of K is:" + str(res))