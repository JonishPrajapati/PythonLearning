
prices = [2200,2350,2600,2130,2190]
febExpenses = prices[1]
janExpenses = prices[0]
x = janExpenses-febExpenses

print(f"{x}$ is spent extra compare to january. ")
print("The total expense in first quarter of the year is: ", prices[0] + prices[1] + prices[2])
for y in prices:
    if(y == 2000):
        print("You spent $2000 in this month: ", y+1)
        break
else:
        print("No dollars spent.")


prices.append(1980)
print("The new expenses", prices)


prices[3] = prices[3]-200
print("the new prices", prices)


#solution 2
heros=['spider man','thor','hulk','iron man','captain america']
print("The length of the list is ", len(heros))
heros.append("black panther")
print(heros)

heros.insert(3,"black panther")
print(heros)
heros[1:3] = ['doctor strange']
heros.sort()
print(heros)