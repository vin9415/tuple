#ordered(wherever the element is,tuple will fix)
#immuatble
#() use
#it allows the  duplicate values(like two red ,threegreen etc)
my_tuple=("red","orange","green")
print(my_tuple)
print(len(my_tuple))
mytuple=("apple",)#if there is one element in tuple and we remove the comma then its not printing like tuple.


print(mytuple)
print(my_tuple[1])

Tuple=("yaahh","theee","yhhhh")
mylist=list(Tuple)
mylist.append("huuu")
Tuple=tuple(mylist)
print(Tuple)