import secrets

def flip():
    return secrets.choice(["heads", "tails"])



print("lets play a game guess hears or tails")

guess= input("whats your guess (heads/tails):").strip().lower()

result=flip()

print("yo good job yout right!! play again?" if guess== result else "aahh sorry not this time. try again?")
