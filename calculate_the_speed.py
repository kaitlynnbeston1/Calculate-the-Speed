import sys


"""
Kaitlynn Allacea Beston
Calculate the Speed
CS30
"""

class DistanceTime:
    """
    Class to hold values for distance and time.
    """
    def __init__(self, distance, time):
        """
        Initializes the object.
        """
        self.distance = distance
        self.time = time
    def calc_speed(self):
        speed = self.distance / self.time
        hr = "undefined"
        if self.time == 1:
            hr = "hour"
        else:
            hr = "hours"
        print(f"Your speed would be {speed} if you went {self.distance} miles in {self.time} {hr}.")
        

print("Welcome to KB Speed Calculator!")
print("You give it a speed in miles and time in hours, it'll give you your speed!")
print("Let's get started.")
d = "undefined"
t = "undefined"
while True:
    typing = True
    while typing:
        d = input("Enter a distance, in miles.")
        if d.lower() == "quit":
                sys.exit()

        try:
            d = float(d)
        except:
            print("Please enter a number.")
            continue
        else:
            if d < 0:
                print("You can't go a negative speed.")
                continue
            else:
                typing = False
    typing = True
    while typing:
        t = input("Enter a time, in hours: ")
        if t.lower() == "quit":
                sys.exit()
        try:
            t = float(t)
        except:
            print("Please enter a number.")
            continue
        else:
            if t < 0:
                print("Oh, so you're a time traveller? \n I highly doubt that. Please try again.")
                continue
            else:
                typing = False
    calc = DistanceTime(d, t)
    calc.calc_speed()
    again = input("Would you like to calculate another speed? \n Enter y or n: ")
    if again == "y":
        print("Ok...")
        continue
    else:
        print("Ok, thank you for using KB Speed Calculator!")
        break

    