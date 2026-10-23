def place_order(item):
    print("order placed:  your order is ",item)

def calculate_total(item):
    base_price = 25.5
    VAT = 0.15
    total= (base_price +len(item))*(1+VAT)
    return total
def get_order():
    print('preparing order..........')
    return 'order_ready'

myfood=input('What would you like')
place_order(myfood)
order_total = calculate_total(myfood)
print('order total =   ',order_total)
print(get_order())


