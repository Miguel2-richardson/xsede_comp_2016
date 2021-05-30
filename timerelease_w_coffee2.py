# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:09:00 2016

@author: Miguel
"""

import math
import matplotlib.pyplot as plt
import numpy as np

time_start = 0.0
time_step = 0.25
time_end = 48
pills = 24 # number of pills taken in 24 hours, this is for time release
a= time_start # iterative variable for if statements
t =np.arange(time_start, time_end, time_step)
N = int((time_end - time_start)/time_step)
next_dose = 24/pills

n=0.18 #percentage of 2day dose from 1st pill. @ 10% of the total value it takes about 12 hours to get in range
#THe range for the time release is 10% for 1st dose to 25%. 19 - 22% gives the best range
#This is true for 12950 mg

if (pills > 1): #To determine percent left of dose after 1st pill is taken
   k = (1-n)/(2*pills - 1) # *2 accounts for the pills taken over the 2 days
else:
    k = 0

intake = [0]*(N+1)
dose =2*14850 #Multiplied by 2 to get the dose for the 2 days
dosage = [0]*(N+1)

#We thought it would be better to have a different dose for the 1st pill than the others
for i in range(N):
    if t[i]==time_start:
        #print ("In first loop")
        dosage[i] = n*dose #1st pill has 24% of the 2day allotment of the meds.
        #print("Next does is", a)
        #print("THe time is", t[i])
        a=next_dose + a
        #print("Next dose",a)
    if t[i]==(a):
        #print("In 2nd loop")
        #print("Next dose is", a)
        dosage[i]=((k*dose)) #The remaining doses all have the same amount.
        a= a + next_dose
        #print("Next dose is", a)
        #print("The time is", t[i])
        
intake = dosage #THe array constructed for dosage gives the same result for intake that was calculated in the sample code



absorption_rate = 0.25
blood_volume = 4.6
medicinal_level = 800  # level at which drug becomes effective mg/l
toxic_level = 1000     # level at which drug becomes toxic  mg/l
half_life = 6
dosage_int = 24/pills
excretion_rate = math.log(2)/half_life
excretion_rate2 = (math.log(2)/half_life)*1.2
steps_between_doses = dosage_int/time_step

medicine_in_intestines = [0]*(N+1)
plasma_level = [0]*(N+1)
plasma_concentration = [0]*(N+1)
plasma_concentration2 = [0]*(N+1)
absorption = [0]*(N+1)
excretion = [0]*(N+1)
excretion2 = [0]*(N+1)

t = [0]*(N+1)
t[0] = time_start
step_next_dose = 1

for i in range(N):
    t[i+1] = t[i] + time_step
    
    if i == step_next_dose:
        #intake[i] = dosage
        step_next_dose = i + steps_between_doses
    #else:
        #intake[i] = 0


for i in range(N): 
    absorption[i] = time_step * absorption_rate *medicine_in_intestines[i]
    excretion[i] = time_step * excretion_rate * plasma_level[i] 
    medicine_in_intestines[i+1] = medicine_in_intestines[i] - absorption[i] + intake[i] 
    plasma_level[i+1] = plasma_level[i]  -  excretion[i] + absorption[i]    
    plasma_concentration[i+1] = plasma_level[i+1] / blood_volume

for i in range(N): 
    absorption[i] = time_step * absorption_rate *medicine_in_intestines[i]
    excretion2[i] = time_step * excretion_rate2 * plasma_level[i] 
    medicine_in_intestines[i+1] = medicine_in_intestines[i] - absorption[i] + intake[i] 
    plasma_level[i+1] = plasma_level[i]  -  excretion2[i] + absorption[i]    
    plasma_concentration2[i+1] = plasma_level[i+1] / blood_volume

plt.plot(t,plasma_concentration, color = 'b', label= "Plasma Concentration")
plt.plot(t,plasma_concentration2, 'bs', label= "Plasma Concentration w/ coffee")
m_level = [medicinal_level]*(N+1)
plt.plot(t, m_level, color= 'r', label= "Medicinal Level",)

t_level = [toxic_level]*(N+1)
plt.plot(t, t_level, color = 'g', label = "Toxic Level")

plt.legend(loc=4)

plt.minorticks_on()
plt.ylim(0,1100)
plt.show()

