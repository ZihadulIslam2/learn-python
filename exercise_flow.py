# create a list = (1,2,3,4,5)
# if the value is 2 print "the value is 2"
# if it is'nt than 'it is ant not True'
# if the value is 5 run a while loop to print 'last item' 6 times

# exersice_list = [1,2,3,4,5]

# if exersice_list == 2:
#     print('The value is true.')
# else:
#     print('it is not 2.')

# i = 0
# while  i<6:
#     if exersice_list == 5:
#         print("Last item")
#     i+= 1

# Create a list
exercise_list = [1, 2, 3, 4, 5]

# Loop through the list to check each value
for value in exercise_list:
    if value == 2:
        print("The value is 2")
    else:
        print("It is not 2")

# If the value is 5, run a while loop to print 'last item' 6 times
if 5 in exercise_list:
    i = 0
    while i < 6:
        print("Last item")
        i += 1
