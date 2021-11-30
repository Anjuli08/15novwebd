#Q1)-------
#Q2)-------
a=5**9
print(a)


a=3//2
print(a)

a=7//3
print(a)

a=7/3
print(a)

a = 6==6
print(a)

a=20
a+=30
a%=3
print(a)

print(True * False)


print(True & False)

print(True and False)

print(((6>3) and (7<4) or (18==3)) and (9>3))

print(True is False)

print(False in 'False')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool

print(((True == False) or (False > True)) and (False <= True))


#Q3)-----------------------------------------

s1='Nice to have it'
s2='here'
print(s1,s2)


#Q4)------------------------------------

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#Q5)------------------------------------

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a = [s1]+a+[s2]
print(a)

#Q6)------------------------------------

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]

for i in numbers:
	if(i==237):
		break
	elif(i%2==0):
		print(i)

#Q7)------------------------------------

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)



#Q8)---------------------------------------------


string = input('enter the string to be checked: ')

alpha = 'abcdefghijklmnopqrstuvwxyz'
string=string.lower()
f=0
for i in alpha:
    if i not in string:
        f =1
        break

if flag==1:
    print('False')
else:
    print('True')
    


#Q9)-------------------------------------------

s=int(input())
a=(s+(s*10+s)+(s*100+s*10+s))
print(a)


#Q10)-----------------------------------------------

s=input("Enter a string")
l=s.split("#")
x=l[0].split(' ')
for i in range(len(x)):
    x[i]=int(x[i])
y=l[1].split(' ')
for i in range(len(y)):
    y[i]=int(y[i])
print(x)
print(y)


#Q11)---------------------------------------------------

sent=input("enter the words: ")
enter the words: without,hello,bag,world
sent=sent.split(",")
sent.sort()
print((',').join(sent))


#Q12)-------------------------------------------------

d={'Student' : ['Rahul','Kishore','Vidhya','Raakhi'],'Marks' : [57,87,67,79]}
max=0
idx=-1
for i in d['Marks']:
    idx+=1
    if(max<i):
        max=i
        pos=idx
print(d['Student'][pos])


#Q13)----------------------------------------------------

s=input("enter the sentence: ")
letters =0
digits=0
for i in s:
    if i.isalpha():
        letters+=1
    if i.isdigit():
        digits+=1
        
print("LETTERS ", letters)
print("DIGITS ", digits)



#Q14)---------------------------------------------

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
s=input('Enter a Subject: ')
l1=d['Name']
l2=[]
l3=[]
l4=d['Ratings']
l5=[]
sub=d['Subject']
for i in range(len(sub)):
    if sub[i]==s:
        l2+=[sub[i]]
        l3+=[l1[i]]
        l5+=[l4[i]]
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)


#Q15)--------------------------------------------




#Q16)--------------------------------------------

import math
x,y=0,0

while True:
    step = input('Type up, down, left right with corresponding number: ')
    if step =='':
        break
    else:
        step = step.split(' ')
        if step[0]=='UP':
            y+=int(step[1])
        elif step[0]=='DOWN':
            y-=int(step[1])
        elif step[0]=='LEFT':
            x-=int(step[1])
        elif step[0]=='RIGHT':
            x+=int(step[1])

b= math.sqrt(x**2 + y**2)
c=int(b)
print('distance: ',c)




