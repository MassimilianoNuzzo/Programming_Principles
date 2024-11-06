# if-else statement

#In Python, ma anche in altri linguaggi di programmazione, 
# le linee di codice vengono eseguite dall’interprete una per una 
# in modo sequenziale in base all’ordine in cui sono state scritte, 
# dall’alto verso il basso.

#user_name = input('Come ti chiami? ')
#print(f'Benvenuto {user_name}!')

# l'istruzione if permette
# di eseguire codice in modo condizionale
# SE la condizione è rispettata:
    # eseguo queste istruzioni
# il programma continua la sua esecuzione..

#psw = input('Inserisci la password: ')
#correct_psw = 'B4rtS1mps0n'
#if psw == correct_psw:
#    print('Accesso consentito')
#print('Il programma continua...')

# istruzione else
# SE la condizione è rispettata:
    # eseguo queste istruzion
# ALTRIMENTI:
    #  eseguo queste altre istruzioni

#psw = input('Inserisci la password: ')
#correct_psw = 'B4rtS1mps0n'
#if psw == correct_psw:
#    print('Accesso consentito')
#else:
#    print('Password errata')
#print('Il programma continua..')

# istruzione elif
# Molto spesso per risolvere problemi più complessi 
# abbiamo bisogno di definire diverse condizioni, 
# per questo motivo si utilizza l’istruzione elif:

#temperature = 80
#if temperature > 70:
#    print('INCENDIO! Attiva gli estintori!')
#elif temperature > 30:
#    print('Accendi il sistema di raffreddamento')
#elif temperature < 10:
#    print('Accendi il sistema di riscaldamento')
#else:
#    print('Temperatura ideale')

# operatore ternario

#is_user_logged_in = False
#user_status = 'Active' if is_user_logged_in else 'Inactive'
#print(user_status)

# Truthy and Falsy values 

#name = input('Inserisci il tuo nome: ')
#if name:
#    print(f'Benvenuto {name}')
#else:
#    print('Nome non inserito')

# falsy value
'''
False
0 0.
None
""
'''

# cicli - loop

# while

#correct_psw = 'B4rtS1mps0n'
#psw = None
#while psw != correct_psw:
#    psw = input('Inserisci la password: ')
#    if psw == correct_psw:
#        print('Accesso consentito')
#    else:
#        print('Password errata')
#print('Il programma continua...')

# break e continue
# sono istruzioni che modificano
# il flusso naturale dei cicli

# break
#numero = 0
#while numero < 10:
#    numero += 1
#    print(numero)
#    if numero == 5:
#        print('Numero trovato:', numero)
#        print('Esco dal ciclo while..')
#        break  # Esce dal ciclo appena trova il numero 5
#else:
    # viene eseguita soltanto se il ciclo termina naturalmente
    # e non tramite istruzione break
#    print('Il ciclo è terminato..') 

# continue
#numero = 0
#while numero < 10:
#    numero += 1
#    if numero == 5:
#        print('Il numero 5 non viene stampato, passa all\'istruzione successiva.')
#        continue  # salta l'esecuzione passando all'istruzione successiva
#    else:
#        print(numero)
#else:
    # viene eseguita comunque
    # perchè continue non interrompe il ciclo
#    print('Il ciclo è terminato..')

# for

#tasks = ['fare la spesa','cucinare i ceci','lavare il cane']
#for task in tasks:
#    print(task)

# enumerate()

#tasks = ['fare la spesa','cucinare i ceci','lavare il cane']
#for id,task in enumerate(tasks):
#    print(id, task)

#tasks = ['fare la spesa','cucinare i ceci','lavare il cane']
#for id,task in enumerate(tasks, start=1):
#    print(id, task)

# range()

#for i in range(10):
#    print(i)

#for i in range(2, 10):
#    print(i)

#for i in range(2, 10, 2):
#    print(i)

#for second in range(10, 0, -1):
#    print(f'Mancano {second} secondi')
#else:
#    print('Capodanno!')

#for second in range(10, 0, -1):
#    print(f'Mancano {second} secondi')
#    if second == 7:
#        break
#else:
#    print('Capodanno!')

# break e continue nel ciclo for

for i in range(10,0,-1):
    
    if i == 2:
        print('interrompe il ciclo')
        break
    
    if i == 7:
        print('l\'istruzione viene saltata')
        continue

    print(i)

else:
    print('Il ciclo è terminato')