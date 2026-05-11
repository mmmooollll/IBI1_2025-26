# What does this piece of code do?
# Answer:
#Calculates the sum of 11 random numbers which were generated between 1 and 10 
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0 # initialize the variable to store the total of random numbers
progress=0 # initialize the variable to count the number of random numbers drawn
while progress<=10: # loop until 10 random numbers have been drawn
	progress+=1 # increase the progress by 1
	n = randint(1,10) # draw a random number between 1 and 10
	total_rand+=n # add the drawn random number to the total

print(total_rand)

