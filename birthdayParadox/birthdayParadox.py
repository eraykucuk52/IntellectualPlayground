
"""Birthday Paradox Simulation, by Al Sweigart
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://github.com/eraykucuk52
Tags: short, math, simulation"""

import datetime, random, time, sys


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is uniportant for our simulation, as long as all 
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs mmore than more
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None.
    
    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday. 
            

# Display the intro:
print("""Birthday Paradox, by Al Sweigart
      
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birtdays is surprisingly large.
This program does a Monte Carlo silumation (that is, repeated random 
silumations) to explore this concept.
      
(It's not actually a paradox, it's just a suprising result.)
""")

# Set up a tuple of month names in order:
MONTHS = ("Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec")

while True: # Keeping asking until the user enters a valid amount.
    print("How many birthdays shall I generate? (Max100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount
print()

# Generate and display the birthdays:
print("Here are", numBDays, "birthdays:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    months = MONTHS[birthday.month -1]
    dateText1 = "| {} {}, ".format(months, birthday.day)
    dateText2 = "| {} 0{}, ".format(months, birthday.day)
    if (i+1) % 7==0:
        if birthday.day < 10:
            print(dateText2)
        else:
            print(dateText1)
    else:
        if birthday.day < 10:
            print(dateText2, end="")
        else:
            print(dateText1, end="")
print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print("In this simulation, ", end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print("multiple people have a birthday on", dateText)
else:
    print("there are no matching birthdays.")
print()

# Run through 100,000 simulations:
print("Generating", numBDays, "random birthdays 100,000 times...")
input("Press Enter to begin...")

RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'

print("Let's run another 100,000 simulations.")
simMatch = 0 # How many simulations had matching birthdays in them.
total_simulations = 100_000
report_every = 10_000
for i in range(total_simulations):
    # Report on the progress ecery 10,000 simulations:
    if i % report_every == 0:
        # Calculate how much completed as a percentage
        percent_complete = int((i / total_simulations) * 100)
        # Create the loading bar
        progress_bar = '[' + (GREEN + '=' * (percent_complete // 2) + ENDC) + (' ' * (50 - (percent_complete // 2))) + ']'
        # Print loading bar and percentage (percentage in red)
        sys.stdout.write(f"\r{progress_bar} {RED}{percent_complete}%{ENDC} completed")
        sys.stdout.flush()
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

# Complete the loading bar when the simulation is finished
sys.stdout.write(f"\r{'[' + GREEN + '=' * 50 + ENDC + ']'} 100% completed\n")
sys.stdout.flush()
print("100,000 simulations run.")

# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')