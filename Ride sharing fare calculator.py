"""Ride-Sharing Fare Calculator
You are working on a Ride-Sharing Fare Calculator. Develop a Python function calculate_fare(distance, 
time_of_day) that takes the distance of the ride and the time of day as input and returns the fare. Apply 
a 20% surcharge during peak hours (8 am - 10 am and 5 pm - 7 pm) and a 10% discount for late-night rides (10 pm - 5 am)."""
print("Ride For you")
print("Only Available for 100 km distance")
print("Peak hours 8am-10am and 5pm-7pm 20% Surcharge")
print("10% Discount in late night rides (10pm-5pm)")
print("""(1km-20km) price is 300
(20km-40km) price is 600
(40km-60km) price is 900
(60km-80km) price is 1200
(80km-100km) price is 1500
""")
def calculate_fare(distance,time_of_day,am_pm):
    if (distance>0 and distance<=20):
            if (am_pm=="am-am" or am_pm=="pm-pm") and ((time_of_day>=8 and time_of_day<=10) or (time_of_day>=5 and time_of_day<=7)):
                cost=300
                surcharge=cost*0.002
                total=cost+surcharge
                return total
            elif am_pm=="pm-am" and (time_of_day>=10 and time_of_day<=12 and time_of_day>=5):
                cost=300
                discount=cost*0.1
                total=cost-discount
                return total
            else:
                 cost=300  
                 return cost
    elif (distance>20 and distance<=40) :
            if (am_pm=="am-am" or am_pm=="pm-pm") and ((time_of_day>=8 and time_of_day<=10) or (time_of_day>=5 and time_of_day<=7)):
                cost=600
                surcharge=cost*0.002
                total=cost+surcharge
                return total
            elif am_pm=="pm-am" and (time_of_day>=10 and time_of_day<=12 and time_of_day>=5):
                cost=600
                discount=cost*0.1
                total=cost-discount
                return total  
            else:
                 cost=600
                 return cost  
    elif (distance>40 and distance<=60) :
            if (am_pm=="am-am" or am_pm=="pm-pm") and ((time_of_day>=8 and time_of_day<=10) or (time_of_day>=5 and time_of_day<=7)):
                cost=900
                surcharge=cost*0.002
                total=cost+surcharge
                return total
            elif am_pm=="pm-am" and (time_of_day>=10 and time_of_day<=12 and time_of_day>=5):
                cost=900
                discount=cost*0.1
                total=cost-discount
                return total
            else:
                 cost=900  
                 return cost
    elif (distance>60 and distance<=80) :
            if (am_pm=="am-am" or am_pm=="pm-pm") and ((time_of_day>=8 and time_of_day<=10) or (time_of_day>=5 and time_of_day<=7)):
                cost=1200
                surcharge=cost*0.002
                total=cost+surcharge
                return total
            elif am_pm=="pm-am" and (time_of_day>=10 and time_of_day<=12 and time_of_day>=5):
                cost=1200
                discount=cost*0.1
                total=cost-discount
                return 
            else:
                 cost=1200  
                 return cost
    elif (distance>80 and distance<=100) :
            if (am_pm=="am-am" or am_pm=="pm-pm") and ((time_of_day>=8 and time_of_day<=10) or (time_of_day>=5 and time_of_day<=7)):
                cost=1500
                surcharge=cost*0.002
                total=cost+surcharge
                return total
            elif am_pm=="pm-am" and (time_of_day>=10 and time_of_day<=12 and time_of_day>=5):
                cost=1500
                discount=cost*0.1
                total=cost-discount
                return total 
            else:
                 cost=1500  
                 return cost     
distance=int(input("Enter Distance: "))
time_of_day=int(input("Enter Time of day: "))
am_pm=input("Enter am or pm: ")
result=calculate_fare(distance,time_of_day,am_pm)
print("Total Cost is",result,"Rupees")
