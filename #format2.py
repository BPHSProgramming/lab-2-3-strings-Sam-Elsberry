# format2.3-sam-elsberry-25

flname = input("Enter your first and last name with a single space separating the two. Do not add leading or trailing characters or spaces: ")

fname = flname.split()[0]
lname = flname.split()[1]

print("Task #1")

first_name = fname.title()
last_name = lname.title()
print(first_name + ", " + last_name)

first_name = fname[0].lower() + fname[1:].upper()
last_name = lname[0].lower() + lname[1:].upper()
print(first_name + ", " + last_name)

print("Task #2")

phrase = "Once you start down the dark path, forever will it dominate your destiny."

upper_phrase = phrase.upper()
print(upper_phrase)

encrypted = upper_phrase.replace("A", "1")
encrypted = encrypted.replace("E", "2")
encrypted = encrypted.replace("I", "3")
encrypted = encrypted.replace("O", "4")
encrypted = encrypted.replace("U", "5")

print(encrypted)

print(phrase) #to show the original is unchanged