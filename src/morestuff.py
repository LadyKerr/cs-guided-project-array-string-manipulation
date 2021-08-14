'''

'''
# in place algos: 
def double_nums_by_ref(a):
  for i in range(len(a)):
    a[i] = a[i] * 2

# out of place algos: 
def double_nums(a):
  new_arr = []
  for i in range(len(a)):
    new_arr.append(a[i] * 2)
  return new_arr

arr = [1,2,3,4]

double_nums_by_ref(arr)
# pass in the reference to the arr in memory
# var a in the func is also pointing to the arr in memory
# this is called pass by reference

arr2 = double_nums(arr)
print(arr)
print(arr2)

