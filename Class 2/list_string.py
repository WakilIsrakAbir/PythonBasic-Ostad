running_total=0
while True:
    n=input("Please enter a number or quit to exit:")
    if n=="quit":
        break
    n=int(n)
    running_total=running_total+n
    print("Running Total:",running_total)


s="abc"
s1=s.lower()
s2=s.upper()
print(s1,s2)
s="this is a title"
s=s.title()
print(s)
print(len(s))
print(s[len(s)-1])
print(s[-1]


n=5
print(id(n))
n=n+15
print(id(n))


item=[1,2,3,"abc",10.5]
x="abc"
print(x in item)
print(item[0],item[1])
print(item[-1],item[-2])
n=len(item)
print(n)
print(type(item))

for n in item:
    print(n)

country="Bangla"
for c in country:
    print(c)
    
li=[1,2,3]
li[0]=4
print(li)


city="Dhaka"
li=list(city)
print(li)
li[0]='d'
print(li)

list=['d', 'h', 'a', 'k', 'a']
list[0]="D"
s=''.join(list)
print(s)


n1="5"
n2="5"
print(n1+n2)


#codingBat :string1    problem solve
#make_out_word
def make_out_word(out, word):
  s=out[0:2]+word+out[2:4]
  return s

#first_two
def first_two(str):
  if len(str) < 2:
    return str
  else:
    return str[0:2]

#without_end
def without_end(str):
  return str[1:-1]
    
#non_start
def non_start(a,b):
  return a[1:]+b[1:]


#list-1      problem solve
#first_last6
def first_last6(nums):
  if nums[0]== 6 :
    return True
  if nums[-1]==6  :
    return True
  else:
    return False
#0r
def first_last6(nums):
  if nums[0]== 6 or nums[-1]==6:
    return True
  else:
    return False

#make_pi
def make_pi():
  pi=[]
  pi.append(3)
  pi.append(1)
  pi.append(4)
  return pi

#sym3
def sum3(nums):
  return nums[0]+nums[1]+nums[2]
#or
    def sum3(nums):
  return sum(nums)

#reverse3
def reverse3(nums):
  nums[0],nums[2]=nums[2],nums[0]
  return nums

#sum2
def sum2(nums):
  if  len(nums)>=2:
    return nums[0]+nums[1]
  elif len(nums)==1:
    return nums[0]
  else:
    return 0

#Logic-1
#cigar-party
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars>=40
  else:
    return 40<=cigars<=60




