from interface_grafica import *
from consulta_cep import *

tela_inicial()

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Consultar':
        try:
            logradouro = consulta(values['cep'])['logradouro']
            bairro = consulta(values['cep'])['bairro']
            localidade = consulta(values['cep'])['localidade']
            uf = consulta(values['cep'])['uf']
            população = consulta(values['cep'])['populacao']
            ddd = consulta(values['cep'])['ddd']

            window['logradouro'].update(logradouro)
            window['bairro'].update(bairro)
            window['localidade'].update(localidade)
            window['uf'].update(uf)
            window['população'].update(população)
            window['ddd'].update(ddd)
        except:
            sg.popup('CEP inválido!', title='Erro')
            window['logradouro'].update('')
            window['bairro'].update('')
            window['localidade'].update('')
            window['uf'].update('')
            window['população'].update('')
            window['ddd'].update('')
