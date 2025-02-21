str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
# print (ipos)
piece = str[ipos+1:]
# print(piece)
# print (piece+42.0) will fail
value = float(piece)
print (value)
# print(value+42.0)

# Can we get a float out of a user created string with a float value?
newstr = input ('Enter a string with a float value: ')
print(newstr)
newpos = newstr.find('.')
newpiece = newstr[newpos-1:]
newvalue = float(newpiece)
print(newvalue)
