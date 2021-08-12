# Immutable variables: ints; O(1) [to find new location for them is cheap]; string
# num = 1
# print(id(num))

# num = 100
# print(id(num))

# num2 = num
# print(num2 is num)

# num2 = 2
# print(num)
# print(num2 is num)

# Mutable Variables: arrays, dictionaries, class instances
arr = [1,2,3] #arrays are mutable
print(id(arr))

arr2 = arr
print(arr2 is arr)

arr2 = ['a', 'b'] # now assigning arr2 to something so this is a new array
print(arr)

arr2.append(4)
print(arr) # will return the original arr since arr2 was reassigned

# Mutable - Dictionaries
my_dict = {'hello': 'world'}
my_dict2 = my_dict

my_dict2['new_key'] = 'new value'
print(my_dict)

