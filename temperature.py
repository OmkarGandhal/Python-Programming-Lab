from easygui import *
import sys
while 1:
    
            
      msg="Convert the temperature ?"
      title="Temperature conersion"
      choices=["Celsius", "Fahrenheit"]
      choice=buttonbox(msg,title,choices)

      if choice=="Celsius":
         f=int(enterbox("Enter the Fahrenheit Temperature:"))
         c=5*(f-32)/9
         msgbox("Celsius Temp. is :" + str(c))

      if choice=="Fahrenheit":
         c1=int(enterbox("Enter the Celsius Temperature:"))
         f1=((9*c1)/5)+32
         msgbox("Fahrenheit Temp. is :" + str(f1))

   
