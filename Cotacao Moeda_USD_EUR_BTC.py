import requests
from tkinter import *


def pegarCotacoes():
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    cotacao_dic = cotacao.json()

    cotacao_dolar = cotacao_dic['USDBRL']['bid']
    cotacao_euro = cotacao_dic['EURBRL']['bid']
    cotacao_btc = cotacao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto



janela = Tk()
janela.title("Cotaçao Atual das Moedas")

texto_orientacao = Label(janela, text="Clique no botao para exibir as cotaçoes das moedas Dólar/Euro/BTC")
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Buscar Cotações", command=pegarCotacoes)
botao.grid(column=0, row=1)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2)

janela.mainloop()
