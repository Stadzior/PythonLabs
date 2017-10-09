for i in range(1,9):
    print (pow(2,i))

for i in range(1,6):
    answer=int(input("Give me 3 to {}:".format(i)))
    if answer != pow(3,i):
        print ("Sorry, 3 to {} equals {} not {}, good bye.".format(i,pow(3,i),answer))
        break
        

