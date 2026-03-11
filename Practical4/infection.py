total_people = 91  
infected = 5       
growth_rate = 0.4 
day = 1          
print(f"day {day}，infected people：{infected} ")
while infected < total_people:
    infected = infected + infected * growth_rate
    day += 1 
    print(f"day {day}，infected people：{infected:.1f} ")
print(f"\n all {total_people} people are infected， {day} days are taken")
