#formula area = (1/2)*base*height

# def calculateTriange(x,y):
#     areaOfTriangle = 0.5 * x * y
#     print(areaOfTriangle)
    

# a = 12
# b =33
# calculateTriange(a,b)


# def calculateArea(x,y,shareType):
#     if shareType == "Triangle":
#         areaOfTriangle = 0.5 * x * y
#         print(areaOfTriangle)
#     elif shareType == "Rectangle":
#         areaOfRectangle = x*y
#         print(areaOfRectangle)
#     else:
#          areaOfTriangle = 0.5 * x * y
#          print(areaOfTriangle)


# a = 10
# b =10
# calculateArea(a,b,"")

#solution 3
def print_pattern(n):
    s=''
    for i in range(n):
        for x in range(i):
            s+="*"
            print(s)


print_pattern(4)
