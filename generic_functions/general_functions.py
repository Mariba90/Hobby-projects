"""
This script includes functions for reading dictionaries/data and other general functions"""


"""
#Importing
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np


"""
# Reading dictionary : 
  application: dictionaries that includes 501 time steps
"""

def reading_dictionary(path_name,extention_name,t_s,t_e):
  # numpy loading numpy 
  dictionary_file_np = np.load(path_name+'/'+extention_name+".npy" , allow_pickle = True)
  dic = {}
  for t in range(t_s,t_e+1):
    dic [t] = dictionary_file_np.tolist() [t]
  return dic
 
 
"""
# finding a corresponding index of a dataframe column in a array
"""
def col_to_index (data,col_name):
  ind = data.columns.tolist().index(col_name)+1
  return ind
 

"""
# converting dataframe to array specifying the type
the default d_type is int
"""
def data_to_array(data,d_type='int'):
  data_array = data.reset_index(level=[0]).to_numpy(dtype = d_type)
  return data_array

"""
# copy a column of a dataframe
"""
def copy_column(data,target_column,new_target_column):
    new_data = data.copy()
    new_data [new_target_column] = data [target_column]
    return new_data

"""
# checking if a point/cell is on boundary, input is the point/cell vector and the boundary array
boundary array format: aaray([[x_min,x_max],[y_min,y_max],[z_min,z_max]])
"""
def boundary_check(vector,boundary_array):
    condition = False
    for i in range(len(vector)):
        if (vector[i] == boundary_array[i,0]) or (vector[i] == boundary_array[i,1]):
            condition = True
            break
    return condition
    
"""
# checking if a vector is a sensative boundary
"""
def boundary_sen_check(vector,boundary_array_sen):
  condition = False
  for i in range(boundary_array_sen.shape[0]):
    for j in range(boundary_array_sen.shape[1]):
      if vector[i] == boundary_array_sen[i,j]:
        condition = True
        break
    else:
      continue
    break
  return condition 

"""
# checking if a group of points/cells is a boundary group, input is the group array and the boundary array
boundary array format: aaray([[x_min,x_max],[y_min,y_max],[z_min,z_max]])
"""
def boundary_group_check(array,boundary_array):
    condition = False
    for i in range(len(array)):
        if boundary_check(array[i],boundary_array):
            condition = True
            break
    return condition

"""
# translating x,y,z into range [0,Li]
"""
def translating(data,column_list):
  for i in range(3):
    data[column_list[i]] = data[column_list[i]] + abs(min(data[column_list[i]]))
  return data

"""
# extracting data at the specified time step from data 
"""
def data_time_step(alldata,t,n):
  # n is number of particles/points, t is the desired time step
  data = alldata [n*t:n*(t+1)]
  return data

"""
# finding the maximum and minimum coordinate of data in all 3 directions
"""
def get_min_max(x,y,z):
    # getting the minimums
    x_min, y_min, z_min = min(x), min(y), min(z)
    # getting the maximums
    x_max, y_max, z_max = max(x), max(y), max(z)
    # constructing the array
    array = np.array([[x_min,x_max], [y_min,y_max] , [z_min,z_max]])
    return array

"""
# finding the first three largest and the last three smallest values of an array
# the last three minimum and the first three maximum cells/point are sensitive for joining step
# so we do not want to remove them in preliminary elimination
input: array : [[x0,y0,z0]
                [x1,y1,z1]
                ...
                [xn,yn,zn]]
"""
def three_boundary_array(array_):
  three_boundary_list = []
  for i in range(array_.shape[1]):
    min1 = np.min(array_[:,i])
    min2 = np.min(array_[array_[:,i]!=min1][:,i])
    min3 = np.min(array_[(array_[:,i]!=min1) & (array_[:,i]!=min2)][:,i])
    max1 = np.max(array_[:,i])
    max2 = np.max(array_[array_[:,i]!=max1][:,i])
    max3 = np.max(array_[(array_[:,i]!=max1) & (array_[:,i]!=max2)][:,i])
    three_boundary_list.append([min1,min2,min3,max1,max2,max3])
  three_boundary_array=np.array(three_boundary_list)
  return three_boundary_array

"""
# swapping the labels in a dataframe based on a given dictionary 

"""
def swaping_labels(data,dictionary,col_name):
  data [col_name].replace(to_replace=dictionary, inplace=True)
  return data
  
  
"""
finding the center of mass of a array
format: [[index0,x0,y0,z0,...]
         [index1,x1,y1,z1,...]
         ...
         [indexn,xn,yn,zn,...]]
"""
def cg_(array):
  cg_ = np.array([np.mean(array[:,1]), np.mean(array[:,2]), np.mean(array[:,3])])
  return cg_
"""
# calculating distance of two arrays 
array format: [x,y,z]
"""
def distance(array1,array2):
  d = np.sqrt(np.sum((array1-array2)**2))
  return d
