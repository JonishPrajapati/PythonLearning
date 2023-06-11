basket = {"orange","apple","mango","apple","orange","apple","orange"}
print(type(basket))

# numbers ={1,2,3,2,3,4}
# print(numbers)
# x = frozenset(numbers)
# x.add(8)
# print(x)

x = {"a","b","c"}
y = {"a","e","f","a","b","c"}

print(x|y) #union
print(x&y) #intersection
print(x-y)
print(x<y) #checking subset


setname = {"jonish","sabina","rahul", "rohini"}
x = frozenset(setname)
print(x)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1-set2) #shows the output that is only in set1
print(set2-set1) #shows the output that is only in set2

