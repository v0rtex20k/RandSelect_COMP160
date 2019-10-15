##########################################################################
#
#    Tufts University, Comp 160 randSelect coding assignment  
#    randSelect.py
#    randomized selection
#
#    includes functions provided and function students need to implement
#
##########################################################################

from random import *

'''
Purpose: randSelect recursively calls randPartition. Each time the array has
	 been partitioned, we compare the desired index with the index of 
	 the pivot - if they match, we have found our value and we can end. 
	 Otherwise, we recurse into the subarray in which our value resides,
	 and partition the subarray.
Inputs:  ray (list of ints), index (desired index)
Returns: The value at the desired index = the pivot index
'''
def randSelect(ray, index):
	print("Looking for value with rank", index, "in the array:")
	print(ray);
	pivot_index = randPartition(ray)
	print("its rank is", pivot_index, end='; ')
	if index == pivot_index:
		print("Thus, we recurse on nothing. We are done.")
		return ray[pivot_index]
	if index < pivot_index:
		ray = ray[0:pivot_index]
		print("Thus, we recurse on left.")
		return randSelect(ray, index)
	if index > pivot_index:
		ray = ray[pivot_index+1:len(ray)]
		print("Thus, we recurse on right.")
		return randSelect(ray, index - pivot_index-1)

'''
Purpose: randPartition partitions the array (or subarray) by randomly choosing 
	 a pivot value and then putting all values greater than the pivot value
	 to the right of the pivot, and leaving all values less than the pivot
	 value to the left of the pivot. If elem > pivot, swap elem and 
	 array[pivot-1], then swap pivot and array[pivot-1] and decrement i by
	 1 to double check the newly swapped value.
Inputs:  ray (list of ints)
Returns: The pivot index
'''
def randPartition(ray):
	pivot_index = randint(0, len(ray)-1)
	print("Selected", ray[pivot_index], "as the pivot", end='; ')
	ray[pivot_index], ray[len(ray)-1] = ray[len(ray)-1], ray[pivot_index]
	pivot_index = len(ray)-1
	i=0
	while i < len(ray)-1:
		if i == pivot_index:
			break;
		if ray[i] > ray[pivot_index]:
			ray[pivot_index-1], ray[i] = ray[i], ray[pivot_index-1]
			ray[pivot_index-1], ray[pivot_index] = \
			ray[pivot_index], ray[pivot_index-1]
			pivot_index-= 1;
			i -= 1
		i += 1
	return pivot_index
