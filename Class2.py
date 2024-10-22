input1 = input("input a word or a sentance: ")

vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

for i in input1:
    if i in vowels:
        vowels[i] += 1

print(vowels)

# find if the number enterd by the user is a panogram or not 

number = input("enter a number: ")

numbers = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

for i in number:
    if i in numbers:
        numbers[i] += 1

panogram = True
for j in numbers.values():
    if j == 0:
        panogram = False
if panogram:
    print("Enterd number is a panogram")
else:
    print("enterd number is not a panogram")



