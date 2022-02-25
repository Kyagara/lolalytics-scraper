from helpers import fetch


class DataDragon:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.patch = fetch(
                "https://ddragon.leagueoflegends.com/api/versions.json").json()[0]

            print("Patch atual: {}".format(cls.patch))

            response = fetch(
                "https://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion.json".format(cls.patch)).json()["data"]

            cls.champions = {}

            for champion in response.values():
                cls.champions[champion["key"]] = champion["name"]

            print("{} champions carregados.\n".format(cls.champions.__len__()))

            cls.instance = super(DataDragon, cls).__new__(cls)

        return cls.instance

    def getChampionName(self, id: int) -> str:
        return self.instance.champions[id]

    def getCurrentPatch(self) -> str:
        return self.instance.patch
