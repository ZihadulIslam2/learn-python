# create a custom function
# # def_function_name: def is for define

# def print_n_times(parameter, loop_amount):    # i need to recive the argument by typing any kind of parameter
#     count = 1
#     while count <= loop_amount:
#         print(count,parameter)
#         count +=1

# # call the function:
# print_n_times('Zihadul Islam', 10) # i pass a argument to the print_5_times function.



# set a default parameter
# def print_n_times(parameter="default parameter", loop_amount=5):    # i need to recive the argument by typing any kind of parameter
#     count = 1
#     while count <= loop_amount:
#         print(count,parameter)
#         count +=1

# # call the function:
# print_n_times() # i pass a argument to the print_5_times function.


# return 

def print_n_times(parameter="default parameter", loop_amount=5):
    count = 1
    while count <= loop_amount:
        print(count,parameter)
        count +=1
    return


print_n_times()