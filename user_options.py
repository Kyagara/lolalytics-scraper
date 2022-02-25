import sys


class UserOptions:
    regions = {
        0: "Global",
        1: "KR",
        2: "BR",
        3: "EUNE",
        4: "EUW",
        5: "JP",
        6: "NA",
        7: "OCE",
        8: "LAN",
        9: "LAS",
        10: "TR",
        11: "RU",
    }

    lanes = {
        0: "main",
        1: "top",
        2: "jungle",
        3: "middle",
        4: "bottom",
        5: "support",
    }

    tiers = {
        0: "challenger",
        1: "grandmaster",
        2: "master_plus",
        3: "master",
        4: "d2_plus",
        5: "diamond_plus",
        6: "diamond",
        7: "platinum_plus",
        8: "1trick",
        9: "all",
    }

    steps = {1: ["Escolha uma região:", regions, 12], 2: [
        "Escolha um tier:", tiers, 18], 3: ["Escolha uma lane:", lanes, 6]}

    def getUserOptions(self) -> tuple:
        currentStep = 1
        region = None
        tier = None
        lane = None

        while currentStep < 4:
            step = self.steps[currentStep]

            print(step[0])
            self.__printDict(step[1])
            input = self.__getInput(step[2], step[1])

            if currentStep == 1:
                region = input
            elif currentStep == 2:
                tier = input
            else:
                lane = input

            currentStep += 1

        return region, tier, lane

    def __getInput(self, maxValue: int, dict: dict) -> str:
        userInput = input(">> ")
        validAnswer = self.__isInputValid(userInput, maxValue)

        while not validAnswer:
            userInput = input("Por favor insira um valor válido.\n>> ")
            validAnswer = self.__isInputValid(userInput, maxValue)

        if not userInput:
            value = dict[0]
        else:
            value = dict[int(userInput)]

        return value.lower()

    def __isInputValid(self, input: str, maxValue: int) -> bool:
        if input.lower() == "q":
            sys.exit()

        if not input:
            return True

        if not input.isdigit():
            return False

        answer = int(input)

        if answer >= 0 and not answer >= maxValue:
            return True

    def __printDict(self, dictionary: dict):
        for key, value in dictionary.items():
            print("{} - {}".format(key, value))
