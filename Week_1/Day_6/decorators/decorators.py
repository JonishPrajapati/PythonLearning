# import time
# def timeCheck(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__ + "took" + str((end-start)*1000) + "mil sec")
#         return result
#     return wrapper

# @timeCheck
# def calculateSquare(num):
#     result=[]
#     for number in num:
#         result.append(number**2)
#     return result

# @timeCheck
# def calculateCube(num):
#     result=[]
#     for number in num:
#         result.append(number*number*number)
#     return result


# array = range(1,100000)
# calculateSquare = calculateSquare(array)
# calculateCube = calculateCube(array)

def check(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not a non-negative integer")

    return helper

@check
def factorial(n):
      if n == 1:
        return 1
      else:
        return n * factorial(n - 1)


for i in range(1, 10):
    print(i, factorial(i))

try:
    print(factorial(-1))
except Exception as e:
    print("negative")

try:
    print(factorial(1.354))
except Exception as e:
    print("e")
    