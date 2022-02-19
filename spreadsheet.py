import xlsxwriter
import os

from ddragon import DataDragon


class Spreadsheet:
    def __init__(self, tierList: list, region: str, tier: str, lane: str) -> None:
        self.tierList = tierList
        self.region = region
        self.tier = tier
        self.lane = lane
        self.patch = DataDragon().patch

    def start(self):
        # Nome do arquivo e diretório para salvar ele
        filename = "{}_{}_{}.xlsx".format(self.region, self.tier, self.lane)
        self.path = "data/{}/{}/{}".format(self.patch, self.lane, filename)

        # Caso o diretório não exista, ele será criado
        if not os.path.exists(os.path.dirname(self.path)):
            os.makedirs(os.path.dirname(self.path))
            print("Criando pastas './data/{}'".format(self.lane))

        print("Criando arquivo '{}'".format(filename))

        self.__createWorkbook()

        print("Arquivo salvo em './{}'\n".format(self.path))

    def __createWorkbook(self):
        # Criando um workbook na biblioteca Xlsxwriter
        workbook = xlsxwriter.Workbook(self.path, {"strings_to_numbers": True})

        # Criando um worksheet no documento
        worksheet = workbook.add_worksheet("Patch {}".format(self.patch))

        # Format para usar nas colunas de Games e Games Worldwide para adicionar uma virgula
        num_format = workbook.add_format({"num_format": "#,###"})

        # Colunas para a tabela do arquivo Excel
        columns = [
            {"header": "List Rank"},
            {"header": "Champion"},
            {"header": "List Tier"},
            {"header": "Lane %"},
            {"header": "Winrate %"},
            {"header": "Winrate Delta"},
            {"header": "Pick"},
            {"header": "Ban"},
            {"header": "PBI"},
            {"header": "Games", "format": num_format},
            {"header": "Rank Worldwide"},
            {"header": "Winrate Worldwide"},
            {"header": "Games Worldwide", "format": num_format},
            {"header": "Delta"},
            {"header": "Elo"},
        ]

        # Criando um header para mostrar informaçoes desse arquivo
        merge_format = workbook.add_format(
            {
                "bold": 1,
                "border": 1,
                "align": "center",
                "valign": "vcenter",
            }
        )

        # Escrevendo essas informações no header criado acima
        worksheet.merge_range("A1:O1", "League of Legends", merge_format)
        worksheet.merge_range(
            "A2:O2", "Patch: {}".format(self.patch), merge_format)
        worksheet.merge_range(
            "A3:O3", "Region: {}".format(self.region), merge_format)
        worksheet.merge_range(
            "A4:O4", "Tier: {}".format(self.tier), merge_format)
        worksheet.merge_range(
            "A5:O5", "Lane: {}".format(self.lane), merge_format)

        tableLength = len(self.tierList) + 5

        # Adicionando a tabela
        worksheet.add_table(
            "A6:O{}".format(tableLength),
            {
                "data": self.tierList,
                "columns": columns,
            },
        )

        workbook.close()
