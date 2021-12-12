# LoLalytics-scraper

Um scraper feito em python que gera arquivos de excel baseados nas tier lists do site [LoLalytics](https://lolalytics.com/).

Começando por um único script com uma url fixa que gerava um único arquivo `.csv`, resolvi ampliar um pouco o projeto para aceitar filtros escolhidos pelo usuário e criar um arquivo excel.

## Como funciona

- Será pedido informações de região, tier e lane ao usuário
- `selenium` será utilizado para visitar a página com o link criado pelas seleções do usuário
- Quando a página carregar, será feita uma busca pelos elementos de ranks e tier list
- Será feita uma limpeza nesses dados e eles serão encaminhados para o `spreadsheet`
- No `spreadsheet` será criado os arquivos de excel e diretórios para acompanhar

## Instalação

Baixe a versão de [python](https://www.python.org/downloads/) mais recente.

Para utilizar esse projeto é necessário utilizar o [Microsoft Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/), baixe a versão estável e coloque o executável em algum lugar do seu `Path`.

Após baixar o projeto, abra um terminal no diretório do projeto e use `pip install -r requirements.txt`.

Ao terminar a instalação dos pacotes, basta usar `python ./main.py` no terminal.

## Colaboradores

[Isac Martins](https://github.com/medalha01) - Ideia original e ajuda
