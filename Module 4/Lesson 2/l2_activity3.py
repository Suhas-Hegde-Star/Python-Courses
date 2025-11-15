import random

tuples = ()
for i in range(100): tuples += (random.randint(0,1),)  
print(tuples)

one, zero = tuples.count(1), tuples.count(0)
print(f'Number of ones: {one}\nNumber of zeros: {zero}')

print('The tuple has more ones' 
      if one > zero 
      else 'The tuple has more zeros' 
      if zero > one 
      else 'The tuple has equal number of ones and zeros')

print(("The ones are more by 25 or more than the zeros" 
      if one - zero >= 25 
      else "The zeros are more by 25 or more than the ones" 
      if zero - one >= 25 
      else "Neither ones nor zeros are more by 25 or more") 
      and ("End of Program")
      and ("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"))