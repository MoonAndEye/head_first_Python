# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:59:52 2016

@author: Moon
"""
import pickle
import nester
man = []
other = []

try:
    
    data = open('sketch.txt')

#print (the_file.readline(), end = '')
    for each_line in data:
        try:
        #print (each_line, end = '')
            (role, line_spoken) = each_line.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
            
            #print(role, end = '')
            #print(' said: ', end  = '')
            #print(line_spoken, end = '')
        except ValueError:
            pass
    data.close()
    
except IOError:
    print('The datafile is missing!')
   
"""   
print(man)
print(other)
"""

try:
    """
    data_man = open('man_data.txt', "w")
    data_other = open('other_data.txt', "w")
    """
    with open('man_data.txt', 'wb') as data_man:
    #print(man, file=data_man)
        pickle.dump(man, data_man)
    with open('other_data.txt', 'wb') as data_other:
    #print(other, file=data_other)
        pickle.dump(other, data_other)
   
    
except IOError as err:
    print ('File error: ' + str(err))
    
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
    
    