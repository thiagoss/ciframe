import json
from collections import OrderedDict

UM_SEGUNDO = 1
UM_MINUTO = 60 * UM_SEGUNDO
UMA_HORA = 60 * UM_MINUTO
UM_DIA = 24 * UMA_HORA

def normalizar_requisicao(request):
    parametros_ordenados = OrderedDict(sorted(request.args.items(), key=lambda x: x[0]))
    return json.dumps(parametros_ordenados)

def criar_cache_key(path, request):
    return path + '?' + normalizar_requisicao(request)

def salvar_em_cache(cliente, chave, valor, ttl):
    cliente.set(chave, valor)
    cliente.expire(chave, UM_DIA)

