# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:47:28 2016
@author: Moon
明天從這個檔案開始改起
在p185,這裡有四個要求
1：字典的建立要以一氣呵成的方式來進行
2：將字典的建立程式碼往 get_coach_data()
"""
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
        #(mins, secs) = time_string.split(splitter)
    elif ':' in time_string:
        splitter = ':'
        #(mins, secs) = time_string.split(splitter)
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)
    
def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
        files = data.strip().split(',')
        diction = {}
        diction['Name'] = files.pop(0)
        diction['DOB'] = files.pop(0)
        diction['time'] = files
        diction['printout'] = str(sorted(set([sanitize(t) for t in files]))[0:3])
        return (diction) 
        
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return (None)
        
"""        
        
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
"""

sarah_dict = get_coach_data('sarah2.txt')

"""
sarah = {}

sarah['Name'] = sarah_list.pop(0)
sarah['DOB'] = sarah_list.pop(0)

sarah['result']=sarah_list
"""
print(str(sarah_dict['Name']) + 
"'s fastest times are: " + 
str(sarah_dict['printout']))
