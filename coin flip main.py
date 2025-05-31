import random

def flip():
    result= random.randint(0,1)
    if result ==0:
        result == "heads"
    else:
        result == "tails"
        
print("lets play a game Heads or tails?")
flip_result= flip 
guess_heads= input("head")
guess_tails= input("tailes")

if guess_heads == flip_result:
    print("congrats thats right")
else:
    print("sorry try again")

if guess_tails == flip_result:
       print("congrats thats right")
else:
    print("sorry try again")