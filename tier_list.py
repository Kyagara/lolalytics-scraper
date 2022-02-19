import sys
from ddragon import DataDragon
from helpers import fetch, toFloat


class TierList:
    listTiers = ["S+", "S", "S-", "A+", "A", "A-", "B+",
                 "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]

    ranks = ["IV", "III", "II", "I"]

    def __init__(self, region: str, tier: str, lane: str) -> None:
        self.region = region
        self.tier = tier
        self.lane = lane

    def createList(self) -> list:
        print(
            "\nRegião: {}\nTier: {}\nLane: {}\n".format(
                self.region,
                self.tier,
                self.lane,
            )
        )

        self.response = self.__fetchData()
        tierList = self.__getChampions()

        return tierList

    def __fetchData(self) -> dict:
        ddragon = DataDragon()

        url = "https://axe.lolalytics.com/tierlist/1/?lane={}&patch={}&tier={}&queue=420&region={}".format(
            self.lane, ddragon.patch, self.tier, self.region
        )

        response = fetch(url).json()

        return response

    def __getChampions(self) -> list:
        cids = self.response["cid"]
        totals = self.response["totals"]
        win = self.response["win"]
        pick = self.response["pick"]

        champions = []

        avgWin = win / pick * 100

        for cid in cids:
            data = cids[cid]

            if data[0] == 0:
                continue

            # Champion, posição e tier na lista
            listRank = data[0]
            name = DataDragon().getChampionName(cid)
            listTier = self.listTiers[data[2] - 1]

            # Performance do champion no elo selecionado
            lanePercent = toFloat((data[4] / data[5]) * 100)
            winRate = toFloat((data[3] / data[4]) * 100)
            avgWinDelta = toFloat((data[3] / data[4]) * 100 - avgWin)
            pickRate = toFloat(data[4] / totals[data[1]] * 200)
            banRate = toFloat(data[6])
            pbi = toFloat(avgWinDelta * (pickRate * 100 / (100 - banRate)))
            games = data[4]

            # Performance Worldwide
            rankWorldwide = data[7]
            winRateWorldwide = float(data[8])
            gamesWorldwide = data[9]
            delta = toFloat(float(data[8]) - data[3] / data[4] * 100)

            eloValue = int(data[10] / 100)

            if eloValue >= 9:
                elo = "Challenger"
            elif eloValue >= 5:
                elo = "Grandmaster"
            elif eloValue >= 4:
                elo = "Master"
            else:
                elo = "Diamond {}".format(self.ranks[eloValue])

            champions.append([listRank, name, listTier, lanePercent, winRate, avgWinDelta, pickRate,
                              banRate, pbi, games, rankWorldwide, winRateWorldwide, gamesWorldwide, delta, elo])

        if len(champions) == 0:
            print("A lista não pode ser criada por falta de champions na tier list.")
            sys.exit()

        champions.sort()

        return champions
