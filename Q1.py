# By Divya Modi
price_table = {
    1: {"data": 5, "price": 0},
    2: {"data": 5, "price": 10},
    3: {"data": 40, "price": 8},
    4: {"data": 50, "price": 5},
    5: {"data": 900, "price": 2},
    6: {"data": 0, "price": 1}
}

def calc_price(price_table, usuage):
    total_cost = 0
    for k in price_table:
        tier_data = price_table[k]["data"]
        price = price_table[k]["price"]
        if usuage <= tier_data or tier_data == 0:
        total_cost += (usuage*price)
        usuage = 0
        else:
        total_cost += (tier_data*price)
        usuage -= tier_data
        print(usuage, total_cost, k)
        if usuage == 0:
        break
    return total_cost

usuage = 1001
print(calc_price(price_table, usuage))