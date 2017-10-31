import shutil
columns = shutil.get_terminal_size().columns
n = int(input("Input a number:"))
persons = []
for i in range(0,n):
    persons.append(input("Give me a name and surname e.g. Jane Plain:").split())
x = "0"
while x != "q":
    x  = "0"
    while x != "1" and x != "2" and x != "q":
        print(" --------------------".center(columns))
        print("| Choose an option:  |".center(columns))
        print(" --------------------".center(columns))
        print("| 1. Sort by name    |".center(columns))
        print("| 2. Sort by surname |".center(columns))
        print(" --------------------".center(columns))
        x = input("")
    if x == "1":
        sortedPersons = sorted(persons, key=lambda person: person[0])
    else:
        if x == "2":
            sortedPersons = sorted(persons, key=lambda person: person[1])
    if (x == "1" or x =="2"):
        for i in range(0, len(sortedPersons)):
            print('{}. {} {}'.format(i+1,sortedPersons[i][0],sortedPersons[i][1]).center(columns))
    
