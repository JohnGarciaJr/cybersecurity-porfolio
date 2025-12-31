# Triathlon Award Program
# Determines the award a competitor receives based on finishing time.

# Get the finishing time from the user
finishing_time = int(input("Enter the finishing time in minutes: "))

# Determine the award based on the finishing time
if 0 <= finishing_time <= 100:
    award = "Provincial Colors"
elif 101 <= finishing_time <= 105:
    award = "Provincial Half Colors"
elif 106 <= finishing_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No Award"

# Output the award
print("Award:", award)
