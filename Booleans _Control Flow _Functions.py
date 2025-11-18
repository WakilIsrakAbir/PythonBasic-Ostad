#1
#12
#123
#1234
print("Number Pattern")
row=5
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end='')  #empty line after each row
    print("")

#count the total number of digits in a number
number=15846865
counter=0
while(number !=0):
    number=number//10
    counter=counter+1
print("Total digits:",counter)

#Write a program to create a function that takes two arguments,name and age,and print there value.
#1.def keyword for function creation
#2.define 2 parameters in the function whice is name and age
#3.print them inside the function
#4.Call the function by passing name and age 

def test(name,age):
    print(name,age)
test("Abir",30)

