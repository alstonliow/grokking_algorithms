def greet(name):
    print(f"Hello, {name}!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print(f"how are you, {name}?")

def bye():
    print("ok bye!")

greet("Alice")