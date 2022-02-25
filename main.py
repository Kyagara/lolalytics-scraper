import sys
import yaml

from ddragon import DataDragon
from tier_list import TierList
from user_options import UserOptions
from spreadsheet import Spreadsheet


def mainLoop():
    print("Você pode sair do programa digitando 'q' como resposta\n")

    # Pedindo valores para o usuário
    region, tier, lane = UserOptions().getUserOptions()

    spreadsheet(region, tier, lane)

    answer = input("Você quer executar o programa novamente (s/n): ")

    if not answer:
        print("Fechando programa")
        sys.exit()

    # Verifica se a resposta está dentro do set de respostas possiveis
    if answer.lower() in {"s", "sim", "yes", "y"}:
        mainLoop()


def spreadsheet(region: str, tier: str, lane: str):
    # Iniciando o processo de obter dados do site e criar uma lista com eles
    champions = TierList(region, tier, lane)
    tierList = champions.createList()

    # Iniciando o processo de salvar a tier list em um arquivo excel
    spreadsheet = Spreadsheet(tierList, region, tier, lane)
    spreadsheet.start()


def readMacros() -> dict:
    try:
        with open('./macros.yaml', "r") as f:
            return yaml.safe_load(f)
    except:
        print("Não foi possivel abrir o arquivo 'macros.yaml'")
        sys.exit()


if __name__ == "__main__":
    print(" - LoLalytics-scraper - \n")

    # Iniciando a classe do DataDragon, responsável por obter o patch atual e todos os champions
    DataDragon()

    # Obtendo argumentos usados
    args = sys.argv[1:]

    # Se houver algum argumento, usar ele para verificar se um macro com o mesmo nome existe
    if len(args) > 0:
        macros = readMacros()

        if args[0] in macros:
            print("Macro '{}' carregado".format(args[0]))

            values = macros[args[0]]
            spreadsheet(values["region"], values["tier"], values["lane"])
        else:
            print("Macro não encontrado, valores disponíveis:\n{}".format(
                list(macros.keys())))
    else:
        # Iniciando o loop principal responsável por obter as opções do usuário
        mainLoop()
