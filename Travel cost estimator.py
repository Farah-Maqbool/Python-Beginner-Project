# Travel cost estimator
#user choose destination
choose_destination=input("Which city (Quetta or Gilgit-Baltistan) are you planning to visit?  ")
#user budget
budget=int(input("What is your budget? "))
# user want luxury or not
luxury=input("Would you like a luxury option, or not? ")
#If user choose Quetta
def Quetta(budget,luxury):
    #total cost
    total_cost=0
    # get transport input from user
    transport=input("How do you plan to travel to your destination? (Plane or Car) ")
    trans={"Car":15000,"Plane":25000}
    if transport in trans:
        total_cost+=trans[transport]
    #get accomodation from user
    accommodation=input("Where do you want to live (Hotel or Guest house)? ")
    accommo={"Hotel":15000,"Guest House":10000}
    accommodation_value=0
    if luxury=="yes" and accommodation in accommo:
        accommodation_value+=15000
        accommodation_value+=accommo[accommodation]
    elif luxury=="no" and accommodation in accommo:
        accommodation_value+=accommo[accommodation]
    total_cost+=accommodation_value
    #get activities from user
    activities=input("Do you want to go Hiking or visit different places in Quetta? ")
    acti={"Guider":4000,"Taxi":5000}
    if "Hiking" in activities:
        guider=input("Do you want guider or not: ") 
        if guider=="yes":
            total_cost+=acti["Guider"]
    elif "Places" in activities:
        taxi=input("Do you have any transport for visiting different places or not? ")
        if taxi=="no":
            total_cost+=acti["Taxi"]
    #total cost
    if total_cost>budget:
        return f"Total cost is {total_cost} and your budget is {budget}. It is out of budget "
    elif total_cost<budget:
        return f"Total cost is {total_cost} and your budget is {budget}. It is within budget"
    else:
        return f"Total cost is {total_cost} and your budget is {budget}. The budget and the amount are equal"
    
# if user choose gilgit baltistan
def Gilgit_Baltistan(budget,luxury):
    #total cost
    total_cost=0
    # get transport input from user
    transport=input("How do you plan to travel to your destination? (Plane or Car) ")
    trans={"Car":20000,"Plane":25000}
    if transport in trans:
        total_cost+=trans[transport]
    #get accomodation from user
    accommodation=input("Where do you want to live (Hotel or Guest house)? ")
    accommo={"Hotel":20000,"Guest House":10000}
    accommodation_value=0
    if luxury=="yes" and accommodation in accommo:
        accommodation_value+=20000
        accommodation_value+=accommo[accommodation]
    elif luxury=="no" and accommodation in accommo:
        accommodation_value+=accommo[accommodation]
    total_cost+=accommodation_value
    #get activities from user
    activities=input("Do you want to go Hiking or visit different places in Quetta? ")
    acti={"Guider":7000,"Taxi":8000}
    if "Hiking" in activities:
        guider=input("Do you want guider or not: ") 
        if guider=="yes":
            total_cost+=acti["Guider"]
    elif "Places" in activities:
        taxi=input("Do you have any transport for visiting different places or not? ")
        if taxi=="no":
            total_cost+=acti["Taxi"]
    #total cost
    if total_cost>budget:
        return f"Total cost is {total_cost} and your budget is {budget}. It is out of budget "
    elif total_cost<budget:
        return f"Total cost is {total_cost} and your budget is {budget}. It is within budget"
    else:
        return f"Total cost is {total_cost} and your budget is {budget}. The budget and the amount are equal"

    
if choose_destination=="Quetta":
    result=Quetta(budget,luxury)
    print(result)
elif choose_destination=="Gilgit-Baltistan":
    result=Gilgit_Baltistan(budget,luxury)
    print(result)     
else:
    print(f"{choose_destination} data is not available")       
        

















