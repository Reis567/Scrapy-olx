# Projeto de Raspagem de Dados da OLX 

## Descrição

Este é um projeto de raspagem de dados que tem como objetivo coletar informações sobre notebooks anunciados na plataforma OLX no estado do Rio de Janeiro. A raspagem é realizada em 14 páginas da OLX, coletando detalhes sobre os anúncios, como título e preço.

## Funcionalidade

O projeto é desenvolvido usando o framework Scrapy, uma poderosa ferramenta de raspagem de dados em Python. O spider  desenvolvido neste projeto visita várias páginas da OLX, extrai os dados relevantes dos anúncios de notebooks e os armazena em um arquivo JSON.

## Configuração

Antes de executar o projeto, é necessário garantir que o ambiente Python e as dependências necessárias estejam configuradas. Aqui estão os passos básicos para configurar o ambiente:

1. Certifique-se de ter Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Instale o Scrapy, que é usado para realizar a raspagem de dados. Você pode instalar o Scrapy usando o pip:

   ```bash
   pip install Scrapy
   ```

## Executando o Projeto

Após configurar o ambiente, você pode executar o projeto seguindo estes passos:

1. Abra um terminal ou prompt de comando.

2. Navegue até o diretório do projeto:

   ```bash
   cd BaseProject
   ```

3. Execute o spider usando o seguinte comando:

   ```bash
   scrapy crawl olx -o output.json
   ```

   Isso iniciará o spider chamado "olx" e os dados raspados serão armazenados no arquivo `output.json`.

## Resultados

Os resultados da raspagem serão armazenados no arquivo `output.json`. Este arquivo conterá informações sobre os notebooks anunciados na OLX no estado do Rio de Janeiro.
