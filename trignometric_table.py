'''
This python script prints the trignometric in a form of a table.
'''
import math

print('-'*54)
print('|','Angle(or x)'.center(10),\
    '|','Sin(x)'.center(10),\
    '|','Cos(x)'.center(10),\
    '|','Tan(x)'.center(10),'|')
print('-'*54)

difference = math.pi/4
upper_limit = 2*math.pi
no_of_iterations = int((upper_limit)/difference) # 2*pi/(pi/4) = 8

# Here i is representing a number which on multiplying with pi/4 gives the respective angle in radians
# In this table, we converted radians to degress 
for i in range(0,no_of_iterations+1):
    print('|',(str(int(math.degrees(i*(math.pi/4)))) + '°').center(12),end='|') # printing angle
    print(str(round(math.sin(i*difference),2)).center(12), end='|' ) # printing sin x
    print(str(round(math.cos(i*difference),2)).center(12),end='|') # printing cos x
    print(str(round(math.tan(i*difference),2)\
         if i % 4 != 2 else 'infinity').center(12), end='|\n') #printing tan x

print('-'*54)

