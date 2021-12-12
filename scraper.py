from selenium.webdriver.common.by import By
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def start(lane, tier, region):
    # Opções do Edge
    chrome_options = EdgeOptions()
    chrome_options.use_chromium = True
    chrome_options.headless = True
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument("--log-level=3")

    print(
        "Região: {}\nTier: {}\nLane: {}\n".format(
            region[1],
            tier[1],
            lane[1],
        )
    )

    print("Inicializando Edge")

    # Abrindo Edge com opções
    driver = Edge(options=chrome_options)

    link = "https://lolalytics.com/lol/tierlist/{}{}{}".format(
        lane[0], tier[0], region[0]
    )

    # Abrindo site
    driver.get(link)

    # Verificando se o site carregou
    assert "LoL Tier List" in driver.title
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, ".TierList_list__2tHpq")
        )
    )

    print("Site '{}' carregado".format(link))

    # Pegando versão do patch
    patch = (
        driver.find_element(By.CSS_SELECTOR, ".TierList_description__1vIx2")
        .find_element(By.TAG_NAME, "h2")
        .text
    )

    patchVersion = patch.replace("LEAGUE OF LEGENDS PATCH ", "")

    # Pegando a tier list
    tierList = driver.find_element(By.CSS_SELECTOR, ".TierList_list__2tHpq")

    # Pegando elementos
    rows = tierList.find_elements(By.XPATH, "./*")

    # Pegando tiers
    tiersList = tierList.find_elements(By.CSS_SELECTOR, ".Elo_elo__1FJZ4 > *")

    # Valores para serem usados no loop
    champions = []
    tiers = []
    ranks = {"I", "II", "III", "IV"}
    grade = {
        "S+",
        "S",
        "S-",
        "A+",
        "A",
        "A-",
        "B+",
        "B",
        "B-",
        "C+",
        "C",
        "C-",
        "D+",
        "D",
        "D-",
    }

    # Separando tiers
    for rank in tiersList:
        elemClass = rank.get_attribute("class")

        if elemClass == "Elo_grandmaster__2XjYq":
            tiers.append("Grandmaster")

        if elemClass == "Elo_master__1pj6b":
            tiers.append("Master")

        if elemClass == "Elo_diamond__35Qce":
            tiers.append("Diamond")

    # Separando champions
    index = 0
    for row in rows:
        text = row.text

        if len(text) == 0:
            continue

        # Retirando newlines e virgulas
        string = text.replace("\n", " ").replace(",", "")

        champion = string.split(" ")

        # Organizando nomes de champions, evitando que por exemplo 'Lee Sin' seja dois valores na array
        if champion[2] not in grade:
            name = champion[2]
            champion[1] = champion[1] + " " + name
            champion.pop(2)

        # Organizando números dos tiers
        if champion[-1][0] == "-" or champion[-1][0].isdigit():
            champion.append("I")
        else:
            if champion[-1] not in ranks:
                champion.append(champion[-1])

        # Adicionando tier ao champion e adicionando ele a lista de champions
        champion.insert(-1, tiers[index])
        index += 1
        champions.append(champion)

    return champions, patchVersion
