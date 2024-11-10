# dizionari
# i dizionari sono strutture dati utili per memorizzare 
# informazioni in coppie chiave-valore (key:value). 
# Ogni elemento del dizionario è costituito da una chiave e un valore associato.
car = {
    'color':'red',
    'price':35_000.,
    'year':2024,
    'hybrid':True
}

# accedere ad una chiave

# tramite []

#car_color = car['color']
#print(car_color)

#car_weight = car['weight']
#print(car_weight)

# tramite metodo get() 

#car_price = car.get('price')
#print(car_price)

#car_weight = car.get('weight')
#print(car_weight)

#car_km = car.get('km','Non sono presenti i km percorsi')
#print(car_km)

#print('weight' in car)

# utilzzo dell'operatore in
# per verificare la presenza di una key
#print('weight' in car)

# metodi 

# keys()

#car_keys = car.keys()
#for key in car_keys:
#    print(key)

# values()

#car_values = car.values()
#for value in car_values:
#    print(value)

# items()

#car_items = car.items()
#for item in car_items:
#    print(item)

# rimuovere una coppia chiave-valore
# pop()
#removed_item = car.pop('year')
#for item in car.items():
#    print(item)

#print(removed_item)

# popitem()
# rimuove l'ultima coppia chiave-valore
#removed_item = car.popitem()
#for item in car.items():
#    print(item)

#print('Item rimosso:')
#print(removed_item)

# clear()
# rimuove tutti le coppie chiave-valore
#car.clear()
#for item in car.items():
#    print(item) 

# del rimuove il dizionario o qualsiasi variabile
#del car
#print(car)

# mutabilità

# mutare il valore di una chiave
#car['color'] = 'green'
#print(car.get('color'))

# aggiungere una nuova coppia chiave-valore
#car['km'] = 2_00000.
#for item in car.items():
#    print(item)

# funzioni utente
# creare una funzione

#punto = {
#    'color':'red',
#    'price':35_000.,
#    'year':2024,
#   'hybrid':True
#}

#panda = {
#    'color':'green',
#    'price':25_000.,
#    'year':2014,
#    'hybrid':False
#}

#discounted_price = panda['price'] * 0.7
#if discounted_price > 20_000.:
#    discounted_price -= 100
#    print(discounted_price)

#discounted_price = punto['price'] * 0.7
#if discounted_price > 20_000.:
#    discounted_price -= 100
#    print(discounted_price)

# DRY - DON'T REPEAT YOURSELF

# def è la keyword per definire una funzione

# price - parametro viene valorizzato nel momento in cui viene chiamata 
# la funzione in base all'argomento passato alla funzione
#def get_discounted_price(price):
#    discounted_price = price * 0.7 
#    if discounted_price > 20_000.:
#        discounted_price -= 100
#    print(discounted_price)


#get_discounted_price(panda['price']) # argomento posizionale passato alla funzione diventa parametro 
#get_discounted_price(price=punto['price']) # argomento keyword passato alla funzione diventa parametro

# le funzioni ricevono parametri in ingresso
# passati come argomento in fase di chiamata
# e possono restituire valori

#def get_discounted_price(price):
#    discounted_price = price * 0.7 
#    if discounted_price > 20_000.:
#        discounted_price -= 100
#    return discounted_price

#panda_disc_price = get_discounted_price(panda['price']) # argomento posizionale passato alla funzione diventa parametro 
#punto_disc_price = get_discounted_price(price=punto['price']) # argomento keyword passato alla funzione diventa parametro

#print(f'Il prezzo della panda scontato è: {panda_disc_price}€.')
#print(f'Il prezzo della punto scontato è: {punto_disc_price}€.')

# parametri funzione opzionali

#def get_discounted_price(price, bonus_discount=100):
#    discounted_price = price * 0.7 
#    if discounted_price > 20_000.:
#        discounted_price -= bonus_discount
#    return discounted_price

#panda_disc_price = get_discounted_price(panda['price'],200)
#punto_disc_price = get_discounted_price(punto['price'])

#print(f'Il prezzo della panda scontato è: {panda_disc_price}€.')
#print(f'Il prezzo della punto scontato è: {punto_disc_price}€.')

# parametri arbitrari

#user_1 = {
#    'first_name':'Mario',
#    'last_name':'Rossi',
#    'email':'mario.rossi@gmail.com'
#}

#user_2 = {
#    'first_name':'Giuseppe',
#    'last_name':'Verdi',
#    'email':'giuseppe.verdi@gmail.com'
#}

#user_3 = {
#    'first_name':'Andrea',
#    'last_name':'Bocelli',
#    'email':'andrea.bocelli@gmail.com'
#}

# parametro arbitrario definito con *
#def print_user_info(*user_list):
#    for user in user_list:
#        print(f'First Name: {user['first_name']}')
#        print(f'Last Name: {user['last_name']}')
#        print(f'Email: {user['email']}')
#        print()

# passiamo come argomento una lista di user preceduta da *
#print_user_info(*[user_1, user_2, user_3])

# scope
# globale variabili definite 
# nel corpo principale del nostro programma
# locale  variabili definite all'interno di una funzione

# globale
#punto = {
#    'color':'red',
#    'price':35_000.,
#    'year':2024,
#   'hybrid':True
#}

#panda = {
#    'color':'green',
#    'price':25_000.,
#    'year':2014,
#    'hybrid':False
#}

#def get_discounted_price(price):
		# la variabile discounted_price ha scope locale
		# in quanto definita all'interno di una funzione
#    discounted_price = price * 0.7 
#    if discounted_price > 20_000.:
#        discounted_price -= 100
#    return discounted_price

# funzioni ricorsive

#def say_hello():
#    print('Ciao')
#    say_hello()

#say_hello()

# calcolare il fattoriale tramite funzioni ricorsive
# 4! = 4*3*2*1 = 24

def factorial(n):
    print('-',n)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))