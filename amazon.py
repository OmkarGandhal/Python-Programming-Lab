from easygui import *
import sys
sum=0
while 1:
    msgbox("Welcome to Amazon")

    msg ="What is your requirement?"
    title = "Amazon"
    choices = ["Mobiles", "T-shirts", "Shoes", "Watches"]
    choice = choicebox(msg, title, choices)
    #msgbox("You chose: " + str(choice))

   
    if choice=="Watches":
        msg1="Which Brand you choose"
        title1="Brands"
        choices1=["Fossil","Casio","Fastrack"]
        choice1 = choicebox(msg1,title1,choices1)
        if choice1 =="Fastrack":
                  m1="Best Prices are"
                  t1="Vendors"
                  cs1=["Mohit-Rs.2000","Ashok-Rs.2500"]
                  c1=boolbox(m1,t1,cs1)
                  if choice==1:
                       sum=sum+2500
                  elif choice==0:
                       sum=sum+2000

        elif choice1 =="Casio":
                  m1="Price is Rs.10000"
                  sum=sum+10000             
        elif choice1=="Fossil":
                  m1="Price is Rs.8000"
                  sum=sum+8000


    if choice=="Shoes":
        msg2="Which Brand you choose"
        title2="Brands"
        choices2=["Nike","Puma","Adidas"]
        choice2 = choicebox(msg2,title2,choices2)
        if choice2 =="Nike":
                  m2="Price is Rs.5000"
                  sum=sum+5000
        elif choice2 =="Puma":
                  m2="Price is Rs.3500"
                  sum=sum+3500             
        elif choice2=="Adidas":
                  m2="Price is Rs.8000"
                  sum=sum+8000

    if choice=="Mobiles":
        msg3="Which Brand you choose"
        title3="Brands"
        choices3=["Redmi","Honor","Oppo"]
        choice3 = choicebox(msg3,title3,choices3)
        if choice3 =="Redmi":
                  m3="Price is Rs.11000"
                  sum=sum+11000
        elif choice3 =="Honor":
                  m3="Price is Rs.9000"
                  sum=sum+9000             
        elif choice3=="Oppo":
                  m3="Price is Rs.18000"
                  sum=sum+18000 
    
    if choice=="T-shirts":
        msg4="Which Brand you choose"
        title4="Brands"
        choices4=["Flying machine","cello","U.S Polo"]
        choice4 = choicebox(msg3,title3,choices3)
        if choice4 =="Flying machine":
                  m4="Price is Rs.700"
                  sum=sum+700
        elif choice4 =="cello":
                  m4="Price is Rs.550"
                  sum=sum+550             
        elif choice4=="U.S Polo":
                  m4="Price is Rs.1100"
                  sum=sum+1100 
    

    msg = "Do you want to shop more?"
    title = "Please Confirm"
    if ccbox(msg, title):      #show a continue/cancel dialog   
       pass                    #user chose continue
    else:
         textbox(msg="bill",title="bill",text=str(sum))
         sys.exit(0)
