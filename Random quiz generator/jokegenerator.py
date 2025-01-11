import random

def random_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? It had too many problems.",
        "What do you call fake spaghetti? An impasta!",
        "Why was the computer cold? It left its Windows open!"
    ]
    print("Here’s a joke for you:")
    print(random.choice(jokes))

random_joke()
