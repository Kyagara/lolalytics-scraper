import sys
from ddragon import DataDragon
from tier_list import TierList
from user_options import UserOptions
from spreadsheet import Spreadsheet


def loop():
    print("Você pode sair do programa digitando 'q' como resposta\n")

    # Pedindo valores para o usuário
    region, tier, lane = UserOptions().getUserOptions()

    # Iniciando o processo de obter dados do site e criar uma lista com eles
    champions = TierList(region, tier, lane)
    tierList = champions.createList()

    # Iniciando o processo de salvar a tier list em um arquivo excel
    spreadsheet = Spreadsheet(tierList, region, tier, lane)
    spreadsheet.start()

    answer = input("Você quer executar o programa novamente (s/n): ")

    if answer == "":
        sys.exit()

    # Verifica se a resposta está dentro do set de respostas possiveis
    if answer.lower() in {"s", "sim", "yes", "y"}:
        loop()


if __name__ == "__main__":
    print(" - LoLalytics-scraper - \n")

    # Iniciando a classe do DataDragon, responsável por obter o patch atual e todos os champions
    DataDragon()

    # Iniciando o loop principal responsável por obter as opções do usuário
    loop()
