def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print_lyrics()


def print_twice(word):
    print(word)
    print(word)

print_twice('Python')


def thing():
    print('Hello')
    print('Fun')
thing()
print('Zip')
thing()

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')  # Hello
greet('es')  # Hola
greet('fr')  # Bonjour


def addtwo(a, b):
    return a + b
x = addtwo(3, 5)
print(x)

def say_hello():
    print("Hello!")
say_hello()

def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    return pay
print(computepay(45, 10))

def greet(name):
    return "Hello " + name + "!"    
print(greet("Ross Taylor"))