def armstrong(x):                  #define a function
  sum=0                             #initialize 'sum=0'
  t=x                               #store input value in variable 't'
  while(t>0):                       #check t>0;if yes,proceed
     d=t%10                         #store last digit in another variable 'd'
     sum+=d**3                      #cube the no.d and add to 'sum'
     t=t//10                        #removes remaining digits aside
  if sum==x:                        #check sum=t;if yes, proceed
     return 'Armstrong'             #print
  else:                             #if no,proceed here
     return 'not Armstrong'         #print
x=int(input())                     #takes input from user 
print(armstrong(x))                #call function 
