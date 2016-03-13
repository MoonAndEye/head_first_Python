# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:35:32 2016

@author: Moon
"""
import sys
def print_lol (the_list, indent = False,level = 0, fh = sys.stdout):
    """This is an example from the book 'head first to Python
    A test."""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent,level + 1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print ("\t", end = '',file = fh)
                print(each_item, file = fh)