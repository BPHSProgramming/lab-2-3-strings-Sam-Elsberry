#format2.3-sam-elsberry-25

flname = input("Enter your first and last name with a single space separating the two. Do not add leading or trailing characters or spaces: ")

#Use string slicing with find
space_index = flname.find(' ')
fname = flname[:space_index]
lname = flname[space_index + 1:]

print("Task #1")

#Capitalize first letters
first_name = fname.title()
last_name = lname.title()
print(first_name + " " + last_name)

#Lowercase first letter, uppercase the rest
first_name = fname[0].lower() + fname[1:].upper()
last_name = lname[0].lower() + lname[1:].upper()
print(first_name + " " + last_name)

print("Task #2")

phrase = "Once you start down the dark path, forever will it dominate your destiny."

upper_phrase = phrase.upper()
print(upper_phrase)

#Encryption by replacing vowels
encrypted = upper_phrase.replace("A", "1").replace("E", "2").replace("I", "3").replace("O", "4").replace("U", "5")

print(encrypted)

print(phrase)  #To show the original is unchanged

print("Task #3")
#finding length and printing it
phraselength = len(phrase)-1
print("The phrase length is ", phraselength)
piecesize = phraselength // 3

#Setting the pieces
first_piece = phrase[:piecesize]
middle_piece = phrase[piecesize:piecesize*2]
last_piece = phrase[piecesize*2:]

#Print the pieces
print(middle_piece)
print(last_piece)
print(first_piece)

print("Task #4")
#Prompt for a 5-digit number
num = input("Enter a 5-digit number: ")

#Convert to int and add
d1 = int(num[0])
d2 = int(num[1])
d3 = int(num[2])
d4 = int(num[3])
d5 = int(num[4])

total = d1 + d2 + d3 + d4 + d5

#Print the sum
print(f"{d1}+{d2}+{d3}+{d4}+{d5} = {total}")

print("Task #5")
t5phrase = "Why, you stuck-up half-witted scruffy-looking nerf herder!"

#Every other character from start to end
print(phrase[::2])

#Every other character from end to start
print(phrase[::-2])