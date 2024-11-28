#Given string
phrase = "AnalyticsData"

#Calculating the length of the string
length = len(phrase)

#Finding the midpoint
#For odd lengths, we include the middle character in the first half
midpoint = (length // 2) + 1  #This gives us the index for the first half

#Slicing the string into two halves
first_half = phrase[:midpoint]
second_half = phrase[midpoint:]
print("First half:", first_half)
print("Second half:", second_half)
