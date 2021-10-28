import requests as req
import json

URI = ' http://viacep.com.br/ws/'

path = "ruas_pvh.json"

f = open(path, encoding="utf8")

ruas = json.load(f)


def set_locais(rua):
    URL = req.request('GET', URI + 'RO' + '/Porto Velho/' + rua + '/json')
    return URL


for rua in ruas:
    URL = set_locais(rua)
    enderecos = URL.json()
    for endereco in enderecos:
        print(endereco['cep'], endereco['logradouro'], endereco['complemento'], endereco['bairro'], endereco['localidade'], endereco['uf'])
