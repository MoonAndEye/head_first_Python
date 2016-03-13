# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:08:50 2016

@author: Moon
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
        return (files)
        
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return (None)
    
    
with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')
#james2 = james.sorted()
#print(james)

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')
#julie2 = julie.sorted()

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')
#mikey2 = mikey.sorted()

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')
#sarah2 = sarah.sorted()

def print_first_three(list):
    clean_list = [sanitize(each_t) for each_t in list]
    clean_list.sort()
    unique_list = []
    
    for each_t in clean_list:
        if each_t not in unique_list:
            unique_list.append(each_t)
    return unique_list[0:3]

clean_james=[sanitize(each_t) for each_t in james]
clean_james.sort()

clean_julie=[sanitize(each_t) for each_t in julie]
clean_julie.sort()

clean_mikey=[sanitize(each_t) for each_t in mikey]
clean_mikey.sort()

clean_sarah=[sanitize(each_t) for each_t in sarah]
clean_sarah.sort()

unique_james = []
unique_julie = []
unique_mikey = []
unique_sarah = []

for each_t in clean_james:
    if each_t not in unique_james:
        unique_james.append(each_t)

for each_t in clean_julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)

for each_t in clean_mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
        
for each_t in clean_sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)

print (unique_james[0:3])
print (unique_julie[0:3])
print (unique_mikey[0:3])
print (unique_sarah[0:3])

"""
clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]

for each_t in james:
    clean_james.append(sanitize(each_t))

for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

    
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
"""

"""
with open('james.txt') as jaf,\
open('julie.txt', 'r') as julie,\
open('mikey.txt', 'r') as mikey,\
open('sarah.txt', 'r') as sarah:
"""