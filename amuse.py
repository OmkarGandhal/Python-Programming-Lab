from easygui import *
import sys
sum=0
while 1:
    msgbox("Welcome to Amusement World")

    msg ="What is your age?"
    title = "Verification"
    choices = ["Above 12","Below 12"]
    choice = buttonbox(msg, title, choices)
    
    if  choice=="Below 12":
         msg1="You can enjoy the following rides"
         title1="Available Rides"
         choices1=["Pirates Bay - Rs.200","Mini slide-Rs.250","Danger Ranger-Rs.200","Break Dance-Rs.270","Dashing Cars-Rs.150","Transformers rides-Rs.250"]
         choice1=buttonbox(msg1,title1,choices1)
         if choice1=="Pirates Bay - Rs.200" :
             sum=sum+200
         elif choice1=="Mini slide-Rs.250":
             sum=sum+250
         elif choice1=="Danger Ranger-Rs.200":
             sum=sum+200
         elif choice1=="Break Dance-Rs.270":
             sum=sum+270
         elif choice1=="Dashing Cars-Rs.150":
             sum=sum+150
         elif choice1=="Transformers rides-Rs.250":
             sum=sum+250

    if choice=="Above 12":
         msg2="You can enjoy the following rides"
         title2="Available Rides"
         choices2=["Dashing Cars-Rs.150","Transformers rides-Rs.250","Nitro-350","Swirl pool-400","Shot n Drop - 300","Free Fall- 370","Mr. India - 300"]
         choice2=buttonbox(msg2,title2,choices2)
         if choice2=="Dashing Cars-Rs.150":
             sum=sum+150
         elif choice2=="Transformers rides-Rs.250":
             sum=sum+250
         elif choice2=="Nitro-Rs.350":
             sum=sum+350
         elif choice2=="Swirl pool-400":
             sum=sum+400
         elif choice2=="Shot n Drop - 300":
             sum=sum+300
         elif choice2=="Free Fall- 370":
             sum=sum+370
         elif choice2=="Mr. India - 300":
             sum=sum+300
   
    msg = "Do you want to shop more?"
    title = "Please Confirm"
    if ccbox(msg, title):      #show a continue/cancel dialog   
       pass                    #user chose continue
    else:
         textbox(msg="bill",title="bill",text=str(sum))
         sys.exit(0)
        


