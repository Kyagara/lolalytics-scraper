import os
import sys
import scraper
import spreadsheet
import helpers

from helpers import regions, tiers, lanes

from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Usando webdriver_manager para automaticamente instalar o driver do Edge
try:
    # Instalando web driver do Edge
    bin = EdgeChromiumDriverManager().install()
    # Verificando se o path existe
    assert os.path.exists(bin)
except:
    print("Ocorreu um erro ao instalar o web driver do edge\n")
    sys.exit(1)


print(" - LoLalytics-scraper - \n")


# Pedindo informações para o usuário, elas serão utilizados pelo scraper
def main():
    print("Você pode sair do programa digitando 'q' como resposta\n")

    print("Escolha uma região:")
    helpers.printChoices(regions)
    regionInput = helpers.getUserInput(0, 12)
    region = helpers.getRegion(regions[regionInput])
    print("Você escolheu a região: {}\n".format(region[1]))

    print("Escolha um tier:")
    helpers.printChoices(tiers)
    tierInput = helpers.getUserInput(0, 18)
    tier = helpers.getTier(tiers[tierInput])
    print("Você escolheu o tier: {}\n".format(tier[1]))

    print("Escolha uma lane:")
    helpers.printChoices(lanes)
    laneInput = helpers.getUserInput(0, 6)
    lane = helpers.getLane(lanes[(laneInput)])
    print("Você escolheu a lane: {}\n".format(lane[1]))

    # Começando o processo de pegar a tier list do site
    result = scraper.start(lane, tier, region)

    # Começando o processo de salvar a tier list para um arquivo excel
    spreadsheet.start(result[0], result[1], lane[1], tier[1], region[1])

    answer = input("Você quer executar o programa novamente (s/n): ")

    # Verifica se a resposta está dentro do set de respostas possiveis
    if answer.lower() in {"s", "sim", "yes", "y"}:
        main()


main()
