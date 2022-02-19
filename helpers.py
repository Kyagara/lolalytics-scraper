import sys
import requests


def fetch(url: str) -> requests.Response:
    response = requests.get(url)

    if response.status_code != 200:
        print("O site respondeu com um erro '{}' ao fazer um perdido para a url '{}', fechando programa.".format(
            response.status_code, url))

        sys.exit(0)

    return response


def toFloat(value: int) -> float:
    return float(format(value, ".2f"))
