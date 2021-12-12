import xlsxwriter
import os


def start(champions, patch, lane, tier, region):
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
        {"header": "Games"},
        {"header": "Rank Worldwide"},
        {"header": "Winrate Worldwide"},
        {"header": "Games Worldwide"},
        {"header": "Delta"},
        {"header": "Tier"},
        {"header": "Rank"},
    ]

    filename = "{}_{}_{}.xlsx".format(region, tier, lane)
    path = "data/{}/{}".format(lane, filename)

    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
        print("Criando pastas './data/{}'".format(lane))

    print("Criando arquivo '{}'".format(filename))

    workbook = xlsxwriter.Workbook(path)

    worksheet = workbook.add_worksheet()

    tableLength = len(champions) + 5

    merge_format = workbook.add_format(
        {
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
        }
    )

    worksheet.merge_range("A1:P1", "League of Legends", merge_format)
    worksheet.merge_range("A2:P2", "Patch: {}".format(patch), merge_format)
    worksheet.merge_range("A3:P3", "Region: {}".format(region), merge_format)
    worksheet.merge_range("A4:P4", "Tier: {}".format(tier), merge_format)
    worksheet.merge_range("A5:P5", "Lane: {}".format(lane), merge_format)

    worksheet.add_table(
        "A6:P{}".format(tableLength),
        {
            "data": champions,
            "columns": columns,
        },
    )

    workbook.close()

    print("Arquivo salvo em './{}'".format(path))
