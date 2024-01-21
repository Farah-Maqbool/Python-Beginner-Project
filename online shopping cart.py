#Question 5: Online Shopping Cart
#Develop a Python program for an Online Shopping Cart. Create a function checkout(cart_total) that 
#takes the total cost of items in the cart and applies a discount based on the user's membership level. 
#Regular members get a 5% discount, premium members get a 10% discount, and VIP members get a 
#15% discount
#dictonaries
novels={"In the City of Gold and Silver":500,"Samarkand":600,"The Alchemist":1000,"The Gift":1200,"The Road to Mecca":1500,\
         "The Conference of the Birds":1300,"The Forty Rules of Love":2000,"The Kite Runner":800}
#printing the itmes in dictonari
for key, values in novels.items():
    print(f"{key}:{values}")
print("If you do not want to buy more novels, then type 'done'.")
#user input items list
user_input=[]
while "done" not in user_input:
        user=input("Enter Items: ")
        user_input.append(user)
user_input.remove("done")
#check price of user input novels name in novels dictonaries
cart_total=0
for novels_name in user_input:
     if novels_name in novels:
            num=novels[novels_name]
            cart_total+=num
print("Price =",cart_total)
print("""Regular Members=5% discount 
Premium Members=10% discount
VIP Members=15% discount""")

def checkout(cart_total):
    member=input("Enter Membership level (Regular Members, Premium Members, VIP Members): ")
    if member=="Regular Member":
          discount=cart_total*0.05
          total_cost=cart_total-discount
          return total_cost
    elif member=="Premium Member":
          discount=cart_total*0.1
          total_cost=cart_total-discount
          return total_cost
    elif member=="VIP Member":
          discount=cart_total*0.15
          total_cost=cart_total-discount
          return total_cost
result=checkout(cart_total)
print(result)




















