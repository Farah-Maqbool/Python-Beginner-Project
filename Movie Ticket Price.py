#Movie Ticket Pricw
def movie_ticket(age,day,member):
    week1=["Sunday","Saturday"]
    week2=["Monday","Tuesday","Wednesday","Thursday","Friday"]

    if age<18 and day in week1 :
        print("Your ticket price is 1000")
        if member=="Group":
            print("Discount 5% So your total amount is 950")
        elif member=="Family":
            print("Discount 10% So your total amoount is 900")
    elif age<18 and day in week2:
        print("Your ticket price is 1200")
        if member=="Group":
            print("Discount 5% So your total amount is 1150")
        elif member=="Family":
            print("Discount 10% So your total amoount is 1100")
    elif age<40 and age>18 and day in week1:
        print("Your ticket price is 1500")
        if member=="Group":
            print("Discount 5% So your total amount is 1450")
        elif member=="Family":
            print("Discount 10% So your total amoount is 1400")
    elif age<40 and age>18 and day in week2:
        print("Your ticket price is 1700")
        if member=="Group":
            print("Discount 5% So your total amount is 1650")
        elif member=="Family":
            print("Discount 10% So your total amoount is 1600")
    elif age>=40 and day in week1:
        print("Your ticket price is 1900")
        if member=="Group":
            print("Discount 5% So your total amount is 1850")
        elif member=="Family":
            print("Discount 10% So your total amoount is 1800")
    elif age>=40 and day in week2:
        print("Your ticket price is 2000")
        if member=="Group":
            print("Discount 5% So your total amount is 1950")
        else:
            print("Discount 10% So your total amoount is 1900")



age=int(input("Enter Age: "))
day=input("Enter Day: ")
member=input("Group or family: ")
# for group 5% discount for family 10%
movie_ticket(age,day,member)
