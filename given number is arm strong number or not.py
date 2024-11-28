num = int(input("Enter a number: "))
original_num = num
sum_of_cubes = 0
while num > 0:
    rem = num % 10  
    sum_of_cubes += rem ** 3  
    num //= 10  
if sum_of_cubes == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
