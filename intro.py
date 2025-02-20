a = 10
b = 20
c = a+b
d = a-b
e=a*b
f=a/b
print ( "Sum is =",c)
print ( "Difference is =",d)
print( "product is =",e)
print("Division is =",f)

g=("software")
print(g.capitalize())

h = "noiya" 
i = list(h)
old="y"
new="d"
index=i.index(old)
i[index]=new
new_string=''.join(i)
print(new_string)

aa="app wars technologies"
print(aa.split())

ab="gyan prakash"
print(ab.capitalize())
print(ab.split())

str="Welcome \t to \t the \t appwars."
str2 = str.expandtabs(1)
str3 = str.expandtabs(2)
str4 = str.title()
str5 = str.capitalize()

print(str2)
print(str3)
print(str4) 
print(str5)

x= 10
y= 20 
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>y and y>x)
print(x>y or y>x)
print(y>x and x!=y)

z = 21
if not z:
    print("Boolean value of  z is true")
if not (z%3 == 0 or z%5 == 0):
    print(z," is not divisible by either 3 or 5")
else:
    print(z," is divisible by either 3 or 5")    

    list = [[1,2,3,4],  ["ritesh","manish","ribu"],[11.1,11.2,11.3]]
    print(len(list))

    print(list[1][1])


list1= ["manish","rohit"]
list1.append("mohit")
print(list1)
list1.append(["abhishek","virender"])
print(list1)
list2=["dhoni"]
list2.extend(["kohli","rohit"])
print(list2)
list2.extend(("pant","hardik"))
print(list2)


list3=[2,5,8,12]
new_list3 = list3.pop(2)
print(list3)

list4=[1,2,3,4,5,6]
new_list4 = list4.pop()
print(list4)
