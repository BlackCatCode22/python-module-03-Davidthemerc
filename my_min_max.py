numbers = []
num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
        numbers.append(fval)
    except:
        print('Invalid Input!')
        continue
    num = num + 1

# Find min and max
minnum = min(numbers)
maxnum = max(numbers)

# Stringify values for display
numbers=str(numbers)

print('All Numbers: ' + numbers)
print('The minimum was :',minnum)
print('The maximum was :',maxnum)