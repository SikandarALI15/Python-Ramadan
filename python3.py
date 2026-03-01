# 1
num1=float(input('Enter num1 : '))
opr=input('Enter Operator +,-,x,** :')
num2=float(input('Enter num2 : '))

res=None

if opr =='+':
    res=num1+num2
elif opr =='-':
    res=num1-num2    
elif opr =='/':
    res=num1/num2        
elif opr =='x':
    res=num1*num2        
elif opr =='**':
    res=num1**num2 
else:
    res='wrong operator'           

print('Your answer is',res)



# 2

lst=['Mango','Banana',356,'Apple',0.34,'Orange',455,'Graps',4.54]

for x in lst:
    if type(x)== int or type(x)==float:
        print(x ,'is a numeric number.')


# 3

student={
    'Name':'Ali',
    'age':22
}
student['City']='Lahore'
student['Country']='Pakistan'

print(student)



#4

marks={
    'english':78,
    'physics':75,
    'urdu':54,
    'chemistry':74,
    
}
num=sum(marks.values())
print(num)



# 5

a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 10]
seen = []
dupes = []

for x in a:
    if x in seen:
        if x not in dupes:
            dupes.append(x)
    else:
        seen.append(x)        
print('Duplicate value is ',dupes)



# 6

student={
    'name':'Ali',
    'class':'Matric',
    'city':'Karachi'
}
checkKey='class'

if checkKey in student:
    print(f"Yes '{checkKey}' is already in dictionary.")
else:
     print(f"No '{checkKey}' does not exist .")    