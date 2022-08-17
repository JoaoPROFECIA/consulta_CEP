import requests


def consulta_cep(cep):
    """
    -> Função que faz a consulta do CEP.
    :param cep: Passa o CEP a ser consultado.
    :return: Retorna os dados da consulta no formato json.
    """
    url = 'https://viacep.com.br/ws/%s/json/' % cep
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    return response_json


def consulta_ddd(ddd):
    """
    -> Função que faz a consulta do DDD.
    :param ddd: Passa o DDD a ser consultado.
    :return: Retorna os dados da consulta no forma json.
    """
    url = 'https://brasilapi.com.br/api/ddd/v1/%s' % ddd
    response = requests.get(url)
    response_json = response.json()
    response_json['cities'] = response_json['cities'][::-1]  # inverter ordem de 'cities'
    return response_json


estados = {'AC': 'ACRE',
           'AL': 'ALAGOAS',
           'AP': 'AMAPÁ',
           'AM': 'AMAZONAS',
           'BA': 'BAHIA',
           'CE': 'CEARÁ',
           'DF': 'DISTRITO FEDERAL',
           'ES': 'ESPÍRITO SANTO',
           'GO': 'GOIÁS',
           'MA': 'MARANHÃO',
           'MT': 'MATO GROSSO',
           'MS': 'MATO GROSSO DO SUL',
           'MG': 'MINAS GERAIS',
           'PA': 'PARÁ',
           'PB': 'PARAÍBA',
           'PR': 'PARANÁ',
           'PE': 'PERNAMBUCO',
           'PI': 'PIAUÍ',
           'RJ': 'RIO DE JANEIRO',
           'RN': 'RIO GRANDE DO NORTE',
           'RS': 'RIO GRANDE DO SUL',
           'RO': 'RONDÔNIA',
           'RR': 'RORAIMA',
           'SC': 'SANTA CATARINA',
           'SP': 'SÃO PAULO',
           'SE': 'SERGIPE',
           'TO': 'TOCANTINS'
}
