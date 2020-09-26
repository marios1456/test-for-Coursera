import  tkinter as tk
houses = ['Lin', 'Malik', 'Nia', 'Ophelia', 'Pradeep']
posible_compos = []
for i in houses:
    for j in houses:
        for k in houses:
            for x in houses:
                for y in houses:
                    posible_compos.append([i, j, k, x, y])
for i in posible_compos:
    temp = len(i) != len(set(i))
    if not temp:
        second_condition = i.index(houses[3]) -i.index(houses[2])
        if second_condition > 0:
            first_condition_1 =(i.index(houses[1]) + i.index(houses[4])/2)
            min_ind = min(i.index(houses[1]), i.index(houses[4]))
            max_ind = max(i.index(houses[1]), i.index(houses[4]))
            if (first_condition_1 > i.index(houses[2]) and min_ind < i.index(houses[2])) or (first_condition_1 < i.index(houses[2]) and max_ind > i.index(houses[2])):
                last_condition = abs(i.index(houses[1])-i.index(houses[2]))
                if last_condition > 1:
                    fourth_condition = i.index(houses[0])-i.index(houses[3])
                    if fourth_condition > 0:
                        print(i)

import re
from urllib.request import *
x = urlopen(Request('https://www.upatras.gr')).read()
#print(type(x))

import os
import os.path
count = 0
for (r,d,f) in os.walk(os.getcwd()):
    count += 1
print("a =", count)

a = 124