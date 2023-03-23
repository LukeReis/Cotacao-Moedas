# Cotacao-Moedas
Este é um programa simples em Python que utiliza a biblioteca PySimpleGUI e a API AwesomeAPI para pegar cotações de moedas.

# Como usar
Ao executar o programa, uma janela será aberta com um campo para inserir o código da moeda que deseja consultar a cotação, um botão para confirmar e outro botão para cancelar.

Ao inserir o código da moeda e clicar em "Pegar Cotação", o programa irá se conectar à API AwesomeAPI e retornar a cotação atual da moeda em Reais (BRL). O resultado será exibido na janela abaixo do botão "Pegar Cotação". 
Para obter os codigos de moeda validos basta acessar https://docs.awesomeapi.com.br.

Caso o código da moeda seja inválido, o programa irá exibir uma mensagem de erro.

# Como funciona
O programa utiliza a biblioteca requests para fazer uma requisição GET à API AwesomeAPI, passando o código da moeda como parâmetro na URL. A resposta é recebida em formato JSON e é processada para extrair a cotação atual da moeda em Reais (BRL).




