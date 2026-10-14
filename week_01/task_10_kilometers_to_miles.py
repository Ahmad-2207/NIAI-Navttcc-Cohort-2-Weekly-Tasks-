# Task 10: Convert kilometers to miles

# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac

# the original sheet stops before printing, so the result is displayed here
print('%0.2f kilometers is equal to %0.2f miles' % (kilometers, miles))
