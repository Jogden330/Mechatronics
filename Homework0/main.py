# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:21:33 2022

@author: jogde
"""
import random

numbsToGuess = 4*[0]
wins = 0
loss = 0
output = ''

#creat random numbers
for i in range(len(numbsToGuess)):
    numbsToGuess[i] = random.randint(0,5)
    print(numbsToGuess[i])

print('wins ', wins,'loss ', loss)

print('Enter 4 numbers between 0 and 5')

input_Numbers = input()

input_Numbers  = input_Numbers.split() 

for j in range(len(input_Numbers)):
    try:
       number = int(input_Numbers[j]) 
       for i in range(len(numbsToGuess)):
           if (numbsToGuess[i] == number) and (i == j) :
               output = output + "+"
               break
           else :
               if (numbsToGuess[i] == number) :
                   output = output + "-"
                   break
                   
       
    except ValueError:
         print(number, " is not a number")
     
print(output)
    

