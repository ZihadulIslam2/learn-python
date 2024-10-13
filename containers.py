a_tuple = (1,2,3,"hello")
print(a_tuple)

a_list =[1,2,3,"hello",1,2]
print(a_list)
 # i can add append on a list
a_list.append('the is append')
print(a_list)

# a list can be change.
#  but a tuple is fixed can't be change


a_set = {1,2,3,"hello",3} # in sets common items not shows.
print(a_set)

print(list(set(a_list)))

a_dictionary = { 'key':'values', 123 : [1,2,3]} #like object key: value

# how to get values from containers

a_listof_name = ['zihaul', 'islam', 'Tusher', 'Hisham','Saad']
print(a_listof_name[4]) # indexing
print(a_listof_name[1:3]) # slicing an indexing

# same system in topol

print(a_dictionary[123])