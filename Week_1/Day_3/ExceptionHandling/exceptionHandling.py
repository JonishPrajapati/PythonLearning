# x=input("Enter a number1: ")
# y = input("Enter a number2: ")
# try:
#     z = int(x)/int(y)
# except ZeroDivisionError as e:
#     print("Zero Division occured", type(e).__name__)
#     z = None
# except Exception as e:
#     print("Type error exception ", type(e).__name__)
#     z=None
# print("Division is: ", z)

#exception => general
#zero division => specific



# x = ["arr","barr", "carr"]
# try:
#     for i in range(4):
#       print(i,x[i])
# except IndexError as e:
#     print("Error occured", type(e).__name__)

# def checkAssert(num):
#    assert(num <0)
#    return num**0.5

# print(checkAssert(5))
# print(checkAssert(-5))



# try:  
#    x = input("enter number 1: ")
#    y = input("enter number 2: ") 
#    z = int(x)/int(y)
#    print(z)
# # this block will handle the exception raised  
# except ZeroDivisionError:  
#     print( "Attempting to divide by zero" ) 
# except ValueError as e:  
#     print( "Attempting to supply string instead of integer", type(e).__name__ ) 
# except:  
#     print( "error 2",__name__ )  
# # this will always be executed no matter exception is raised or not  

x=1
assert x==2, "x should be 1"
 