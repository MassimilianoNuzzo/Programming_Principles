# operatori aritmetici

# addizione  
print(33 + 1)
# sottrazione
print(33 - 1)
# moltiplicazione
print(33 * 1)
# divisione
print(33 / 2)

a = 10
b = 5
c = a / b

print(c)

# modulo - restituisce il resto della divisione
d = 13 % 2
print(d)

# esponenziale - elevazione di potenza
print(2**3)

# floor division - divide un numero apporossimando il risultato all'intero più vicino per difetto
print(13 // 3)

# gli operatori + e - possono essere utilizzati
# sia come operatori binari
print(2 - 1)
# che come operatori unari
e = 6
print(- e)

# anche il + può essere utilizzato
# come operatore unario
# ma quello che fa 
# è mantenere il segno originale
f = - 12
print(+ f)

# dobbiamo sempre considerare
# il data-type, soprattutto
# in python che non è un linguaggio tipizzato
# le variabili possono variare in valore 
# ma anche in tipo
test = 1
test = 'ciao'

print(type(2 + 3)) # restituirà int in quanto entrambi valori sono di tipo int
print(type(2 + 3.)) # restituirà float in quanto uno dei due valori (3.) è di tipo float

# gli operatori + - * funzionano cosi:
# - se entrambi i numeri sono intero -> restituisce int
# - se uno dei due numeri è float -> restituisce float
print(type(2 * 3.))

# l'unico operatore che fa eccezione è /
# restituisce sempre float 
# anche se i due numeri sono entrambi int
print(type(10 / 3))
# anche se effettuo una divisione che non produce
# parte frazionaria
print(type(4 / 2))

# sempre attenti al data-type
# non è possibile effettuare operazioni tra string e int/float
#print('10'+2) # -> ERRORE!

# operatori di assegnazione - shortcut

# +=
# -=
# *=
# /=
# %=
# //=

a = 1
#a = a + 1
# equivale ad
a += 1
print(a)

# espressioni
# quali operatori hanno più priorità?

# si seguono le stesse regole applicate alle espressioni aritmetiche

print(10 - 4 * 2) 
# -> risultato = 2 viene eseguita prima la * e poi -
# quindi equivale a (10 - (4*2))
# la moltiplicazione ha maggior priorità

print((10 - 4) * 2) 
# risultato = 12 -> le parentesi assegnano maggior 
# priorità alla porzione di espressione che racchiudono

# raramente si scrivono espressioni matematiche tanto complesse 
# cioè che richiedono l'utilizzo di parentesi {} o []
# generalmente espressioni cosi complesse sono suddivise 
# in espressioni più piccole in modo
# da ridurne la complessità

# l'operatore esponenziale è quello con maggiore priorità
# in python come nella matematica
# esiste la regola Right Binding: 
# nel caso in cui ci siano più esponenziali nella stessa espressione
# acquisisce maggior priorità quello più a destra
print(2**1**3) # risultato = 2 -> viene prima eseguito 1**3 = 1 e poi 2**1

print((2**1)**3) # risultato = 8

print(6 / 3 * 2) # risultato = 4.0 -> data-type float
# gli operatori / e * hanno stessa priorità
# ma quando sono presenti nella stessa espressione
# si utilizza la regola Left Binding
# l'operatore di sinistra acquisisce maggior priorità
# viene eseguita prima la divisione e poi la moltiplicazione

# priorità degli operatori nelle espressioni
'''
1. ()
2. **
3. + - (as unary)
4. * / // %
5. + - (as binary)
'''

# operatori e stringhe

# concatenation - concatenazione
print('ciao ' + 'mondo')

# replication - replica: ripete una concatenazione per il numero di volte indicato dopo *
print('ciao' * 3)

# funzioni di conversione
# utilizzate per convertire una variabile in un altro data-type

age = '33'

# ricorda: la funzione input() restituisce solo string
#print(age + 1) -> genera errore

# int() -> converte se possibile una stringa in int 
age = int('33') 
print(age + 1)

# float()
age = float('33')
print(type(age))

# str()

age = 33
# print('La mia età è ' + age) -> genera errore: non possiamo concatenare string e int
print('La mia età è ' + str(age))

age = str(33)
print(type(age))

# bool()
# la funzione bool() non controlla il contenuto della stringa
# quindi non effettua la conversione da string 'True' o 'False' in boolean
# infatti se eseguo
print(bool('False')) # -> otterrò sempre true
print(bool('True'))

# ma controlla se la string è valorizzata e non sia  stringa vuota - ''
print(bool('')) # restituisce False
print(bool('Ciao')) # restituisce True

# quindi controlla se abbiamo una stringa vuota o una qualsiasi collezione vuota
# restituirà False - controlla se la variabile che stiamo testando è valorizzata

# per i numeri int invece 
# per il valore 0 restituirà False
# qualsiasi altro valore restituirà True
print(bool(0))
print(bool(22))

# None
# si utilizza quando non conosciamo ancora il valore
# di una variabile, perchè magari di qualche calcolo
# non ancora effettuato o perchè restituito da un API
a = None

# anche in questo caso la funzione bool() -> restituirà False
print(bool(a))


# operatori di comparazione
# eseguono una comparazione tra due valori e restituisce un valore booleano

# comparazione tra int

# == -> comparatore di uguaglianza
print(1 == 2) # risultato -> False

# != -> comparatore di disuguaglianza
print(1 != 2) # risultato -> True

# > - maggiore di
print(1 > 2) # risutlato -> False

# < - minore di 
print(1 < 2) # risultato -> True

# >= - maggiore uguale di
print(1 >= 2) # risultato -> False: 1 non è maggiore uguale a 2

age = 18
print('Sei maggiorenne?')
print(age >= 18)

# <= - minore uguale di
print(1 <= 2) # risultato -> True 

# comparazione tra string

# comparatore di uguaglianza
user = 'Mario'
print(user == 'Giuseppe')

# comparatore di disuguaglianza
print(user != 'Giuseppe')

# le comparazioni > o < tra stringhe
# restituiscono un risultato basato sull'Unicode delle stringhe stesse
# e in ogni caso non ha senso effettuare questo tipo di comparazione
# potrebbe aver senso effettuare la comparazione tra il numero di caratteri di due stringhe
# ma sarebbe una comparazione tra int che quindi può essere eseguita

# operatori logici
# prendono in ingresso valori booleani e restituiscono valori booleani

# and -> restituisce True se entrambi i valori sono True
# se uno dei due valori e False restituisce False

# or -> restituisce True se almeno uno dei due valori è True

# not -> esegue l'inverso del valore ricevuto 
# definito unario in quanto opera su un unico valore

# è buona pratica nominare le variabili booleane sotto forma di domanda

is_admin = False
is_moderator = True
is_banned = True

# anche in questo caso esiste una gerarchia delle priorità
# l'operatore logico and ha maggiore priorità
# con l'utilizzo delle parentesi modifichiamo questa gerarchia
# quindi viene prima risolto il contenuto delle parentesi
# e il risultato verrà comparato con la restante espressione:
# l'accesso è consentito se l'utente è admin o moderatore e non è stato bannato
is_access_allowed = (is_admin or is_moderator) and not is_banned
print(is_access_allowed)

# è possibile utilzzare operatori aritmetici, logici e di comparazione insieme
product_price = 150
is_available = True

can_buy = (product_price < (120 + 80)) and is_available
print(can_buy)

# priorità
'''
1. operatori aritmetici
2. operatori di comparazione
3. not
4. and
5. or
'''

# operatori bitwise
# sono operatori che operano non sul valore per intero
# ma operano bit per bit infatti è utilizzato con i numeri binari

# ad esempio i microcontrollori hanno dei registri di configurazione
# orgranizzati in byte - 1 byte = 8 bit

# in python è possibile effettuare 
# operazioni tra numeri binari
# con gli operatori bitwise
# raramente utilizzeremo questo tipo di operatori
# solo in caso di istruzioni di basso livello (più vicine a linguaggio macchina)

# operatore di congiunzione &
# gli operatori bitwise ragionano bit per bit
# questo tipo di operatore restituisce 1 quando
# entrambi i bit sono 1, altrimenti 0

register_1 = 0b01010110
register_2 = 0b11011011

register_3 = register_1 & register_2

print(bin(register_3))
#print(f'{register_3:b}')

# operatore di disgiunzione |
# corrispettivo dell'operatore logico or
# ma ragiona bit per bit
# restituisce 1 quando almeno uno dei due
# bit confrontati è 1

register_4 = register_1 | register_2
print(bin(register_4))

# operatore di disgiunzione esclusiva ^
# funziona come l'operatore di disgiunzione 
# ma restituisce 0 anche se entrambi i bit
# confrontati sono uguali a 1

register_5 = register_1 ^ register_2
print(bin(register_5))

# tilde (alt + 5 su mac se no alt + 126 su windows)
# è un operatore unario bitwise
# inverte bit per bit 
register_6 = ~ register_1
print(bin(register_6))

# operatore di shifting >>
# operatore unario 
# permette di shiftare i bit verso destra
# per l'intero indicato dopo l'operatore
register_7 = register_1 >> 1
print(bin(register_7))

# operatore di shifting <<
register_8 = register_1 << 1
print(bin(register_1))

