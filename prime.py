start = 900 
end = 1000
 
for i in range(start,end):
  if i>1: # checking that number is positive
    for j in range(2,i): 
        if(i % j==0): # checking the number divisible by 'i'
            break
    else:
        print(i)
