import xlsxwriter
import os


def start(champions, patch, lane, tier, region):
    # Nome do arquivo e diretório para salvar ele
    filename = "{}_{}_{}.xlsx".format(region, tier, lane)
    path = "data/{}/{}".format(lane, filename)

    # Caso o diretório não exista, ele será criado
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
        print("Criando pastas './data/{}'".format(lane))

    print("Criando arquivo '{}'".format(filename))

    # Criando um workbook na biblioteca Xlsxwriter
    workbook = xlsxwriter.Workbook(path, {"strings_to_numbers": True})

    # Criando um worksheet no documento
    worksheet = workbook.add_worksheet("Patch {}".format(patch))

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
        {"header": "Tier"},
        {"header": "Rank"},
    ]

    tableLength = len(champions) + 5

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
    worksheet.merge_range("A1:P1", "League of Legends", merge_format)
    worksheet.merge_range("A2:P2", "Patch: {}".format(patch), merge_format)
    worksheet.merge_range("A3:P3", "Region: {}".format(region), merge_format)
    worksheet.merge_range("A4:P4", "Tier: {}".format(tier), merge_format)
    worksheet.merge_range("A5:P5", "Lane: {}".format(lane), merge_format)

    # Adicionando a tabela
    worksheet.add_table(
        "A6:P{}".format(tableLength),
        {
            "data": champions,
            "columns": columns,
        },
    )

    workbook.close()

    print("Arquivo salvo em './{}'\n".format(path))
