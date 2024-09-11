import string,random

chars = " "+string.punctuation+string.digits+string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

plain_text = input("Enter message: ")
chipher = ""
for letter in plain_text:
    index = chars.index(letter)
    chipher+=key[index]
print(f"{plain_text}\n{chipher}")

#___________
plain_text = input("Enter message: ")
chipher = ""
for letter in plain_text:
    index = key.index(letter)
    chipher+=chars[index]
print(f"{plain_text}\n{chipher}")

