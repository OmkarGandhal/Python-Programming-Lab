from easygui import *
import sys
sum=0
while 1:
    sum=0
    msgbox("Welcome to Amusement World",image="amuse.jpg")  
    
    msgbox("please create your account in order to continue")
    
    y=enterbox("enter username")
    passwordbox(msg="Enter your password",title="Password")
    
    msgbox("welcome "+y)

    msg="Would you like to to get notifications about our offers?"
    title="Notifications"
    choice=ynbox(msg,title)

    msg ="What is your age?" 
    title = "Verification"   
    choices = ["Above 12","Below 12"] 
    choice = indexbox(msg, title, choices) 

    if choice==0:
     msg="Please select if you like nitro (Rs.250)"
     title="Nitro"
     choices= ["yes","no"]
     choice=indexbox(msg,title,choices,image="nitro.jpg")
     if choice==0:
       sum+=250
     

     msg="Please select if you like Danger Ranger (Rs.220)"
     title="Danger Ranger"
     choices= ["yes","no"]
     choice=indexbox(msg,title,choices,image="danger.jpeg")
     if choice==0:
       sum+=220
     

     msg="Please select if you like Dare to Drop (Rs.250)"
     title="D2D"
     choices= ["yes","no"]
     choice=indexbox(msg,title,choices,image="d.jpeg")
     if choice==0:
       sum+=250
    
   

    elif choice==1:
     msg="Please select if you like mini nitro (Rs.180)"
     title="Mini Nitro"
     choices= ["yes","no"]
     choice=indexbox(msg,title,choices,image="mn.jpeg")
     if choice==0:
       sum+=180
     
       

     msg="Please select if you like Mr India (Rs.220)"
     title="Mr India"
     choices= ["yes","no"]
     choice=indexbox(msg,title,choices,image="india.jpeg")
     if choice==0:
       sum+=220
     
       

     msg="Please select if you like Dora the explorer (Rs.125)"
     title="Dora Dora"
     choices= ["yes","no"]
     choice=indexbox(msg,title,choices,image="dora.jpeg")
     if choice==0:
       sum+=125
   
    x=enterbox("Please enter your preferred date to visit")
    msgbox(msg="See you on "+x ,image="cal.jpeg") 

    msgbox("Please use the promocode-vit50 if you're from VIT to avail 50% off")

    z=enterbox("Do you have a promocode?")
    if z=="vit50":
      a=sum*0.5
      textbox(msg="bill",title="bill",text=str(a))
    else:
      textbox(msg="bill",title="bill",text=str(sum))
sys.exit(0) 
