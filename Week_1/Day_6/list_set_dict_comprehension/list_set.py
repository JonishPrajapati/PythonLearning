# x = [1,2,3,4,5,6,7,8]

# y = [i for i in x if i%2==0]

# print(y)

# sql_numbers = [i*i for i in x]
# print(sql_numbers)


# s = set([1,2,3,4,5,1,2])
# print(s)

# z = {i for i in s if i%2==0 }
# print(z)


# city =["Kathmandu", "London", "Kansas"]
# country = ["Nepal","England", "USA"]

# d={cities:countries for cities,countries in zip(city, country)} 
# print(d)


# e = [(i,j) for i in range(4) for j in range(4)]
# print(e)

# numbers=[0,1,2,3,4,5,6,7,8,9]
# f = ["even" if i %2==0 else "odd" for i in numbers]
# print(f)

# g = [[(i*j) for i in range(4)] for j in range(4)]
# print(g)


integer = [0,1,2,3,4]
binary = ["0","1","10","11","100"]
#binary_dict = {0:"0",1:"1",2:"10",3:"11",4:"100"}


x = {i:j for i,j in zip(integer,binary)}
print(x)


integer = [1, -1, 2, 3, 5, 0, -7]
#additive_inverse = [-1, 1, -2, -3, -5, 0, 7]

#list
additive_inverse = [-num for num in integer]
print("list", additive_inverse)

#set
additive_inverse = {-num for num in integer}
print("set",additive_inverse)

#dictionary
additive_inverse = {num:-num for num in integer}
print("dict", additive_inverse)


#list
integer = [1,-1,2,-2,3,-3]
x = [i**2 for i in integer if i % 2 == 0]
print("lists: ",x)

#set
x = {z**2 for z in integer}
print("sets: ", x)

#dictionary
x = {y:y**2 for y in integer }
print("dictionary: ", x)

# List
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1*i for i in integer]
print("a+i=0",additive_inverse)