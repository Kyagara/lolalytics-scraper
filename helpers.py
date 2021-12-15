regions = [
    "0 - Global",
    "1 - KR",
    "2 - BR",
    "3 - EUNE",
    "4 - EUW",
    "5 - JP",
    "6 - NA",
    "7 - OCE",
    "8 - LAN",
    "9 - LAS",
    "10 - TR",
    "11 - RU",
]

lanes = [
    "0 - Main",
    "1 - Top",
    "2 - Jungle",
    "3 - Middle",
    "4 - Bottom",
    "5 - Support",
]

tiers = [
    "0 - All Ranks",
    "1 - Master+",
    "2 - Diamond+",
    "3 - Diamond 2+",
    "4 - Platinum+",
    "5 - Gold+",
    "6 - Challenger",
    "7 - G. Master",
    "8 - Master",
    "9 - Diamond",
    "10 - Platinum",
    "11 - Gold",
    "12 - Silver",
    "13 - Bronze",
    "14 - Iron",
    "15 - Unranked",
    "16 - 1 Trick",
]

tiersDict = {
    "All Ranks": "all",
    "Master+": "master_plus",
    "Diamond+": "diamond_plus",
    "Diamond 2+": "d2_plus",
    "Platinum+": None,
    "Gold+": "gold_plus",
    "Challenger": "challenger",
    "G. Master": "grandmaster",
    "Master": "master",
    "Diamond": "diamond",
    "Platinum": "platinum",
    "Gold": "gold",
    "Silver": "silver",
    "Bronze": "bronze",
    "Iron": "iron",
    "Unranked": "unranked",
    "1 Trick": "1trick",
}


def printChoices(list):
    for a, b, c in zip(list[::3], list[1::3], list[2::3]):
        print("{:<20}{:<20}{:<}".format(a, b, c))


def getUserInput(minValue, maxValue):
    userInput = input(">> ")
    validAnswer = validateAnswer(userInput, minValue, maxValue)

    while not validAnswer or not userInput:
        userInput = input("Por favor insira um valor válido.\n>> ")
        validAnswer = validateAnswer(userInput, minValue, maxValue)

    return int(userInput)


def validateAnswer(value, minValue, maxValue):
    if value.lower() == "q":
        quit()

    if not value.isdigit():
        return False

    answer = int(value)

    if answer >= minValue and not answer >= maxValue:
        return True


def getTier(value):
    tierKey = value.split(" - ")[1]
    tier = tiersDict[tierKey]

    if tier == None:
        return ["", "platinum_plus"]

    return ["&tier=" + tier, tier]


def getRegion(value):
    region = value.split(" - ")[1].lower()

    if region == "global":
        return ["", "global"]

    return ["&region=" + region, region]


def getLane(value):
    lane = value.split(" - ")[1].lower()

    return ["?lane=" + lane, lane]
