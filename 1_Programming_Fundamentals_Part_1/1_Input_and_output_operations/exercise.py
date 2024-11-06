# stampa sul terminale uno sotto l'altro
# i nomi dei tre personaggi principali
# di tre uomini e una gamba usando solo argomenti posizionali
print('Aldo')
print('Giovanni')
print('Giacomo')

# aggiungi alle print precedenti uno o più argomenti 
# keyword affinchè la stampa diventi come segue:
# 'Aldo,Giovanni,Gicomo'

print('Aldo', end=',')
print('Giovanni', end=',')
print('Giacomo', end='.')

# stampa il seguente testo usando una sola funzione print
# Jacqueine>Marge>Lisa
# gli argomenti posizionali non devono contenere il carattere >
print('\nJacqueline', 'Marge', 'Lisa', sep='>')

# stampa il seguente testo usando un solo argomento posizionale
# Abrham>Homer>Bart
# gli argomenti posizionali non devono contenere il carattere >
# puoi usare più di una print se necessario
print('Abrham', end='>')
print('Homer', end='>')
print('Bart', end='>')

# genera 3 errori di sintassi e 3 errori di run-time

# errori sintassi
# !
# ()print
# saluta
# print('ciao', end=)

# errori run-time
# saluta('Mario')
# input('Ciao', 'Ciao')
# input('Ciao', end='#')

# chiedere all'utente di inserire il proprio nome
# fa si che possa inserirlo nel terminale
# salvarlo in una variabile
# e stampalo nel terminale con un testo simile Nome utente = Max
# approccio procedurale
name=input('\nCome ti chiami?\n')
print('Nome utente =',name)


# paradigma funzionale evita di creare variabili e cambiarne lo stato
# il codice è piu robusto performante e facile da manuntenere 
# non sto utilizzando risorse creando variabili e assegnando valori
# print('Nome utente =',input('\nCome ti chiami?'))





