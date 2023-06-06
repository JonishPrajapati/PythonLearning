#solution 1
'''
Nepal = ["kathmandu", "bhaktapur", "lalitpur", "banepa"]
Pakistan = ["lahore","karachi","islamabad"]
Bangladesh = ["dhaka", "khulna", "rangpur"]

cityName = input("Enter a city name: ")
for i, x in enumerate(Nepal):
    if x == cityName:
        newIndex = i
        print(f"the city lies at {newIndex} position and belongs to Nepal")
        break
for j, y in enumerate(Pakistan):
    if y == cityName:
        newIndex = j
        print(f"the city lies at {newIndex} position and belongs to Pakistan")
        break
for k, z in enumerate(Bangladesh):
    if z == cityName:
        newIndex = k
        print(f"the city lies at {newIndex} position and belongs to Bangladesh")
        break

else:
    print("No city available")

'''

#solution 2
'''
Nepal = ["kathmandu", "bhaktapur", "lalitpur", "banepa"]
Pakistan = ["lahore","karachi","islamabad"]
Bangladesh = ["dhaka", "khulna", "rangpur"]

cityName = input("Enter a city name: ")
cityName1 = input("Enter an another city name: ")


if cityName in Nepal and cityName1 in Nepal:
        print(f" both city belongs to Nepal")
elif cityName in Pakistan and cityName1 in Pakistan:
        print(f"both belongs to Pakistan")
elif cityName in Bangladesh and cityName1 in Bangladesh:
        print(f"both belongs to Bangladesh")
else:
        print("They don't belong to the same country.")
'''

#solution 2

user = int(input("Enter the sugar level: "))
if user < 80:
    print("Your sugar level is low.")
elif user>100:
    print("Your sugar level is high.")
else:
    print("Your sugar level is normal.")
