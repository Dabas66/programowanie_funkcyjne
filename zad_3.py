human_avg_temperture=36.6

def fever():
    your_temperature=float(input("What is your current temperture? "))
    if (your_temperature>human_avg_temperture):
        print("You might have a fever")
    else:
        print("You do not have a fever")
fever()