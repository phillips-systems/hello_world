from art import *

def say_hello():
    word_0 = text2art("HELLO", font="rnd-large")
    word_1 = text2art("WORLD", font="rnd-large")
    message = [word_0, word_1]
    for word in message:
        print(word)

say_hello()
