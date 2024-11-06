# dizionari
car = {
    'color':'red',
    'price':35_000.,
    'year':2024,
    'hybrid':True
}

#print(car['color'])

#print(car.get('price'))

#print(car.get('weight', 'Non è presente il pesoß'))

#print('weight' in car)

#for key in car.keys():
#    print(key)

#for value in car.values():
#    print(value)

#for item in car.items():
#    print(item)

#for key,value in car.items():
#    print(key, value)

# funzioni utente
# creare una funzione

# def è la keyword per definire una funzione

def get_discounted_price(price):
    discounted_price = price * 0.7
    if discounted_price > 20_000.:
        discounted_price -= 100
    #print(discounted_price)
    return discounted_price

car_disc_price= get_discounted_price(car['price'])
print(car_disc_price)