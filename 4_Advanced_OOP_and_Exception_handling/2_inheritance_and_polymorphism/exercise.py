'''
Crea una classe che rappresenta una persona,
e possiede gli attributi di istanza nome e età.
Ora crea una classe che rappresenta un regista,
che eredita dalla classe persona,
e possiede un attributo di istanza in più
che indica un film famoso che ha girato.

Istanzia un oggetto della superclasse,
e poi un oggetto della sottoclasse,
e verifica quali attributi sono accessibili
su di essi.
'''

'''
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class MovieDirector(Person):

    def __init__(self, name, age, famous_movie):
        super().__init__(name, age)
        self.famous_movie = famous_movie
    
persona1 = Person('Mario Rossi', 30)
regista1 = MovieDirector('Martin Scorsese', 79, 'The wolf of wall street')
'''

'''
Alle classi dell'esercizio precedente,
aggiungi un metodo.
La classe persona dovrà avere un metodo per presentarsi,
stampando a schermo i valori dei propri attributi.

La sottoclasse dovrà fare un override di tale metodo,
per stampare a schermo un messaggio diverso,
che contenga il valore del suo attributo specifico (film famoso).
'''

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return (f'Ciao sono {self.name} e ho {self.age} anni.')
    
class MovieDirector(Person):

    def __init__(self, name, age, famous_movie):
        super().__init__(name, age)
        self.famous_movie = famous_movie
    
    def introduce(self):
        return super().introduce() + (f'\nIl mio film più famoso è: {self.famous_movie}.')

persona1 = Person('Mario Rossi', 30)
regista1 = MovieDirector('Martin Scorsese', 79, 'The wolf of wall street')

print(persona1.introduce())
print(regista1.introduce())

# attributi accessibili superclasse
persona1.name
persona1.age

# attributi accessibili subclasse
regista1.name
regista1.age
regista1.famous_movie