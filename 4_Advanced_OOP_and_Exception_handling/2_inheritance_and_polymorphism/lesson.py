'''
class Payment:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def process(self):
        print(f'Paying {self.amount} {self.currency}')

class CreditCardPayment:

    def __init__(self, amount, currency, card_number):
        self.amount = amount
        self.currency = currency
        self.card_number = card_number
    
    def process(self):
        print(f'Paying {self.amount} {self.currency}')

class PaypalPayment:

    def __init__(self, amount, currency, email):
        self.amount = amount
        self.currency = currency
        self.email = email
    
    def process(self):
        print(f'Paying {self.amount} {self.currency}')

payment = Payment(200.0, 'USD')
payment.process()

cc_payment = CreditCardPayment(100.0, 'EUR', '0000111122223333')
cc_payment.process()

paypal_payment = PaypalPayment(10.0, 'CHF', 'mario.rossi@gmail.com')
paypal_payment.process()
'''

# in questo esempio abbiamo creato 3 differenti classi
# rappresentanti ognuna di esse un metodo di pagamento differente
# infrangendo il principio della programmazione DRY Don't Repeat Yourself
# ciò rende il codice molto più prolisso e inoltre stiamo aggiungendo
# molte complessità dal punto di vista della manutenzione del codice
# e anche per quanto riguarda il testing.
# Inoltre, quando scriviamo codice ripetitivo generalmente c'è una soluzione migliore.

# Ereditarietà
# il principio dell'ereditarietà prevede che ci sia una sorta di gerarchia
# tra le classi:
# ci sono delle classi genitore (chiamate superclassi)
# e delle classi figlie (chiamate sottoclassi).
# Le sottoclassi possono ereditare attributi e metodi dalla classe madre.

'''
# definiamo la classe madre (superclasse)
class Payment:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def process(self):
        print(f'Paying {self.amount} {self.currency}')

# definiamo la classe figlia (sottoclasse)
class CreditCardPayment(Payment):

    def __init__(self, amount, currency, card_number):
        # amount e currency sono attributi di istanza ereditati
        # già definiti nella superclasse
        # possono essere omessi evitando 
        # la ripetizione degli attributi di istanza


        #self.amount = amount
        #self.currency = currency

        # attraverso la funzione super() possiamo accedere alla superclasse
        # e utilizzare il metodo costruttore
        # inizializzando la superclasse passando 
        # gli attributi di istanza ereditati come argomento
        super().__init__(amount, currency)
        # la classe figlia avrà i suoi attributi di istanza
        self.card_number = card_number

# definiamo un altra classe figlia che eredita da Payment
class PaypalPayment(Payment):

    def __init__(self, amount, currency, email):
        super().__init__(amount, currency)
        self.email = email


# notiamo che nelle classe figlie
# non abbiamo definito il metodo process()
# ma è comunque disponibile in quanto ereditato da Payment    
cc_payment = CreditCardPayment(100.0, 'EUR', '0000111122223333')
cc_payment.process()

paypal_payment = PaypalPayment(10.0, 'CHF', 'mario.rossi@gmail.com')
paypal_payment.process()
'''

# nelle classi figlie è possibile definire
# metodi che ovviamente saranno accessibili
# solo da oggetti istanziati partendo da quella classe stessa

'''
class Payment:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def process(self):
        print(f'Paying {self.amount} {self.currency}')


class CreditCardPayment(Payment):

    def __init__(self, amount, currency, card_number):
        super().__init__(amount, currency)
        self.card_number = card_number

class PaypalPayment(Payment):

    def __init__(self, amount, currency, email):
        super().__init__(amount, currency)
        self.email = email
    
    # definizione nuovo metodo per la classe
    # figla PaypalPayment
    def make_paypal_payment(self):
        print('Paypal Payment')


cc_payment = CreditCardPayment(100.0, 'EUR', '0000111122223333')
cc_payment.process()

paypal_payment = PaypalPayment(10.0, 'CHF', 'mario.rossi@gmail.com')
paypal_payment.process()
paypal_payment.make_paypal_payment()
'''

# Override dei metodi
# è possibile nelle subclass ridefinire
# un metodo ereditato da una superclass

'''
class Payment:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def process(self):
        print(f'Paying {self.amount} {self.currency}')


class CreditCardPayment(Payment):

    def __init__(self, amount, currency, card_number):
        super().__init__(amount, currency)
        self.card_number = card_number

    # override metodo process()
    def process(self):
        input('Enter CVV code:')
        print(f'Paying {self.amount} {self.currency}')

class PaypalPayment(Payment):

    def __init__(self, amount, currency, email):
        super().__init__(amount, currency)
        self.email = email
    
    # override metodo process()
    def process(self):
        input('Enter password:')
        #print(f'Paying {self.amount} {self.currency}')
        
        # per evitare ripetizioni di codice
        # possiamo chiamare tramite super()
        # il metodo process definito nella superclass
        super().process()


cc_payment = CreditCardPayment(100.0, 'EUR', '0000111122223333')
cc_payment.process()

paypal_payment = PaypalPayment(10.0, 'CHF', 'mario.rossi@gmail.com')
paypal_payment.process()
'''

