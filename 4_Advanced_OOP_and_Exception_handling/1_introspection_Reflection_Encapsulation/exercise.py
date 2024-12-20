'''
Definisci una classe che rappresenti
uno strumento musicale,
ad esempio una chitarra, un piano etc..
Assegna alla classe almeno due attributi d'istanza
e almeno due attributi di classe, a piacere.

Istanzia un oggetto della classe e applica
il principio dell'introspection:
con le funzioni hasattr e dir,
verifica quali attributi sono accesibili 
sull'oggetto e quali sulla classe. 
'''

'''
class Guitar:

    strings_number = 6
    instrument_type = 'String'
    total_built_guitar = 0

    def __init__(self, model, is_electric):
        self.model = model
        self.is_electric = is_electric
        Guitar.total_built_guitar +=1
    
guitar1 = Guitar('Stratocaster',True)

print(hasattr(guitar1,'strings_number'))
print(hasattr(guitar1,'instrument_type'))
print(hasattr(guitar1,'total_built_guitar'))
print(hasattr(guitar1,'model'))
print(hasattr(guitar1,'is_electric'))

print(hasattr(Guitar,'model'))
print(hasattr(Guitar,'is_electric'))

print(dir(guitar1))
print(dir(Guitar))
'''

'''
Alla classe dell'esercizio precedente,
aggiungi il metodo speciale __str__ affinchè,
quando l'oggetto viene stampato 
appaia un messaggio descrittivo a piacere.
'''
'''
class Guitar:

    strings_number = 6
    instrument_type = 'String'
    total_built_guitar = 0

    def __init__(self, model, is_electric):
        self.model = model
        self.is_electric = is_electric
        Guitar.total_built_guitar +=1

    def __str__(self):
        return f'Model: {self.model} Electric: {self.is_electric}'
    
guitar1 = Guitar('Stratocaster',True)

print(guitar1)
'''

'''
Alla classe dell'esercizio precedente,
aggiungi un attributo di istanza PRIVATO.
Verifica, sull'oggetto istanziato, che tale attributo
NON sia accessibile.
Una volta effettuata questa verifica,
aggiungi alla definizione della classe,
un metodo che permetta di restituire il valore
dell'attributo privato.

BONUS:
Aggiungi alla classe un altro metodo,
che permette di MODIFICARE l'attributo privato.
(il metodo prende un parametro in ingresso
e lo usa per valorizzare l'attributo privato)
'''

class Guitar:

    __strings_number = 6
    __instrument_type = 'String'
    __total_built_guitar = 0
    __total_played_guitar = 0

    def __init__(self, model, is_electric):
        self.model = model
        self.__is_electric = is_electric
        Guitar.__total_built_guitar +=1
    
    # se non passo self come argomento
    # potrò chiamare i metodi solo utilizzando la classe
    # e non l'istanza
    def get_strings_number():
        return Guitar.__strings_number
    
    def get_instrument_type():
        return Guitar.__instrument_type

    def get_total_built_guitar():
        return Guitar.__total_built_guitar
    
    def get_total_played_guitar(self):
        return Guitar.__total_played_guitar
    
    def get_is_electric(self):
        return self.__is_electric
    
    def set_total_played_guitar(self, played_guitar):
        Guitar.__total_played_guitar += played_guitar

    def set_is_electric(self, is_electric):
        self.__is_electric = is_electric
    
    def __str__(self):
        return f'Model: {self.model} Electric: {self.__is_electric}'
    
guitar1 = Guitar('Stratocaster',True)

print(guitar1)

#print(Guitar.get_instrument_type())
#print(Guitar.get_instrument_type())
#print(Guitar.get_total_built_guitar())

#print(guitar1.__total_played_guitar)

print(guitar1.get_total_played_guitar())

guitar1.set_total_played_guitar(10)

print(guitar1.get_total_played_guitar())

print(guitar1.get_is_electric())

guitar1.set_is_electric(False)

print(guitar1)

