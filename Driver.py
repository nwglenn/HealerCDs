from Encounter import Encounter
from Classes import Person, Monk, Druid, Paladin, Priest, Shaman
from time import time as myTime

if __name__ == "__main__":
    # tracking which simulation had the highest count of abilities used
    highestCount = 0
    # tracking which simulation had the highest sum of cooldowns used
    highestSum = 0
    # tracking the order the abilities were used in the "best" simulation
    spellOrder = []
    # assigning a floor to the amount of nones I want to allow, or else the simulation will just front load abilities and pay no attention to events where nothing can be cast.
    # I would rather there be no events without a cd being used than get the highest possible, so this value gets slowly incremented with each iteration if it's not possible
    # to cover every event with an ability
    allowedNones = 0
    # tracking whether or not we've found results that meet the criteria
    results = False
    # timing how long the script takes to complete

    # getting the event times from the user
    eventTimes = Encounter.getEventTimes()

    allSpells = []
    numHealers = int(input("How many healers does your raid have? (2-5)\n"))
    for i in range(numHealers):
        # add all of the people and their class/specs to the encounter
        print("--- Next Person ---")
        allSpells.append(Encounter.getClassSpells())
        print("Person Successfully Added\n")

    numSimulations = int(input("Please input the number of simulations that you'd like the script to run.\
 The higher the number of simulations, the more accurate the results. In general, 10,000 simulations\
 is decently accurate and takes ~14 seconds to run. 100,000 simulations is about as accurate as it gets,\
 but takes ~2 minutes to run.\n"))

    startTime = myTime()

    while results == False:

        # since this script is mostly just trying random permutations and seeing which ends with the best results,
        # the higher the number of simulations, the more accurate it will be. I have noticed that ~100,000 simulations 
        # seems to be enough to get an accurate result almost every time. 100,000 simulations takes approximately 
        # 2 minutes. 10,000 simulations takes about 14 seconds, but is quite a bit less accurate.

        for x in range(numSimulations):
            # initialize the encounter
            encounter = Encounter()

            for spellList in allSpells:
                encounter.addSpells(spellList)


            # loop over the event array and actually call the aoe event function
            for time in eventTimes:
                encounter.aoeEvent(time)

            # if the sum is higher than the highest, and it meets our none requirements:
            if encounter.spellSum > highestSum and encounter.totalNones <= allowedNones:
                # record the order of the spells used
                spellOrder = encounter.abilitiesUsed
                # record the number of spells used
                highestCount = encounter.totalSpells
                # record the sum of the cooldowns
                highestSum = encounter.spellSum
                # set the results to true so that we exit the while loop after the simulations are done
                results = True
        # if we didn't find any results, increment the allowed nones
        allowedNones += 1

    endTime = myTime()

    print("\n---------------RESULTS--------------\n")
    # formatting the output to be readable
    for x in range(len(spellOrder)):
        # if only one ability was cast for a specific event
        if len(spellOrder[x]) == 1:
            # if the spell has a shorter cooldown due to talents, make sure to display that cooldown instead of the base one
            if spellOrder[x][0]["talentCooldown"]:
                # Show the output like: [Cooldown] <tab> [Player] used [Ability]
                # the output of this ends up looking like: 180      Ruru used [Tree]
                print("{} \t {} used [{}]".format(spellOrder[x][0]["shortCooldown"], str(spellOrder[x][0]["owner"]).title(), spellOrder[x][0]["name"].title()))
            else:
                print("{} \t {} used [{}]".format(spellOrder[x][0]["cooldown"], str(spellOrder[x][0]["owner"]).title(), spellOrder[x][0]["name"].title()))
        # if two abilities were used for the event, show both cooldowns and abilities on one line.
        elif len(spellOrder[x]) == 2:
                if spellOrder[x][0]["talentCooldown"]:
                    # the output of this ends up looking like: 180 60   Nick used [Aura Mastery], Thunder used [Earthen Wall Totem]
                    print("{} {} \t {} used [{}], {} used [{}]".format(spellOrder[x][0]["shortCooldown"], spellOrder[x][1]["cooldown"], str(spellOrder[x][0]["owner"]).title(), spellOrder[x][0]["name"].title(), str(spellOrder[x][1]["owner"]).title(), spellOrder[x][1]["name"].title()))
                elif spellOrder[x][1]["talentCooldown"]:
                    print("{} {} \t {} used [{}], {} used [{}]".format(spellOrder[x][0]["cooldown"], spellOrder[x][1]["shortCooldown"], str(spellOrder[x][0]["owner"]).title(), spellOrder[x][0]["name"].title(), str(spellOrder[x][1]["owner"]).title(), spellOrder[x][1]["name"].title()))
                else:
                    print("{} {} \t {} used [{}], {} used [{}]".format(spellOrder[x][0]["cooldown"], spellOrder[x][1]["cooldown"], str(spellOrder[x][0]["owner"]).title(), spellOrder[x][0]["name"].title(), str(spellOrder[x][1]["owner"]).title(), spellOrder[x][1]["name"].title()))
        else:
            print("No spells were used on this event.")

    print("\nNumber of cooldowns used: " + str(highestCount))
    print("Sum of their cooldowns: " + str(highestSum))
    print("Total simulation run time: " + str(int(endTime - startTime)) + " seconds.")