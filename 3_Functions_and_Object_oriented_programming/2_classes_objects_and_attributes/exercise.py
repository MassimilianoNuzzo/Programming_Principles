'''
Definisci una classe che rappresenta un libro.
La classe ha gli attributi di istanza
titolo,autore,anno pubblicazione e prezzo.
La classe ha anche un metodo stampa,
con un messaggio a piacere, tutti i propri attributi.
Una volta completata la classe,
istanziane due oggetti, passando un argomento
per ciascun attributo di istanza.
Chiama su ciascuno dei due oggetti il metodo stampa
e verifica che il messaggio stampato sia corretto.
'''
'''
class Book:

    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
    
    def show_details(self):
        print(f'Il libro {self.title} di {self.author}, pubblicato nel {self.year} ha un prezzo di {self.price} €.')
        
book_1 = Book('La Divina Commedia','Dante Alighieri', 1321, 29.99)
book_2 = Book('Il Fù Mattia Pascal','Luigi Pirandello',1904, 19.99)

book_1.show_details()
book_2.show_details()
'''

'''
Alla classe dell'esercizio precedente
aggiungi un nuovo metodo,
che servirà per applicare uno sconto al libro.
Il metodo perciò, prevede un parametro
che rappresenta la percentuale da scontare
e, in base ad essa riduce il prezzo originario
(rappresentato dall'attributo di istanza).
Una volta chiamato il metodo su un oggetto,
controlla se il prezzo è stato aggiornato correttamente.
Per controprova, controlla anche il prezzo,
sull'altro oggetto sia rimasto invariato.
'''

class Book:

    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
    
    def show_details(self):
        print(f'Il libro {self.title} di {self.author}, pubblicato nel {self.year} ha un prezzo di {self.price} €.')

    def applay_discount(self, discount_percentage):
        self.price = self.price * (100 - discount_percentage)/100

book_1 = Book('La Divina Commedia','Dante Alighieri', 1321, 15.9)
book_2 = Book('Il Fù Mattia Pascal','Luigi Pirandello',1904, 19.99)

book_1.applay_discount(30)

book_1.show_details()
book_2.show_details()


'''
Crea una classe Pokemon coi seguenti attributi:
Nome, Salute e Forza.
Implementa un metodo di attacco che permetta
a un Pokemon di attaccarne un altro,
riducendo la Salute dell'avversario.
(al metodo passeremo come argomento un oggetto Pokemon)
La Salute dell'avversario viene ridotta
di un valore pari alla Forza dell'attaccante.
Il metodo infine stampa un messaggio,
con alcuni dettagli sull'attacco, ad esempio:
Pikachu attacca Charizard causando 15 danni!

Completata la classe, istanzia due Pokemon
e falli attaccare l'un l'altro, quante volte desideri.
Dopo il combattimento, stampa la Salute
di entrambi, per vedere se è coerente con gli attacchi.
'''

'''
class Pokemon:

    def __init__(self, name, health, force, level, winner):
        self.name = name
        self.health = health
        self.force = force
        self.level = level
        self.winner = winner
    
    def attack(self, enemy_pokemon):
        enemy_pokemon.health -= self.force
        print(f'{self.name} attacca {enemy_pokemon.name} causando {self.force} danni!')
        print()
        
pokemon_1 = Pokemon('Pikachu', 100, 10, 45, False)
pokemon_2 = Pokemon('Charizard',100,25, 100,False)

print('Statistiche:')

print()

print(f'Nome: {pokemon_1.name}')
print(f'Salute: {pokemon_1.health}')
print(f'Forza: {pokemon_1.force}')
print(f'Livello: {pokemon_1.level}')

print()

print(f'Nome: {pokemon_2.name}')
print(f'Salute: {pokemon_2.health}')
print(f'Forza: {pokemon_2.force}')
print(f'Livello: {pokemon_2.level}')

print()

while pokemon_1.health > 0 and pokemon_2.health > 0:
        pokemon_1.attack(pokemon_2)
        pokemon_2.attack(pokemon_1)
        if pokemon_1.health == 0:
            pokemon_2.winner = True
        elif pokemon_2.health == 0:
             pokemon_1.winner = True

winner_pokemon = pokemon_1 if pokemon_1.winner else pokemon_2

print(f'Salute {pokemon_1.name}: {pokemon_1.health}')
print(f'Salute {pokemon_2.name}: {pokemon_2.health}')

print()

print(f'Il pokemon vincitore è {winner_pokemon.name}!')
'''

