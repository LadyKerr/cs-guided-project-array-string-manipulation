# arrays are series of spaces

# Static Arrays
arr = [1,2,3,4] # this will be 4 spaces long, next to each other
# the arr itself points to the first value in the arr
# if you want to access the other values, add 1,2,3 etc to get the location you want

'''
- arrays access items at constant time O(1)
- arr.append() is O(n)
- changing an item in the arr is O(1)
- deleting an item is O(n) since you have to shuffle items to the left
- arr.insert() is O(n) since things have to shuffle to the right
'''

num = 1
