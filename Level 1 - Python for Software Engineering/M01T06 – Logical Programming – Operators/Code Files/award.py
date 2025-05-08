"""
This program will figure out what award a triathalon competitor will recieve using 
logical perators and criteria for each race component.
2025-05-08 EJS
"""

swim_time = int(input("Please enter the swim time in minutes: "))
cycle_time = int(input("Please enter the cycle time in minutes: "))
run_time = int(input("Please enter the run time in minutes: "))

total_time = swim_time + cycle_time + run_time

award = ""
if (total_time >= 0) and (total_time <=100):
    award = "Provincial colours"
elif total_time <= 105:
    award = "Provincial half colours"
elif total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

print(f"The competitor's award: {award}")