# livelli multipli di ereditarietà

# è possibile organizzare le classi del nostro codice
# in più livelli di ereditarietà, ad esempio
# se volessimo definire una classe ancora più specifica
# per quanto riguarda il pagamento tramite paypal
# potremmo creare una nuova classe che eredita dalla classe PaypalPayment,
# che a sua volta eredita dalla classe Payment.

'''
class Payment:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def process(self):
        print(f'Paying {self.amount} {self.currency}')

class PaypalPayment(Payment):

    def __init__(self, amount, currency, email):
        super().__init__(amount, currency)
        self.email = email
    
    def process(self):
        input('Enter password:')
        super().process()

class PremiumPaypalPayment(PaypalPayment):

    def __init__(self, amount, currency, email, discount):
        super().__init__(amount, currency, email)
        # definizione nuovo attributo di istanza
        self.discount = discount
        # assegnazione nuovo valore per attributo di istanza ereditato
        self.amount *= 1 - self.discount / 100
    
premium_paypal_payment = PremiumPaypalPayment(100.0, 'CHF', 'mario.rossi@gmail.com', 10.0)
#premium_paypal_payment.process()

# metodi utili per l'ereditarietà

# issubclass() accetta due argomenti (classi differenti)
# e restituisce un booleano: 
# - True nel caso in cui il primo argomento è una subclass del secondo argomento
# - False nel caso in cui il primo argomento non è una subclass del secondo argomento
print(issubclass(PaypalPayment, PaypalPayment))

# isinstance() accetta due argomenti, un oggetto e una classe
# restituisce un booleano:
# - True nel caso in cui l'oggetto è un istanza della classe passata come argomento
# - False nel caso in cui l'oggetto non è un istanza della classe passata come argomento
print(isinstance(premium_paypal_payment, PremiumPaypalPayment))

# is è un operatore binario, restituisce un booleano
# - True se due elementi rappresentano lo stesso oggetto
# - False se due elementi non rappresentano lo stesso oggetto

premium_paypal_payment1 = PremiumPaypalPayment(100.0, 'CHF', 'mario.rossi@gmail.com', 10.0)
premium_paypal_payment2 = PremiumPaypalPayment(100.0, 'CHF', 'mario.rossi@gmail.com', 10.0)
premium_paypal_payment3 = premium_paypal_payment1

print(premium_paypal_payment1 is premium_paypal_payment2)

print(premium_paypal_payment1 is premium_paypal_payment3)
'''

# Polimorfismo

# In Python, il concetto di polimorfismo applicato alla programmazione ad oggetti, 
# consente a metodi e attributi di assumere forme differenti in base 
# all’oggetto in cui vengono eseguiti.
'''
class Payment:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def engage_payment(self):
        print('Abilitating payiment...')
        self.process()
    
    def process(self):
        print(f'Paying {self.amount} {self.currency}')

class PaypalPayment(Payment):

    def __init__(self, amount, currency, email):
        super().__init__(amount, currency)
        self.email = email
    
    # override del metodo process()
    # ereditato dalla superclass
    def process(self):
       print(f'Paying with Paypal: {self.amount} {self.currency}')

payment = Payment(20.0, 'USD')
paypal_payment = PaypalPayment(10.0, 'CHF', 'mario.rossi@gmail.com')

payment.engage_payment()
paypal_payment.engage_payment()
'''

# Composition

# il concetto di composition può essere un 
# alternativa all'utilizzo dell'ereditarietà.

# Definizione della classe base
class Payment:
    # Il costruttore accetta un oggetto di una classe specifica
    def __init__(self, payment_service):
        self.payment_service = payment_service
    
    # Metodo generico che delega l'implementazione alla classe specifica
    def process(self):
        self.payment_service.make_payment()

# Definizione della classe specifica per il pagamento con carta di credito
class CreditCardPayment:
    def make_payment(self):
        print('Paying via credit card...')

# Definizione della classe specifica per il pagamento con PayPal
class PaypalPayment:
    def make_payment(self):
        print('Paying via PayPal...')

# Creazione di oggetti utilizzando la composition
credit_card_payment = Payment(CreditCardPayment())
paypal_payment = Payment(PaypalPayment())

# Esecuzione del metodo process che delega alle classi specifiche
credit_card_payment.process()  # Output: Paying via credit card...
paypal_payment.process()       # Output: Paying via PayPal...