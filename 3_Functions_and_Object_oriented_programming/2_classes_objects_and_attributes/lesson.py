# OOP - Object Oriented Programming

'''
car_1 = {
    'brand':'Fiat',
    'max_speed':200,
    'year':2020,
    'is_electric':True
}

car_2 = {
    'brand':'Ferrari',
    'max_speed':300,
    'year':2021,
    'is_electric':False
}

def drive_fast(car_brand, car_speed):
    print(f'La {car_brand} corre a {car_speed} km/h')

drive_fast(car_1['brand'], car_1['max_speed'])
drive_fast(car_2['brand'], car_2['max_speed'])
'''
# La programmazione orientata agli oggetti (OOP) 
# ci consente di rappresentare entità reali attraverso classi, 
# che definiscono un modello per la creazione di oggetti. 

# La classe serve come modello per descrivere 
# gli attributi (caratteristiche) e i metodi (azioni) 
# comuni a un certo tipo di oggetto. 
# Un oggetto è una singola istanza di una classe, con valori 
# specifici per ogni attributo che lo rendono unico.

# In Python, è convenzione utilizzare la notazione PascalCase per i nomi delle classi.
# Esempio: FastCar, Car, Person
class Car:
    
    # Metodo speciale di inizializzazione o costruttore (__init__)
    # È preceduto e seguito da doppio underscore e viene automaticamente chiamato
    # quando creiamo un nuovo oggetto della classe.
    # Il costruttore consente di definire e assegnare gli attributi necessari per ogni oggetto.
    
    def __init__(self, brand, max_speed, year, is_electric):
        # 'self' rappresenta l'istanza attuale dell'oggetto ed è obbligatorio.
        # Attraverso 'self', possiamo assegnare gli argomenti ricevuti dal costruttore agli attributi dell'oggetto.
        
        #print('self',self)
        # attributi di istanza
        self.brand = brand          
        self.max_speed = max_speed  
        self.year = year            
        self.is_electric = is_electric

    def drive_fast(self):
        print(f'La {self.brand} corre a {self.max_speed} km/h')
        return self.max_speed
    
    # ai metodi è possibile passare parametri esterni alla classe
    # e utilizzarli ad esempio per effettuare calcoli 
    def get_maximum_boosted_speed(self, boosted_speed):
        return self.max_speed + boosted_speed

# Creazione di oggetti
# Per creare un oggetto, si chiama la classe come se fosse una funzione, passando gli argomenti richiesti dal costruttore.
# Il costruttore viene eseguito immediatamente, e gli argomenti sono assegnati agli attributi dell'oggetto tramite 'self'.
# In questo modo, possiamo istanziare nuovi oggetti della classe Car e assegnarli a variabili.

car_1 = Car('Fiat', 200, 2020, True)   
car_2 = Car('Ferrari', 300, 2021, False)


#print('car_1',car_1)
#print('car_2',car_2)

#max_spped_car_1 = car_1.drive_fast()
#max_spped_car_2 = car_2.drive_fast()

#print(max_spped_car_1)
#print(max_spped_car_2)

maximum_boosted_speed_car_1 = car_1.get_maximum_boosted_speed(20)
print(f'La nuova velocità massima della macchina {car_1.brand} è {maximum_boosted_speed_car_1}')

# è possibile aggiungere attributi d'istanza
# al di fuori della classe
# questi attributi cosi definiti faranno riferimento 
# all'istanza associata e non saranno disponibili
# per le altre istanze
#car_1.weight = 1500
#print(car_1.weight)

# attraverso la keyword del
# è possibile rimuovere attributi d'istanza
# da un istanza specifica
del car_1.is_electric

print(car_1.is_electric) # genera errore -> 'Car' object has no attribute 'is_electric'
print(car_2.is_electric)