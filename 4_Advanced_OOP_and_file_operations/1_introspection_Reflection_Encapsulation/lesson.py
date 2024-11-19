#class Car:

    # attributi di classe
#    wheels = 4
#    total_built_car = 0
#    total_driven_km = 0

#    def __init__(self, brand, max_speed, year, is_electric):
        # attributi di istanza
    #    self.brand = brand
    #    self.year = year
    #    self.max_speed = max_speed
    #    self.is_electric = is_electric
    #    Car.total_built_car += 1
    
    #def drive(self, kilometers):
    #    print(f'La {self.brand} ha percorso {kilometers} km.')
    #    Car.total_driven_km += kilometers

    # sovrascriviamo il metodo __str__()
    #def __str__(self):
    #    return f'Brand: {self.brand}, Year: {self.year}, Max Speed: {self.max_speed}, Electric: {self.is_electric}'


#car1 = Car('Fiat', 200, 2020, True)   
#car2 = Car('Ferrari', 300, 2021, False)

#print(car1.wheels)
#print(car2.wheels)

#print(Car.wheels)

#print(Car.total_built_car)

#car1.drive(30)
#car2.drive(50)
#car1.drive(20)

#print(Car.total_driven_km)

# in questo modo stiamo creando un attributo di istanza
# che sovrascrive l'attributo di classe 
# da questa istanza non sarà più possibile accedere al reale
# valore dell'attributo di classe
#car1.total_driven_km = 10

#print(car1.total_driven_km)
#print(Car.total_driven_km)

# Introspection e reflection
# gli oggetti in python sono molto dinamici e mutabili
# possiamo cambiare i valori degli attributi di istanza e di classe
# possiamo cambiare anche gli attributi stessi modificando l'intera struttura della classe

# possiamo ad esempio aggiungere nuovi attributi di istanza

# in questo modo abbiamo effettuato una modifica alla struttura della nostra classe
# che prima di questa modifca rispettava la struttura definita all'interno del metodo costruttore
#car1.weight = 1500

# possiamo anche cancellare un attributo di istanza
#del car1.is_electric

# l'introspection è la capacità di una classe o di un oggetto di una classe
# di ottenere informazioni su se stessa come attributi, valori ..

# un esempio di una funzione di introspezione è la funzione type
# ci restituisce il data-type del nostro oggetto
#print(type(car1))

# dir()
# la funzione dir ci permette di visualizzare
# tutti gli attributi di istanza, di classe e i metodi
# che possiede un oggetto
#print(dir(car1))

# possiamo chiamare la funzione dir 
# anche sulla classe stessa

# la differenza nel chiamare la funzione
# direttamente sull'oggetto oppure sulla classe
# è che chiamando la funzione sulla classe stessa 
# non visualizziamo gli attributi di istanza
# ma solo quelli di classe
#print(dir(Car))

# chiamando la funzione dir senza argomenti
# otteniamo tutti gli elementi presenti nello scope attuale
# dove abbiamo effettuato la funzione dir
#print(dir())

# hasattr()
# serve per verificare se un istanza ha un attributo
# restituisce un valore booleano

#print(hasattr(car1, 'brand'))
#print(hasattr(car1, 'is_electric'))

# possiamo chiamare la funzione hasattr()
# per verificare la presenza di un metodo
#print(hasattr(car1, 'drive'))

# possiamo chiamare anche sulla classe stessa
# ma se cerchiamo di accedere ad attributi di istanza
# otteremo sempre False

#print(hasattr(Car, 'brand'))

# il metodo __dict__
# restituisce in forma di dizionario
# gli attributi e relativi valori appartenenti ad una istanza
#print(car1.__dict__)

# possiamo chiamarlo anche sulla classe stessa
# ottenendo solo informazioni riguardo attributi di classe
#print(Car.__dict__)

# il metodo __module__
# restituisce informazione riguardo
# in quale file è stata definita l'istanza 
# o la classe su cui chiamiamo il metodo
#print(car1.__module__)
#print(Car.__module__)

# il metodo __str__()
# metodo di rappresentazione del nostro oggetto
# se non ridefinito fornisce informazioni 
# riguardo l'oggetto come il modulo in cui è stato definito
# il data-type e indirizzo di locazione in memoria
#print(car1.__str__())

# la reflection invece è la capacità di una classe o di un oggetto
# di modificare se stessa

# in questo modo stiamo mutando l'oggetto
# in maniera statica

#car1.weight = 1500
#car1.is_electric = False
#del car1.is_electric

# la reflection fornisce metodi per mutare oggetti
# in modo dinamico durante l'esecuzione del nostro codice

# setattr()
# permette di aggiungere o modificare (se presente) un attributo
# accetta 3 argomenti:
# - l'oggetto interessato
# - l'attributo che vogliamo aggiungere/modificare
# - il valore dell'attributo

# modifica attributo is_electric
#setattr(car1,'is_electric',False)
#print(car1.is_electric)

# aggiunge nuovo attributo weight
#setattr(car1,'weight',1500)
#print(car1.weight)

# getattr()
# restituisce il valore di un attributo 
# accetta due argomenti 
# - l'oggetto
# - l'attributo di cui vogliamo ottenere il valore
#print(getattr(car1,'brand'))

# encapsulation
# incapsulare significa proteggere 
# un determinato attributo (di classe e di istanza) o metodo 
# rendendolo accessibile solo dall'interno della classe 
# (come il modificatore di visibilità private in java)

# l'incapsulamento si ottiene anteponendo il doppio __
# prima dell'attributo o del metodo

class Car:

    # attributi di classe
    wheels = 4
    # attributi privati accessibili solo dall'interno della classe
    __total_built_car = 0
    __total_driven_km = 0

    def __init__(self, brand, max_speed, year, is_electric):
        # attributi di istanza
        self.brand = brand
        self.year = year
        self.max_speed = max_speed
        self.is_electric = is_electric
        Car.__total_built_car += 1
    
    def drive(self, kilometers):
        print(f'La {self.brand} ha percorso {kilometers} km.')
        Car.__total_driven_km += kilometers

    # sovrascriviamo il metodo __str__()
    def __str__(self):
        return f'Brand: {self.brand}, Year: {self.year}, Max Speed: {self.max_speed}, Electric: {self.is_electric}'

    # definizione metodo per restituire attributi protetti
    def get_total_built_car(self):
        return Car.__total_built_car

    def get_total_driven_km(self):
        return Car.__total_driven_km

car1 = Car('Fiat', 200, 2020, True)
car2 = Car('Ferrari', 300, 2021, False)

car1.drive(20)
car2.drive(30)

print(car1.get_total_built_car())
print(car2.get_total_built_car())

print(car1.get_total_driven_km())
print(car2.get_total_driven_km())

# python ci consente molte libertà
# è comunque possibile (anche se errato)
# creare un nuovo attributo di istanza
# con lo stesso nome dell'attributo di classe protetto
car1.__total_built_car = 0
print(car1.__total_built_car)

print(car1._Car_total_built_car)
print(car1._Car_total_driven_km)
