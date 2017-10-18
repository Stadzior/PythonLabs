n = int(input("Input a number:"))
persons = []
for i in range(0,n):
    persons.append(input("Give me a name and surname e.g. Jane Plain:").split())
x = "0"
while x != "q":
    x  = "0"
    while x != "1" and x != "2":
        print("-------------------\n")
        print("-Choose an option:-\n")
        print("-------------------\n")
        print("1. Sort by name\n")
        print("2. Sort by surname\n")
        x = input("")
    if x == "1":
        sortedPersons = sorted(persons, key=lambda person: person[0])
    else:
        if x == "2":
            sortedPersons = sorted(persons, key=lambda person: person[1])
    for person in sortedPersons:
        print('{} {}'.format(person[0],person[1])
