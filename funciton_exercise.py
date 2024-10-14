def shouter(strings,number):
    if  number>10:
        print("you are too loude.")
    else:
        for i in range(number):
            print(i,strings.upper())
    return "done"            

   
print(shouter("This is a string",11))