#Movie Ticket Price
# discount function
def discount(discount_rate,value):
    return value-((discount_rate/100)*value)
# value check function
def movie_ticket(age,day,member):
    week1=["Sunday","Saturday"]
    value=0
    if age=="Child":
        if day in week1:
            value=500
        else:
            value=600
    elif age=="Adult":
        if day in week1:
            value=700
        else:
            value=800
    elif age=="Adult":
        if day in week1:
            value=900
        else:
            value=1000
    # Discount for family and group
    if member=="Family":
        discount_rate=int(input("Enter Discount rate for family: "))
        result=discount(discount_rate,value)
        return result
    elif member=="Group":
        discount_rate=int(input("Enter Discount rate for group: "))
        return discount(discount_rate,value)



age=input("Enter (Adult, Child, Senior): ")

day=input("Enter Day: ")
member=input("Group or Family: ")
# for group 5% discount, for family 10%
result=movie_ticket(age,day,member)
print(result)
