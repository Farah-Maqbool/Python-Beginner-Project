# Resturant Bill Calculator
#  Menu
Item={"Biryani":200,"Pizza":600,"Burger":100,"Fries":50,"Cake":500,"Chiken Seekh kabab":600,"Desi Chowmein":1000,"Chiken Tikka karahi":700}
for key, values in Item.items():
    print(key,values)
def bill(your_item,enter_discount,tax_rate,people):

    #cost
    total_cost=0
    for key1, values1 in your_item.items():
        for key2, values2 in Item.items():
            if key1==key2:
                cost=values1*values2
                total_cost+=cost

    print("Cost is",total_cost)
    #discount calculation
    discount_decimal=enter_discount/100
    discount_point=total_cost*discount_decimal
    value_after_discount=total_cost-discount_point
    discount=value_after_discount
    print("The Amount after the discount is=",discount)
    #tax Calculation
    tax_decimal=tax_rate/100
    tax_point=total_cost*tax_decimal
    value_after_tax=discount+tax_point
    amount=value_after_tax
    print("The amount after tax is=",value_after_tax)
    # how many amount paid by 1 person
    one_person=int(amount/people)
    print("Total Amount",amount)
    print("One Person will pay the",one_person,"Rupees")

your_item={}
print('If you want to stop enter "Stop"')
while True:

    enter_item=input("Enter Item: ")
    enter_quantity=input("Enter Quantity: ")
    if enter_item=="stop" and enter_quantity=="stop":
        break
    else:
        your_item[enter_item]=int(enter_quantity)
enter_discount=int(input("Enter Discount: "))
tax_rate=int(input("Enter Tax Rate: "))
people=int(input("Number of People: "))
bill(your_item,enter_discount,tax_rate,people)
