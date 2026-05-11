total_people = 91  # total population
infected = 5       # initial infected people
growth_rate = 0.4 # growth rate of infection
day = 1          # day counter
print(f"day {day}，infected people：{infected} ")# print the initial state
while infected < total_people:
    infected = infected + infected * growth_rate # calculate the number of infected people for the next day
    day += 1 # increase the day counter by 1
    print(f"day {day}，infected people：{infected:.0f} ") 
print(f"\n all {total_people} people are infected， {day} days are taken")
