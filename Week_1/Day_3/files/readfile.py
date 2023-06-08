from collections import defaultdict

# f = open("C:\\Personal\\Code\\Data_Analytics\\Week_1\\Day_3\\files\\test.txt","r")
# f_out = open("C:\\Personal\\Code\\Data_Analytics\\Week_1\\Day_3\\files\\test_1.txt","w")

# for line in f:
#     tokens = line.split(' ')
#     print(tokens)
#     f_out.write("wordcount:"+ str(len(tokens))+line)
#     print(len(tokens))
# f.close()

# # with open("C:\\Personal\\Code\\Data_Analytics\\Week_1\\Day_3\\files\\test.txt","r")



# from collections import Counter

# # Read the contents of the poem.txt file
# with open('C:\\Personal\\Code\\Data_Analytics\\Week_1\\Day_3\\files\\poem.txt',"r") as file:
#     poem_text = file.read()

# # Tokenize the text into words
# words = poem_text.lower().split()

# # Count the occurrences of each word
# word_counts = Counter(words)

# # Find the maximum count
# max_count = max(word_counts.values())

# # Get the words with the maximum count
# max_words = [word for word, count in word_counts.items() if count == max_count]

# # Print the words with the maximum occurrence
# print("Words with maximum occurrence:")
# for word in max_words:
#     print(f"The words with maximum occurence is {word} , number of occurence is {max_count}")




# pe ratio = price / earnings per share
# price to book ratio = price / book value


# with open("C:\\Personal\\Code\\Data_Analytics\\Week_1\\Day_3\\files\\stocks.csv","r") as f, open("C:\\Personal\\Code\\Data_Analytics\\Week_1\\Day_3\\files\\output.csv","w") as g:
#   g.write("Company Name, PE Ratio, PB Ratio\n")
#   next(f)  # Skip the header line
#   for line in f:
#         tokens = line.split(",")
#         stock = tokens[0]
#         price = float(tokens[1])
#         eps = float(tokens[2])
#         book = float(tokens[3])
#         pe = round(price / eps, 2)
#         pb = round(price / book, 2)
#         g.write(f"{stock},{pe},{pb}\n")



