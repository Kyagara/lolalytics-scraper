# LoLalytics-scraper

Um scraper feito em python que gera arquivos de excel baseados nas tier lists do site [LoLalytics](https://lolalytics.com/).

## Why

Por pedido de um amigo eu tinha criado um script em python que gerava um arquivo `.csv` com uma URL de alguma tier list que ele quisesse, depois de um tempo eu decidi práticar um pouco de python e usar ferramentas como `selenium` para expandir o projeto, quando descobri que existe um endpoint utilizado pelo LoLalytics, decidi refazer o projeto usando classes e removendo `selenium`.

Esse projeto usa o endpoint `https://axe.lolalytics.com/` e obtém dados que estão sobre copyright do LoLalytics, ele **não** foi criado com o intuito de violar copyright e/ou ser usado em algum outro lugar que não seja para uso pessoal.

## Como funciona

-   Ao iniciar o projeto, ele irá fazer dois pedidos para o [Data Dragon](https://developer.riotgames.com/docs/lol#data-dragon), obtendo o patch atual e todos os champions dele utilizando a classe `DataDragon`
-   Ele irá perguntar as opções que o usuário quer usar para formar um pedido para o enpoint do LoLalytics utilizando a classe `UserOptions`
-   Depois de obter os dados, ele irá fazer cálculos para gerar a tier list utilizando a classe `TierList`
-   Depois de gerar uma tier list, o projeto irá utilizar a classe `Spreadsheet` para criar o arquivo excel e separar ele entre pastas

## Instalação

É necessário ter [python](https://www.python.org/downloads/) instalado.

Após baixar o projeto, abra um terminal no diretório do projeto e use o comando `pip install -r requirements.txt`.

Ao terminar a instalação das dependências, basta usar o comando `python ./main.py` no terminal.

## Macros

Você pode acelerar a criação de spreadsheets adicionando macros no arquivo `macros.yaml`, eles precisam seguir o seguinte padrão:

```yaml
nome_do_macro:
    region: br
    tier: platinum_plus
    lane: top
```

Valores que podem ser usados podem ser encontrados no arquivo `user_options.py`. Para usar um macro basta colocar o nome dele na execução do programa, como por exemplo: `python ./main.py nome_do_macro`.

## Colaboradores

[Isac Martins](https://github.com/medalha01) - O amigo e também a pessoa que ajudou com a matemágica

## Legal

### LoLalytics

LoLalytics-scraper uses data obtained from an endpoint meant for lolalytics.com visitors use only, this data is under lolalytics.com copyright. This project was **not** made with the intention of violating copyright and/or for being used for something that isn't personal use.

### League of Legends

LoLalytics-scraper isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.
