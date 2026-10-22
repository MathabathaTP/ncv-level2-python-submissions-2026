n= int(input('Enter Number  :'))
total = 0
for x in range(1,n+1):
    
    cube = x**3
    
    print(cube, end=",")

    total = total + cube
print("total is = ",total)
