num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input!')
        continue
    # print (fval)
    num = num + 1
    tot = tot + fval

    # Stringify values for display
    num=str(num)
    tot=str(tot)

# print ('ALL DONE')
# print (tot,num,tot/num)
print ('Total: ' + tot + ' # of Numbers: ' + num + 'Average of Numbers: ' + tot/num )