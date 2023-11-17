# ponderada4m8

## Descrição do Projeto

A ponderada requer a criação de um chatbot com expressões regulares. O chatbot desenvolvido é capaz de identificar as seguintes expressões:

- `(?:diri(gir|ja))`: Identifica palavras como "dirigir", "dirija"
- `(?:conduz(ir|a))`: Identifica palavras como "conduzir", "conduza"
- `(?:movimentar)`: Identifica a palavra "movimentar".
- `(?:mov(er|a))`: Identifica palavras como "mover" ou "move".
- `(?:encontr(ar|e))`: Identifica palavras como "encontrar" ou "encontre".
- `(?:gui(ar|e))`: Identifica palavras como "guiar" ou "guie".
- `(?:ir)`: Identifica a palavra "ir".

e é capaz de levar aos seguintes lugares:

- biblioteca
- garagem
- fazol (faz o l Nicola)

## Como rodar o projeto

1. Clone o repositório
2. na pasta do projeto, execute o comando colcon build.
3. na pasta do projeto, execute o comando  ```bash source  pacote/install/setup.bash```
4. na pasta do projeto, execute o comando ros2 run pacote chat_bot

## Como testar o projeto

No terminal digite 1 se quiser a lista de locais, exit se deseja sair. Para executar o chatbot, digite a frase que deseja testar. Ela deve ter a seguinte estrutura: verbo_acao + local (ex: ir para a biblioteca). O chatbot irá responder com a frase "indo para "+local+" na posição "+str(position)

## Vídeo

Existe um vídeo no youtube <https://youtu.be/dip6wAV0iaY>
