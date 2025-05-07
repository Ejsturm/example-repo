"""
Ask for three integers and execute mathematics on them. Print results
2025-05-07 EJS
"""

int1 = int(input("Provide first integer: "))
int2 = int(input("Provide second integer: "))
int3 = int(input("Provide third integer: ")) 

print("The sum of all three is {}.".format(int1+int2+int3))
print("The first minus the second is {}".format(int1-int2))
print("The third multiplied by the first is {}".format(int3*int1))
print("The total sum divided by the third is {}".format((int1+int2+int3)/int3))