from datetime import*
today=datetime.today()
print('today is: ',today)
#print(dir(datetime))
'''print(today.day)
print(today.month)
print(today.year)'''
print('Today\'s Date: ',today.strftime('%A,%d.%B.%Y'))
print('Today\'s Time: ',today.strftime('%I:%M:%S:%f %p'))
print('now using loop in order to change attributes of today automatically in format datetime.today.attribute')
for attr in ['year','month','day','hour','minute','second','microsecond']:
    print(attr,':\t',getattr(datetime.today(),attr))
#adding a statement to display time using dot notation
print( 'Time:',today.hour,':', today.minute ,':', today.second, sep ='' )




