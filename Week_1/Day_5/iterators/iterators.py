# class RemoteControl():
#     def __init__(self):
#         self.channels = ["HBO","CNN","KANTIPUR","HIMALAYAN"]
#         self.index = -1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.index+=1
#         if self.index == len(self.channels):
#             raise StopIteration
        
#         return self.channels[self.index]
    
# r = RemoteControl()
# itr = iter(r)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


# class Fibonacci:
#     def __init__(self,limit):
#         self.previous = 0
#         self.current=1
#         self.n=0
#         self.limit = limit

    
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n < self.limit:
#             result = self.previous + self.current
#             self.previous = self.current
#             self.current = result
#             self.n += 1
#             return result
#         else:
#             raise StopIteration


# itr = iter(Fibonacci(5))
# while True:
#     try:
#         print(next(itr))
#     except StopIteration:
#         break




class CalculateFibonacciSeries():
    def __init__(self,n):
        self.previous=0
        self.current = 1
        self.n =n
    
    def CalculationPart(self):
        if self.n >= 0:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n -= 1
            return result
        else:
            return None
   

x = CalculateFibonacciSeries(7)
while True:
       next_number = x.CalculationPart()
       if next_number is None:
         break
       print(next_number)