for i in range(1,9):
    print (pow(2,i))

for i in range(1,6):
    answer=input("Give me 3 to {}:".format(i))
    boostedAnswer=""
    for x in answer:
        if x.isdigit():
            boostedAnswer+=x
    if int(boostedAnswer) != pow(3,i):
        print ("Sorry, 3 to {} equals {} not {}, good bye.".format(i,pow(3,i),boostedAnswer))
        break    
        

