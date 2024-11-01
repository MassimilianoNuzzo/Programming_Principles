'''
Salva un numero a piacere su una variabile
chiedi all'utente di indovinarlo.
Il numero deve essere da 0 a 9.
Controlla se l'utente lo indovina,
lo sbaglia,
o inserisce un numero fuori range,
e stampa a schermo un messaggio opportuno.
'''
#correct_number = 5
#input_number = int(input('Indovina il numero, inserendo un valore da 0 a 9: '))
#if input_number < 0 or input_number > 9:
#    print('Hai inserito un valore fuori range. Valori consentiti da 0 a 9!')
#elif input_number == correct_number:
#    print('Hai indovinato il numero')
#else:
#    print('Numero sbagliato')

'''
Modifica l'esercizio precedente
continua a chiedere il numero all'utente
FINCHE' non indovina il numero
'''
#correct_number = 5
#input_number = None
#while input_number != correct_number:
#    input_number = int(input('Indovina il numero, inserendo un valore da 0 a 9: '))
#    if input_number < 0 or input_number > 9:
#        print('Hai inserito un valore fuori range. Valori consentiti da 0 a 9!')
#    elif input_number == correct_number:
#        print('Hai indovinato il numero')
#    else:
#        print('Ritenta!')

'''
Modifica il programma precedente per
implementare il numero di tentativi.
Stavolta è vietato utilizzare il ciclo while!
Ad ogni iterazione,
stampa il numero del tentativo corrente,
ad esempio “Tentativo n. 1”
poi, come sempre, richiedi l'inserimento del numero,
e valuta se è corretto.
Se l'utente non indovina entro 5 tentativi,
il gioco termina, stampando un messaggio opportuno.
'''
secret_number = 5
input_number = None
for attempt in range(1,6):
    print(f'Tentativo numero {attempt}')
    input_number = int(input('Indovina il numero, inserendo un valore da 0 a 9: '))
    if input_number < 0 or input_number > 9:
        print('Hai inserito un valore fuori range. Valori consentiti da 0 a 9!')
    elif input_number == secret_number:
        print('Hai indovinato il numero')
        break
    else:
        print('Ritenta!')
else:
   print('Troppi tentativi!')
print('Gioco terminato.')
