# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# count=0
# for x in result:
#     if x == "heads":
#         count+=1 

# print(count)
        
       
# #solution 2
# for x in range(1,11):
#     if x%2==1:
#         y = x**2
#         print("The square of all numbers between 1 to 10 except even numbers is", y)

# #solution 3
# expense_list = [2340, 2500, 2100, 3100, 2980]
# monthList = ["jan","feb","march","april", "may"]
# count = 0
# userExpenseInput = int(input("Enter the expense amount: "))
# for x in expense_list:
#     if userExpenseInput == x:
#         print("The month that expensed occured is : ", monthList[count])
#         break
#     count +=1

# else:
#         print("Expense is not found.")


#solution 4
# for i in range(5):
#     print(f"You ran {i+1} miles") # i starts with zero hence adding 1
#     tired = input("Are you tired? ")
#     if tired == 'yes':
#         break

# if i == 4: # 4 because the index starts from 0
#     print("Hurray! You are a rock star! You just finished 5 km race!")
# else:
#     print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")
         

#solution 5

# for i in range(1,6):
#     s = ''
#     for j in range(i):
#         s += '*'
#     print(s)

for i in range(1,6): #1,2,3,4,5,
   for j in range(i):
       print(i,j)

x = range(6)

for n in x:
   for j in range(n):
      print{j}
  