#Create the initial set
colors = {'red', 'blue', 'green'}
#Add a new color 'yellow'
colors.add('yellow')
#Remove 'blue' from the set
colors.remove('blue')  # or colors.discard('blue')
#Check if 'green' is present in the set
is_green_present = 'green' in colors
print(is_green_present)  # This will print True
#Use update() to add multiple items
new_colors = ['purple', 'orange']
colors.update(new_colors)
#Final set of colors
print(colors)  
