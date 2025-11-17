running_total=0
while True:
    n=input("Please enter a number or quit to exit:")
    if n=="quit":
        break
    n=int(n)
    running_total=running_total+n
    print("Running Total:",running_total)
  
