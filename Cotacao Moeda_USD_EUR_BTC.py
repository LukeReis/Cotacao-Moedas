import PySimpleGUI as sg
from cotacao import pegar_cotacoes

# Layout
sg.theme('Reddit')

layout = [
    [sg.Text('Pegar Cotaçao da Moeda')],
    [sg.InputText(key='nome_cotacao')],
    [sg.Button('Pegar Cotação'), sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')],
]

janela = sg.Window("Sistema de Cotaçoes USD EUR BTC", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Pegar Cotação':
        codigo_cotacao = valores["nome_cotacao"]
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela['texto_cotacao'].Update(f"A cotação do {codigo_cotacao} é de R${cotacao}")



janela.close()






