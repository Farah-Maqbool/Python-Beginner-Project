# Resturant Bill Calculator
#  Menu
Item={"Biryani":200,"Pizza":600,"Burger":100,"Fries":50,"Cake":500,"Chiken Seekh kabab":600,"Desi Chowmein":1000,"Chiken Tikka karahi":700}
for key, values in Item.items():
    print(key,values)
def bill(enter_item,enter_quantity,enter_discount,tax_rate,people):
    #cost
    cost=1
    for key, values in Item.items():
        if key==enter_item:
            cost=enter_quantity*values
    print("Cost is",cost)
    #discount calculation
    discount_decimal=enter_discount/100
    discount_point=cost*discount_decimal
    value_after_discount=cost-discount_point
    discount=value_after_discount
    print("The Amount after the discount=",discount)
    #tax Calculation
    tax_decimal=tax_rate/100
    tax_point=cost*tax_decimal
    value_after_tax=discount+tax_point
    amount=value_after_tax
    print("The amount after cutting tax=",value_after_tax)
    # how many amount paid by 1 person
    one_person=int(amount/people)
    print("Total Amount",amount)
    print("One Person will pay the",one_person,"Rupees")




enter_item=input("Enter Item: ")
enter_quantity=int(input("Enter Quantity: "))
enter_discount=int(input("Enter Discount: "))
tax_rate=int(input("Enter Tax Rate: "))
people=int(input("Number of People: "))
bill(enter_item,enter_quantity,enter_discount,tax_rate,people)





















