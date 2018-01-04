

def price_to_pay(food_cost, tip_percentage=.15,
                 tax_percentage=.101, discount=0,
                 additional_cost=0):
    tax = food_cost * tax_percentage
    tip = food_cost * tip_percentage
    return food_cost + tax + tip - discount + additional_cost
