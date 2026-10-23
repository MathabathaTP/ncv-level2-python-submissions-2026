marks=[]

mark = int(input('Enter mark:  or -1 to stop '))

while mark != -1:
    marks.append(mark)
    
    mark = int(input('Enter mark:  or -1 to stop '))
print("first:", marks[0])
for x in range(len(marks)):
    print (marks[x])
    
print(f'Our list has {len(marks)} elements')
sum = 0
for x in range(len(marks)):
    mark = marks[x]
    sum =sum + mark
    
print(f'the sum of all marks =   {sum}')
## get the average of all marks
total =0

for x in range(len(marks)):
    mark = marks[x]
    total = total + mark

avg = total/len(marks)
print(f'the average of all marks =  {avg} ')

