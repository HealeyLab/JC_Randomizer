# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:24:46 2021

@author: Healey
"""


"""Journal Club Random Figure Presentation Selector"""

import random
import time



classlist = ['Felipe','Hannah', 'Sarah', 'Annabelle', 
             'Hyejoo', 'Chase', 'Julia', 'Danny', 'Christine', 
             'Ellen', 'Andrew', 'Jennifer']

def opt_out(student):
    
    for i in range(len(classlist)-1):
        if classlist[i] == student:
            classlist.pop(i)
    

def choose_presenters(classlist, number_of_figures):
    
    fig_list = []   
    
    fig_list.append(random.sample(classlist, number_of_figures))
    
    input("Press Enter to begin....")
    print(" ... ... ... [drumroll......]  ... ... ...")
    time.sleep(4)
    
    for i in fig_list[0]:
        print("                                                   ")
        print("                                                   ")
        print(str("The next figure will be presented by: " + str(i) + " "))
        input("Press Enter to continue to the next Figure....")
        print("                                                   ")
        print("                                                   ")
        print(" ... ... ... [drumroll......]  ... ... ...")
        time.sleep(4)
        print("                                                   ")
        
    print("Your lucky winners for today's 892 Journal Club were: ")
    
    return fig_list




def chooser_simulation(numTrials, student, figs):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of a named 'student' appearing in on the list of
    figure presenters ('fig_list' from 'choose_presenters' 
    above). Returns the a decimal - the fraction of times 
    the student made the list.
    '''
  
    frac = 0
    numtarget = 0
    for t in range(numTrials+1):
        if student in choose_presenters(classlist, figs)[0]:
            numtarget += 1
    
    frac = numtarget/numTrials
    print(frac)
    return frac




