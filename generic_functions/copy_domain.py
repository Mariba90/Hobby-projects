
"""
# this function is for copying an array in 1D,2D or 3D periodic space
"""

"""
# Importing
"""
import numpy as np


# copy array and change the index : 
# example the first copy indices will be from n_p to n_p+np and so on

def copy_all(array):
  n_p = len(array)
  array_copy = np.copy(array) 
  for i in range(n_p):
    array_copy [i,0] =  array [i,0] + n_p
  return array_copy


# copy to the right
def UpcoordR(X,L,i):
  n_p = len(X)
  for j in range(n_p):
    X [j,i+1] = X [j,i+1] + L
  return (X)
# copy to the left
def UpcoordL(X,L,i):
  n_p = len(X)
  for j in range(n_p):
      X [j,i+1] = X [j,i+1] - L
  return (X)

"""
basically for each dimension if dim_arr==1 
we copy the array to the left and right and store array
for the next dimension we append the previously copied array to the new copied array
for example:
i=0 input:  array                   output: [array][array][array]

i=1 input:  [array][array][array]   output: [array][array][array]
                                            [array][array][array]
                                            [array][array][array]
                                         
i=2:input:  [array][array][array]   output: in 3 dimensional
            [array][array][array]
            [array][array][array]
"""
def copy_domain_array(dim_arr, domain_length, array):
  for i in range(len(dim_arr)):
    if dim_arr [i] == 1:
      L = domain_length [i]
      pack_array1 = copy_all (array)
      pack_array2 = copy_all (pack_array1)
      pack_array1 = UpcoordR(pack_array1,L,i)
      pack_array2 = UpcoordL(pack_array2,L,i)
      array = np.concatenate((array, pack_array1 , pack_array2 ), axis=0)
  return array
