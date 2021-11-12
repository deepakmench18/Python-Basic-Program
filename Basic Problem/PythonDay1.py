# -*- coding: utf-8 -*-
"""

Created on Mon Nov  8 12:28:33 2021
@author: Deepak Mench

"""

txt = "Deepak Mench"
if "Mench" in txt :
    print(True);
    
txt = "Deepak Mench"
if "Solapur" not in txt :
    print(True);

txt = "Deepak Mench"
print(txt[2:6]);

txt = "Deepak Mench";
print(txt[:6])

txt = "Deepak Mench"
print(txt[1:])

txt = "Deepak Mench"
print(txt[:])

txt = "Deepak Mench"
print(txt[-5:0])

#Remove space from starting and end

txt = " Deepak Mench  "
print(txt.strip())

txt = "Deepak Mench"
print(txt.replace("D","a"))

txt = "Deepak ,Mench"
print(txt.split(","))

age = 21
txt = "Deepak Mench is {} old"
print(txt.format(age))

age = 21
city = "Solapur"
state = "MH"
txt = "Deepak Mench from {} , {} he is {} old"
print(txt.format(city,state,age))

n=6
if n %2 == 0:
    print("Even")
else:
    print("Odd")
                