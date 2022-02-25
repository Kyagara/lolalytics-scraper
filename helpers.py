import sys
import requests


def fetch(url: str) -> requests.Response:
    try:
        response = requests.get(url)
    except:
        print("Não foi possivel fazer um pedido para a url '{}', fechando programa.".format(url))
        sys.exit()

    if response.status_code != 200:
        print("O site respondeu com um erro '{}' ao fazer um perdido para a url '{}', fechando programa.".format(
            response.status_code, url))

        sys.exit()

    return response


def toFloat(value: int) -> float:
    return float(format(value, ".2f"))
