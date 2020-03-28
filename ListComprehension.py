people = ["leSlEy", "KEN", "sYDNey", "AnNa", "gRANT"]



def printInvite(name):
    print(f"I would like to invite: {name}")


#correct_names = [p.capitalize() for p in people]

print(correct_names)

[printInvite(person.capitalize()) for person in people]