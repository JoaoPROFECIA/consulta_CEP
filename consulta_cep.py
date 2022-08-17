def consulta(cep):
    import requests
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    response_json = response.json()
    return response_json
