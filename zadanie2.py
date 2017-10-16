import os

n = int(input("Input a number:"))
persons = []
for i in range(0,n):
    persons.append(input("Give me a name and surname e.g. Jane Plain:"))
x = -1
while x != 1 or x != 2:
    os.system("cls")
    print("-------------------\n")
    print("-Choose an option:-\n")
    print("-------------------\n")
    print("1. Sort by name\n")
    print("2. Sort by surname\n")
    x = int(input(""))
if x == 1:
    persons = sorted(persons, key=lambda person: person[0])
    print("X == 1")
else:
    if x == 2:
        print("X == 2")
        persons = sorted(persons, key=lambda person: person[1])
for person in persons:
    print(person)
    print("WUT")
    
