import json
from collections import OrderedDict

def normalizar_requisicao(request):
    parametros_ordenados = OrderedDict(sorted(request.args.items(), key=lambda x: x[0]))
    return json.dumps(parametros_ordenados)

def criar_cache_key(path, request):
    return path + '?' + normalizar_requisicao(request)
