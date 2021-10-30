#TempConvert.py
val = input('Please input a temperature ended by C:')
if val[-1] in ['C', 'c']:
    f = 1.8*float(val[0:-1])+32
    print('Converted temperature is: %.2fF'%f)
elif val[-1] in ['F', 'f']:
    c = (float(val[0:-1])-32)/1.8
    print('converted temperature is: %.2fC'%C)
else:
    print('Error')
