a=20.0
b=30
c=a+b
print(c)
print(type(a),type(b),type(c))

print()

x='abc'
y="def"
d=True
e=False
print(d,e,type(x),type(y),type(d),type(e))

print()

n1=10;
n2=3;
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1**n2)
print(n1/n2)
print(n1//n2)
print(n1%n2)
print(divmod(n1,n2))

print()

name="Wakil Israk Abir"
marks=90
grade="A+"
gpa=5.00
print(type(name),type(marks),type(grade),type(gpa))

print("---------------------------------")

for _ in range(5):
    print("Python")
    print("py")
print("Programming")

print()

n=10
for number in range(n):
    print(number)

print()

for i in range(5,8):
    print(i)

print()

for number in range(1,20,2):
    print(number)

print()

for number in range(5,101,7):
    print(number)

print()

total=0
for i in range(1,5):
    total=total+i

print()

total=0
for i in range(5):
    total=total+i
    print("Hi")

print()

total=1
for i in range(1,11):
    total=total*i
    print(total)
print(total)

print()

for i in range(20,0,-2):
    print(i)

print("------------------------------------")

def print_greetings(name):#parameter
    print("dear",name)
    print("I am Rajin Saleh")
print_greetings("Abir") #argument

print()

def add_two_number(n1,n2):
    return n1+n2
v=add_two_number(10,30)
print(v)

