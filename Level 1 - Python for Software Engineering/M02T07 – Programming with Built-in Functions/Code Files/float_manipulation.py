'''Takes in 10 floats from the user and performs statistics on them using the
statistics module. 2025-05-13 EJS'''

import statistics

numbers = []
for _ in range(10):
    numbers.append(float(input("Enter a float: ")))

total = 0.0
for n in numbers:
    total += n

max_index = numbers.index(max(numbers))
min_index = numbers.index(min(numbers))
mean = round(statistics.mean(numbers), 2)
median = statistics.median(numbers)

print(f"The max index is {max_index}.")
print(f"The min index is {min_index}.")
print(f"The mean is {mean}.")
print(f"The median is {median}.")
