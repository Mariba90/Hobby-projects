# -*- coding: utf-8 -*-
"""
  Reading hits and threshold dictionaries from remote machine results/subdomain_results:
  we do not initialize the dictionary in this function because
  the *.npy data have been stored in different files depends on the time step range.
  because we could not run all 500 time steps at once using Sabine cluster
  Saving all dictionaries into one integerated dictionary
#Importing
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np



"""# Reading dictionaries function"""


def reading_dictionary(path_name,extention_name,t_s,t_e,dic):
  # numpy loading numpy 
  dictionary_file_np = np.load(path_name+'/'+extention_name+"_"+str(t_start)+"_"+str(t_end)+".npy" , allow_pickle = True)
  for t in range(t_s,t_e+1):
    dic [t] = dictionary_file_np.tolist() [t]
  return dic

"""# Reading dictionary"""
path_results='/content/drive/MyDrive/PhD_ML/results/subdomain_results'

t_start = 0
t_end = 200
# when moving forward with the time-steps, comment the below initialized dictionaries
hits_cell , hits_point = {},{}
thresh_fall_cell , thresh_rise_cell = {},{}
thresh_fall_point , thresh_rise_point = {},{}
hits_cell = reading_dictionary(path_results,'hits_cell',t_start,t_end,hits_cell)
hits_point = reading_dictionary(path_results,'hits_point',t_start,t_end,hits_point)
thresh_fall_cell = reading_dictionary(path_results,'thresh_fall_cell',t_start,t_end,thresh_fall_cell)
thresh_rise_cell = reading_dictionary(path_results,'thresh_rise_cell',t_start,t_end,thresh_rise_cell)
thresh_fall_point = reading_dictionary(path_results,'thresh_fall_point',t_start,t_end,thresh_fall_point)
thresh_rise_point = reading_dictionary(path_results,'thresh_rise_point',t_start,t_end,thresh_rise_point)

"""# Saving dictionary
basically, let's save all time-steps dictionaries into one dictionary 
"""

np.save(path_results+"/hits_cell", hits_cell)
np.save(path_results+"/hits_point", hits_point)
np.save(path_results+"/thresh_fall_cell_002", thresh_fall_cell)
np.save(path_results+"/thresh_rise_cell_002", thresh_rise_cell)
np.save(path_results+"/thresh_fall_point_002", thresh_fall_point)
np.save(path_results+"/thresh_rise_point_002", thresh_rise_point)