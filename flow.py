if 5>6:
    print("this is a bulion")
elif 3>2:
    print('this is also like the if') 
elif 0==0 and 5>2:
    print('this is also like the if')        
else:
    print('incorrect result.')
print('not connected to the if')

# while loop

counter = 0
while counter <= 10:
    print(counter)
    counter+=1
    if counter==5:
        print("Counter is 5")
print("the while loop is stop.")

# for loop
test_list =[1,2,3,4,5]
for x in test_list:  # we are storing every single thing in the test_list to x variable
    print(x)

# truthy and falsy
if 0: # is falsy
    print('some thing')
elif [1]:
    print('true')