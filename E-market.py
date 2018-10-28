from easygui import *
import sys
sum=0
while 1:
    msgbox("Welcome to E-market")

    msg ="What is your requirement?"
    title = "E-market"
    choices = ["Mobiles", "T-shirts", "Shoes", "Watches"]
    choice = choicebox(msg, title, choices)
    #msgbox("You chose: " + str(choice))

   
    if choice=="Watches":
        msg1="Which Brand you choose"
        title1="Brands"
        choices1=["Fossil","Casio","Fastrack"]
        choice1 = choicebox(msg1,title1,choices1)
        if choice1 =="Fastrack":
                  m11="Best Prices are"
                  t11="Vendors"
                  cs11=["Overseas-Rs.2000","Technos-Rs.2500"]
                  c11=boolbox(m11,t11,cs11)
                  if c11==0:
                       sum=sum+2500
                  elif c11==1:
                       sum=sum+2000

        elif choice1 =="Casio":
                  m12="Best Prices are"
                  t12="Vendors"
                  cs12=["Overseas-Rs.10000","Technos-Rs.12000"]
                  c12=boolbox(m12,t12,cs12)
                  if c12==0:
                       sum=sum+12000
                  elif c12==1:
                       sum=sum+10000
 
        elif choice1=="Fossil":
                  m13="Best Prices are"
                  t13="Vendors"
                  cs13=["Overseas-Rs.9000","Technos-Rs.9800"]
                  c13=boolbox(m13,t13,cs13)
                  if c13==0:
                       sum=sum+9800
                  elif c13==1:
                       sum=sum+9000



    if choice=="Shoes":
        msg2="Which Brand you choose"
        title2="Brands"
        choices2=["Nike","Puma","Adidas"]
        choice2 = choicebox(msg2,title2,choices2)
        if choice2 =="Nike":
                  m21="Best Prices are"
                  t21="Vendors"
                  cs21=["Overseas-Rs.4500","Woods-Rs.5000"]
                  c21=boolbox(m21,t21,cs21)
                  if c21==0:
                       sum=sum+5000
                  elif c21==1:
                       sum=sum+4500

                 
        elif choice2 =="Puma":
                  m22="Best Prices are"
                  t22="Vendors"
                  cs22=["Overseas-Rs.3200","Woods-Rs.2500"]
                  c22=boolbox(m22,t22,cs22)
                  if c22==0:
                       sum=sum+2500
                  elif c22==1:
                       sum=sum+3200
             
        elif choice2=="Adidas":
                  m23="Best Prices are"
                  t23="Vendors"
                  cs23=["Overseas-Rs.7500","Woods-Rs.8400"]
                  c23=boolbox(m23,t23,cs23)
                  if c23==0:
                       sum=sum+8400
                  elif c23==1:
                       sum=sum+7500

    if choice=="Mobiles":
        msg3="Which Brand you choose"
        title3="Brands"
        choices3=["Redmi","Honor","Oppo"]
        choice3 = choicebox(msg3,title3,choices3)
        if choice3 =="Redmi":
                  m31="Best Prices are"
                  t31="Vendors"
                  cs31=["Overseas-Rs.8500","Sham-Rs.11000"]
                  c31=boolbox(m31,t31,cs31)
                  if c31==0:
                       sum=sum+11000
                  elif c31==1:
                       sum=sum+8500
            
        elif choice3 =="Honor":
                  m32="Best Prices are"
                  t32="Vendors"
                  cs32=["Overseas-Rs.9000","Sham-Rs.10000"]
                  c32=boolbox(m32,t32,cs32)
                  if c32==0:
                       sum=sum+10000
                  elif c32==1:
                       sum=sum+9000
                          
        elif choice3=="Oppo":
                  m33="Best Prices are"
                  t33="Vendors"
                  cs33=["Overseas-Rs.15500","Sham-Rs.17000"]
                  c33=boolbox(m33,t33,cs33)
                  if c33==0:
                       sum=sum+17000
                  elif c33==1:
                       sum=sum+15500
                   
    
    if choice=="T-shirts":
        msg4="Which Brand you choose"
        title4="Brands"
        choices4=["Flying machine","cello","U.S Polo"]
        choice4 = choicebox(msg4,title4,choices4)
        if choice4 =="Flying machine":
                 m41="Best Prices are"
                 t41="Vendors"
                 cs41=["Classic collection-Rs.750","Casual-Rs.800"]
                 c41=boolbox(m41,t41,cs41)
                 if c41==0:
                      sum=sum+800
                 elif c41==1:
                      sum=sum+750
        elif choice4 =="cello":
                 m42="Best Prices are"
                 t42="Vendors"
                 cs42=["Classic collection-Rs.950","Casual-Rs.800"]
                 c42=boolbox(m42,t42,cs42)
                 if c42==0:
                      sum=sum+800
                 elif c42==1:
                      sum=sum+950
                           
        elif choice4=="U.S Polo":
                 m43="Best Prices are"
                 t43="Vendors"
                 cs43=["Classic collection-Rs.1150","Casual-Rs.1300"]
                 c43=boolbox(m43,t43,cs43)
                 if c43==0:
                      sum=sum+1300
                 elif c43==1:
                      sum=sum+1150
          
    

    msg = "Do you want to shop more?"
    title = "Please Confirm"
    if ccbox(msg, title):      #show a continue/cancel dialog   
       pass                    #user chose continue
    else:
         textbox(text=choice+str(sum))
         textbox(msg="bill",title="bill",text=str(sum))
sys.exit(0)
