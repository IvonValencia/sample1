func1 = lambda x,y : x*y
print(func1(5,6))

myList = [1,2,3,4,5]
func2 = lambda x: x*2
result = map(func2, myList)
print(list(result))