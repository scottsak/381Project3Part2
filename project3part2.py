'''
EE 281 Project 3 - Part 2
Scott Sakurai
018497139
'''

step  = [] #list to record movement

import random 

p_A = float(input("Enter the probability of going from 0 to 1: "))
p_B = float(input("Enter the probability of going from 1 to 0: "))

S = int(input("Enter either 0 or 1 for the starting location: "))

step.append(S) # starting point

for i in range(24):
    r = random.uniform(0,1)
    if r < p_A and S == 0: #at node 0 flip coin A
        S = 1
    elif r < p_B and S == 1: #at node zero flip coin B
        S ==0
    step.append(S)

for i in step:
    print(i,end="") #print Target variable