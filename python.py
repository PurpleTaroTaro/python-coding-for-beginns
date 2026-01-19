name=input('what is your name?')
print(f'hi,{name}.')
print("my name is python")
def greet(name):
    print('hello',name)
    greet('jack')
    friends=['haru chan', 'haniko', 'zato', 'miku',]
    for i, name in enumerate(friends):
        print(f"iteration{i} is {name}")