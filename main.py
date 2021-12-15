import scraper
import spreadsheet
import helpers

from helpers import regions, tiers, lanes


print(" - LoLalytics-scraper - \nVocê pode sair do programa digitando 'q'\n")

# Pedindo informações para o usuário, elas serão utilizados pelo scraper
def main():
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

    answer = input("Você quer rodar o script novamente (S/N):")

    # Verifica se a resposta está dentro do set de respostas possiveis
    if answer.lower in {"s", "sim", "yes", "y"}:
        main()


main()
